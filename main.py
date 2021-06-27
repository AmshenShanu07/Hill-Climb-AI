#Importing all the needed files
import cv2 as cv #OpenCV2
from mediapipe.python.solutions import drawing_utils, holistic #MediaPipe
from pynput.keyboard import Controller, Key #Keyboard controler and keys


cam = cv.VideoCapture(0)    #Reading the webcam
draw = drawing_utils    #Helps to draw the coordinates by mediapipe 
keyboard = Controller() #Keyboard controller


#Our Program Engine starts here
with holistic.Holistic(min_detection_confidence=0.5,min_tracking_confidence=0.5) as holi: 
    while True:
        ret,frame = cam.read() #reading the image from the webcam

        img = cv.cvtColor(frame,cv.COLOR_BGR2RGB) #converting BGR to RGB
        results = holi.process(img) #Giving the image to mediapipe to process

        #drawing the right and left hand coordinates
        draw.draw_landmarks(img,results.right_hand_landmarks,holistic.HAND_CONNECTIONS)
        draw.draw_landmarks(img,results.left_hand_landmarks,holistic.HAND_CONNECTIONS)

        #if the hand is not shown in the screen there is a chance of getting error
        try:

            #Getting all the coordinate points from both hands
            RightLandmarks = results.right_hand_landmarks.landmark
            LeftLandmarks = results.left_hand_landmarks.landmark

            #Checking the right hand if closed or not
            if RightLandmarks[8].y > RightLandmarks[7].y and RightLandmarks[12].y > RightLandmarks[11].y and RightLandmarks[16].y > RightLandmarks[15].y and RightLandmarks[20].y > RightLandmarks[19].y:
                
                #writting text on the screen
                cv.putText(img,'Right',(10,400), cv.FONT_HERSHEY_COMPLEX, 1,(255,0,127),2)
                
                #Pressing the keyboard right arrow key
                keyboard.release(Key.left)
                keyboard.press(Key.right)
                
            #Checking the left hand if closed or not
            elif LeftLandmarks[8].y > LeftLandmarks[7].y and LeftLandmarks[12].y > LeftLandmarks[11].y and LeftLandmarks[16].y > LeftLandmarks[15].y and LeftLandmarks[20].y > RightLandmarks[19].y:
                
                #writting text on the screen
                cv.putText(img,'Left',(550,400), cv.FONT_HERSHEY_COMPLEX, 1,(255,0,127),2)

                #Pressing the keyboard left arrow key
                keyboard.release(Key.right)
                keyboard.press(Key.left)

            else:
                #Releasing both keys if the hand is not closed
                keyboard.release(Key.right)
                keyboard.release(Key.left)
                

        except:

            #if the hand is not shown in the screen, Releasing both keys
            keyboard.release(Key.right)
            keyboard.release(Key.left)

        #Converting the RGB to BGR cause cv2 format is BGR 
        img = cv.cvtColor(img,cv.COLOR_RGB2BGR)

        #Displaying the processed imaged
        cv.imshow('CountFingure',img)

        #Wait for 1ms 
        key = cv.waitKey(1)

        #checking if the "q" key is pressed the loop will exit
        if key == ord('q'):
            break



cam.release()   #releasing the cam 
cv.destroyAllWindows()  #Destroying all the windows opened by OpenCv