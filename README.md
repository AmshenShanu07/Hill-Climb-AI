# Hill Climb Racing Ai

This is a type of AI that can read your both palms to control Hill Climb, It will help you to accelerate the car in the game by closing your right hand palm and you can press brake/back by closing your left hand palm 


## Technologies used

- OpenCv :- it is a huge open-source library for the computer vision, machine learning, and image processing and now it plays a major role in real-time operation which is very important in today's systems. By using it, one can process images and videos to identify objects, faces, or even handwriting of a human.
- MediaPipe :-  MediaPipe Holistic, with its 540+ key points, aims to enable a holistic, simultaneous perception of body language, gesture and facial expressions. Its blended approach enables remote gesture interfaces, as well as full-body AR, sports analytics, and sign language recognition.
- Pynput :- This library allows you to control and monitor input devices. Currently, mouse and keyboard input and monitoring are supported.
## How it works

OpeCv will take your both hand's image using your pc or lap webcam and it will pass the image to mediapipe, Mediapipe will take that image and do a full scan, after scanning the image it will find the main coordinates in your both palms. By this coordinated you can find if the hand is colsed or oppend. Pynput will help you to press the keybord keys, by this library we will controll the gas and brake in the game,  This is the basic working

<img src="https://1nwu8i3sj55rdbw4k4fm55i1-wpengine.netdna-ssl.com/wp-content/uploads/2021/04/1_fMBLvkdLbg0MEfv7KbJZjQ.png" />


In this image you can see the coordinates that mediapipe can understand on your hand, each coordinate point has a id it is respresented in the above picture. So if you fold your palm the coordinate number 8,12,16,20 will come under the coordinate 7,11,15,2 By this method you can find if the palm is open or closed. Then we can come to the main part. So we sucessfully find if the hand is closed or not and we will use the pynput library to take control over our keyboard so we can control our game by our script So BOOM 

 ## How to control

Your can press the "Gas" by folding your right hand palm, And press "Brake/Back" by folding your left hand, You can't press both "Gas" and "Brake" together, if you close your both palms it will press "Gas" because its a if condition its the right hand condition at the first so it will match the first condition and press "Gas"


## Things to Note


- Make sure that you are on the game window after running the script else it will to control your game
- Show your both hands to the screen, It will not read only one hand
- Make sure all the coordinates are perfectly placed on your hand by looking at your cam screen


# How to  run this?

## Prerequisite
- Maily your pc shound have a webcam
- Python 3.9.0
- must install all requirements in the requirements.txt file

## How to run?

- Install all the requiremets needed for this script by the command ```pip install - r requirements.txt```
- Run your script by ```python main.py```

 

