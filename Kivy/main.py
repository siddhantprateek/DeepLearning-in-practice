import cv2

img = cv2.imread("panda.jpeg")

print(img.shape)

panda_face = img[:400, 400:]
cv2.imshow("My Frame", panda_face)

cv2.waitKey(0)