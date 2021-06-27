import cv2 as cv
from mediapipe.python.solutions import drawing_utils, holistic
from pynput.keyboard import Controller, Key

cam = cv.VideoCapture(0)
draw = drawing_utils
holistics = holistic
keyboard = Controller()

with holistic.Holistic(min_detection_confidence=0.5,min_tracking_confidence=0.5) as holi:
    while True:
        ret,frame = cam.read()

        img = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
        results = holi.process(img)

        draw.draw_landmarks(img,results.right_hand_landmarks,holistic.HAND_CONNECTIONS)
        draw.draw_landmarks(img,results.left_hand_landmarks,holistic.HAND_CONNECTIONS)
        try:
            RightLandmarks = results.right_hand_landmarks.landmark
            LeftLandmarks = results.left_hand_landmarks.landmark

            if RightLandmarks[8].y > RightLandmarks[7].y and RightLandmarks[12].y > RightLandmarks[11].y and RightLandmarks[16].y > RightLandmarks[15].y and RightLandmarks[20].y > RightLandmarks[19].y:
                cv.putText(img,'Right',(10,400), cv.FONT_HERSHEY_COMPLEX, 1,(255,0,127),2)
                keyboard.release(Key.left)
                keyboard.press(Key.right)
                
                

            elif LeftLandmarks[8].y > LeftLandmarks[7].y and LeftLandmarks[12].y > LeftLandmarks[11].y and LeftLandmarks[16].y > LeftLandmarks[15].y and LeftLandmarks[20].y > RightLandmarks[19].y:
                cv.putText(img,'Left',(550,400), cv.FONT_HERSHEY_COMPLEX, 1,(255,0,127),2)
                keyboard.release(Key.right)
                keyboard.press(Key.left)
            else:
                keyboard.release(Key.right)
                keyboard.release(Key.left)
                

        except:
            keyboard.release(Key.right)
            keyboard.release(Key.left)

        img = cv.cvtColor(img,cv.COLOR_RGB2BGR)
        cv.imshow('CountFingure',img)

        key = cv.waitKey(1)

        if key == ord('q'):
            break



cam.release()
cv.destroyAllWindows()