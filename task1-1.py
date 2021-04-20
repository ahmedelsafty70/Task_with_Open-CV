from cv2 import cv2

img = cv2.imread("chair.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

width, height = gray.shape
upper_left = (width // 4, height // 4)
bottom_right = (width * 3 // 4, height * 3 // 4)
cv2.rectangle(img,upper_left,bottom_right, (0,0,255) , -1)


cv2.imshow("Gray image",gray)
cv2.imshow("squared img",img)


cv2.waitKey(0)
cv2.destroyAllWindows()
