import cv2




image = cv2.imread('example.jpg')





gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)





resized_image = cv2.resize(gray_image, (400, 400))





cv2.imshow('my image', resized_image)





key = cv2.waitKey(0)





if key == ord('s'):
    cv2.imwrite('gray_image.jpg', resized_image)
    print("image saved as gray_image.jpg")
else:
    print("image not saved")

cv2.destroyAllWindows()
print("processed image dimension:", resized_image.shape)