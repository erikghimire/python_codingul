
import cv2
import matplotlib.pyplot as plt

image = cv2.imread('exsample.jpg')


image_rgb = cv2.cvtcolor(image , cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.title('RGB Image')
plt.show()


gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_image, cmap='gray')
plt.title('Gray Image')
plt.show()


crooped_image = image[100:400, 100:400]
plt.imshow(cv2.cvtColor(crooped_image, cv2.COLOR_BGR2RGB))
plt.title('Cropped Image')
plt.show()