#Image Annotation with Shapes and Measurements

import cv2

image = cv2.imread('example.jpg')

h, w = image.shape[:2] # Image height and width

# Two rectangles: top-left (yellow) and bottom-right (magenta)

cv2.rectangle(image, (20, 20), (170, 170), (0, 255, 255), 3)

cv2.rectangle(image, (w-220, h-170), (w-20, h-20), (255, 0, 255), 3)

# Green dots at both centres, joined by a green line

c1, c2 = (95, 95), (w-120, h-95)

cv2.circle(image, c1, 15, (0, 255, 0), -1)

cv2.circle(image, c2, 15, (0, 255, 0), -1)

cv2.line(image, c1, c2, (0, 255, 0), 3)

# Labels

font = cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(image, 'Region 1', (20, 15), font, 0.7, (255, 255, 255), 2)

cv2.putText(image, 'Region 2', (w-220, h-180), font, 0.7, (255, 255, 255), 2)

# Two-way arrow on the right showing the height

cv2.arrowedLine(image, (w-50, 20), (w-50, h-20), (255, 255, 0), 3, tipLength=0.05)

cv2.arrowedLine(image, (w-50, h-20), (w-50, 20), (255, 255, 0), 3, tipLength=0.05)

cv2.putText(image, f'Height: {h}px', (w-200, h//2), font, 0.8, (255, 255, 0), 2)

cv2.imshow('Annotated Image', image)

cv2.waitKey(0)