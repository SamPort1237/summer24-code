# summer24-code
Open Cv Code for Summer24 semester co-op. Mostly hand gesture recognition.

Face Detection Project, Face Mesh Project, and Pose Estimation Project are as stated and can be used for futher ideas such as using the pose detesction to follow someone or stuff like that.

I was working on Gesture control by using the Hand Tracking Project files. The initial py files in the folder are basic codes and can be gone through to futher understand how mediapipe and open cv work, but the main files I have been using are in the hand-gesture-recognition-mediapipe-main folder.

The files StopTest.py and RobotControls.py work ogether to follow hand gestures and produce results (for now that is just giving an output) with StopTest being the main run file.
Run StopTest.py and play around with it a little bit or even the app.py file as well to gain more of an understanding.
The lines I have changed in StopTest.py vs the app.py provided in the other GitHub files are lines 45-50 and 181-239 which is how the program detects the hand gesture and calls to the RobotControls.py to produce results.
Refer to the video I linked in the Summer24 List to better understand the hand-gesture-recognition-mediapipe-main. It will help you understand how it works, how to change parts of it, and how to build your own hand gestures. 

The GestureCode.py and GestureCode2.py are files I have tried to work on to connect python to ROS2 by calling the StopTest and RobotControl codes. This is where I struggled as this is not my area of expertise. 
I reccomend looking into the other links I provided if you need help with this part and asking for help if needed.
