import cv2

img = cv2.imread('/Users/andrewwinnicki/desktop/camera.png', 0)

ret, threshed = cv2.threshold(img, 115, 255, cv2.THRESH_BINARY)
#for mobile screen, lower thresh = 215 works well
#for paper, lower thresh = 

print('Thresholded image...')

file = '/Users/andrewwinnicki/desktop/image.png'

print('Saving image...')

cv2.imwrite(file, threshed)
