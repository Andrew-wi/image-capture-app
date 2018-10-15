import cv2

cameraPort = 0

calibrateFrames = 30

camera = cv2.VideoCapture(cameraPort)

def getImage():
    retval, im = camera.read()
    return im

for frame in range(calibrateFrames):
    temp = getImage()

print("Taking image..........NOW!!!!!")

image = getImage()

file = "/Users/andrewwinnicki/desktop/camera.png"

cv2.imwrite(file, image)

del(camera)
