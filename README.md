# Image Capturing App

### Updates

#### Day 2. October 15

#### Day 1. October 14/15:
Today, initialized git repo and connected to the remote host on github. Yesterday we implemented the capturing of an image using the built in camera (port 0). The first step was initializing some variables, namely the camera port (assumed to be 0 for a built in camera), and the number of frames that will be ignored by the computer (this was 30). The reason for skipping 30 consecutive frames becomes apparent when we see the for loop through through 30 frames, during which we see calibration of the camera (so that proper light levels can be calculated from the camera–I assume this is built into the camera framework itself). I construct a cv2 object, our camera, and use the read() method and imread() method to get the image and save the image, then delete the .camera() object. Future implementation of features will come, probably going to work on thresholding today. 
