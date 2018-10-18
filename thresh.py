import cv2

#store image using imread() method (from cv2 library) in img variable
img = cv2.imread('/Users/andrewwinnicki/desktop/camera.png', 0)

#threshold the image (built-in cv2 method)
ret, threshed = cv2.threshold(img, 115, 255, cv2.THRESH_BINARY)
#for mobile screen, lower thresh = 215 works well
#for paper, lower thresh = 

#print and save
print('Thresholded image...')

file = '/Users/andrewwinnicki/desktop/image.png'

print('Saving image...')

cv2.imwrite(file, threshed)
