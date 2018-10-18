# Image Capturing App

## Description
Image capturing app. Can be modified into many things, but v1 will be capture of text on a page, so that we can transform it into notes.

### Updates

#### Day 3. October 18
Plan of attack: threshold image, translate into txt document – after that, can easily transform this with a natural language processing program. Need to find appropriate libraries for this.

#### Day 2. October 15
Able to threshold image. Simply imported cv2 library, used .threshold() method to threshold the image in a binary fashion (below threshold = white, above threshold = black) and saved it using imwrite(). Thresholds for a screen picture vs a paper picture were very different, by about 100. Was not able to work on it on October 16 because math and robotics. 

#### Day 1. October 14/15:
Today, initialized git repo and connected to the remote host on github. Yesterday we implemented the capturing of an image using the built in camera (port 0). The first step was initializing some variables, namely the camera port (assumed to be 0 for a built in camera), and the number of frames that will be ignored by the computer (this was 30). The reason for skipping 30 consecutive frames becomes apparent when we see the for loop through through 30 frames, during which we see calibration of the camera (so that proper light levels can be calculated from the camera–I assume this is built into the camera framework itself). I construct a cv2 object, our camera, and use the read() method and imread() method to get the image and save the image, then delete the .camera() object. Future implementation of features will come, probably going to work on thresholding today. 
