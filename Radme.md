Python library offering a class for hand detection mixing diverse methods using opencv and inspired on this sources: https://github.com/lzane/Fingers-Detection-using-OpenCV-and-Python/tree/py2_opencv2 https://github.com/sashagaz/Hand_Detection

This model is madeup on Linux but is also compatible with windows (tested on windows 10 [2018 version])_

The HandDetection class let the user get the hand detection from an image or the own class can get the camera capture task. Currently it only draw the points of the fingers on the original image.

This project is written in Python 3.6.8 The following libraries are used in this project and neccessary to be add to your computer:

system - usually comes with python 3
Time - usually comes with Python 3
OpenCV (3.2.0) - http://docs.opencv.org
NumPy (1.14.5) - http://www.numpy.org

The library can be executed for it own test with: python3 Real_time_hand_gesture_recognition.py

When running the python file, you can expect to see the real time frame from your camera with a bounding rectangular framing your hand. The bounding rectangular will contain green circles corresponding to the fingertips and finger webbing. The center mass of your hand will also appear in the bounding rectangular. A number on the upper left side of the frame corresponds to the number of pointed fingers.

To increase accuracy of the gesture recognition, it is recommended to run the code in a bright light room. Additionally, the code can analyze one hand (either left or right), and the hand needs to be in front of the camera.