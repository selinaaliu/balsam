import numpy
import imutils
import cv2


# filename = "circle3.jpg"
filename = "expt1.jpg"

image = cv2.imread(filename)

# todo: increase contrast on image

resized = imutils.resize(image, width=300)
ratio = image.shape[0] / float(resized.shape[0])

gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
b = 9
blurred = cv2.GaussianBlur(gray, (b,b), 0)
thresh = cv2.threshold(gray, 127, 225, cv2.THRESH_BINARY)[1]
thresh = cv2.bitwise_not(thresh)

cv2.imshow("thresh", thresh)
cv2.waitKey(0)

circles = cv2.HoughCircles(
  thresh.copy(),
  cv2.HOUGH_GRADIENT,
  3,
  1,
  param1=100,
  param2=100,
  minRadius=5,
  maxRadius=50)

print circles
if circles is not None:
  circles = numpy.round(circles[0,:]).astype("int")
  for (x,y,r) in circles:
    print (x,y,r)
    cv2.circle(resized, (x, y), r, (0, 255, 0), 4)
		# cv2.rectangle(resized, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

  cv2.imshow("image", resized)
  cv2.waitKey(0)
else: print 'no circles found'
