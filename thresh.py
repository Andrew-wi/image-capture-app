import cv2

#store image using imread() method (from cv2 library) in img variable
img = cv2.imread('/Users/andrewwinnicki/desktop/camera.png', 0)

#threshold the image (built-in cv2 method)
threshed = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
#for mobile screen, lower thresh = 215 works well
#for paper, lower thresh = 

#print and save
print('Thresholded image...')

file = '/Users/andrewwinnicki/desktop/image.png'

print('Saving image...')

cv2.imwrite(file, threshed)
