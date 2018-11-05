from skimage.morphology import skeletonize
from skimage import img_as_bool
import numpy
import imutils
import cv2

filename = "expt3.jpg"
# filename = "black1.jpg"
image = cv2.imread(filename)

# todo: increase contrast on image

resized = imutils.resize(image, width=300)
ratio = image.shape[0] / float(resized.shape[0])
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
b = 5
blurred = cv2.GaussianBlur(gray, (b,b), 0)
thresh = cv2.threshold(gray, 127, 225, cv2.THRESH_BINARY)[1]
cv2.imshow("thresh", thresh)
cv2.waitKey(0)
print thresh[100]

# prob omit the following
'''
thresh = cv2.bitwise_not(thresh)
cv2.imshow("thresh", thresh)
cv2.waitKey(0)
print thresh[100]

binary = img_as_bool(thresh)
print thresh[100]
skeleton = skeletonize(binary)
skeleton = numpy.where(skeleton == 1, 225, 0)
print skeleton[100]
cv2.imshow("skeleton", skeleton)
cv2.waitKey(0)
'''

contours = cv2.findContours(thresh.copy(), cv2.RETR_LIST,
  cv2.CHAIN_APPROX_SIMPLE)
print(contours[0])

for c in contours:
  print("contour: ", len(c), len(c[0]))

for c in contours[1]:
  print "countour size = ", len(c)
  if len(c) < 50: continue

  (x,y), radius = cv2.minEnclosingCircle(c)
  center = (int(x * ratio), int(y * ratio))
  radius = int(radius * ratio)

  ctr = numpy.array(c).reshape((-1,1,2)).astype(numpy.int32)
  M = cv2.moments(ctr)
  cX = int((M["m10"] / M["m00"]) * ratio)
  cY = int((M["m01"] / M["m00"]) * ratio)
  print "center = (", cX, cY, ")"
  ctr = ctr.astype(numpy.float32)
  ctr *= ratio
  ctr = ctr.astype(numpy.int32)
  cv2.drawContours(image, [ctr], -1, (0, 255, 0), 2)
  cv2.circle(image, center, radius, (0, 255, 0), 2)
  cv2.imshow("Image", image)
  cv2.waitKey(0)
cv2.destroyAllWindows()

'''
c = contours[1][4]
print(len(c))
ctr = numpy.array(c).reshape((-1,1,2)).astype(numpy.int32)
M = cv2.moments(ctr)
#cX = int((M["m10"] / M["m00"]) * ratio)
#cY = int((M["m01"] / M["m00"]) * ratio)
ctr = ctr.astype(numpy.float32)
ctr *= ratio
ctr = ctr.astype(numpy.int32)
cv2.drawContours(image, [ctr], -1, (0, 255, 0), 2)
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''


