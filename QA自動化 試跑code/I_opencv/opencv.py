import cv2

img_rgb = cv2.imread("C:\\python_code\\I_opencv\\1.PNG")
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
cv2.imwrite('img_gray.PNG', img_gray)

edges = cv2.Canny(img_gray, 110, 140)

cv2.imshow('edges', edges)

# Press any key to close the image
cv2.waitKey(0)

# Clean up
cv2.destroyAllWindows()

cv2.imwrite('img_edges.PNG', edges)