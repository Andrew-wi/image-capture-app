import cv2

#initialize variables
cameraPort = 0

calibrateFrames = 30

#make camera object
camera = cv2.VideoCapture(cameraPort)

#define getimage function
def getImage():
    retval, im = camera.read()
    return im
#calibrate camera (take 30 pictures in a row, no save)
for frame in range(calibrateFrames):
    temp = getImage()

#take image and save
print("Taking image..........NOW!!!!!")

image = getImage()

file = "/Users/andrewwinnicki/desktop/camera.png"

cv2.imwrite(file, image)

del(camera)
