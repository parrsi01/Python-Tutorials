#Date: 01/12/2021
# Author: Simon Parrs
# Title: Image and Video Processing with Python

import cv2


img = cv2.imread("galaxy.jpg",0)

print(type(img))
print(img)
print(img.shape)
print(img.ndim)

resized_image = cv2.resized(img,(1000,500))
cv2.imshow("Galaxy", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
