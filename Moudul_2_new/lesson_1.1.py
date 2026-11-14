import cv2
import os



folder = os.path.dirname(os.path.abspath(__file__))

image = cv2.imread(os.path.join(folder, 'example.jpg'))


if image is None:
    print("image not found put the image")
    exit()


print("image shape:", image.shape)
cv2.imshow('my image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()