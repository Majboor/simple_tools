# swaps.py file from which variables to be imported
from skimage.metrics import structural_similarity
import cv2
import numpy as np
print("""
-------------------------------
welcome to Waleed's project
-------------------------------
\n\n\n""")


# Load images
def check(im1, im2):
 before = cv2.imread(im1)
 after = cv2.imread(im2)

# Convert images to grayscale
 before_gray = cv2.cvtColor(before, cv2.COLOR_BGR2GRAY)
 after_gray = cv2.cvtColor(after, cv2.COLOR_BGR2GRAY)

# Compute SSIM between the two images


 (score, diff) = structural_similarity(before_gray, after_gray, full=True)
 x = ("{:.0f}".format(score * 100)) #f = how many decimal places
#everything before { will be added to the print
 print(x)







 diff = (diff * 255).astype("uint8")
 diff_box = cv2.merge([diff, diff, diff])

# Threshold the difference image, followed by finding contours to
# obtain the regions of the two input images that differ
 thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
 contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
 contours = contours[0] if len(contours) == 2 else contours[1]

 mask = np.zeros(before.shape, dtype='uint8')
 filled_after = after.copy()

 for c in contours:
     area = cv2.contourArea(c)
     if area > 40:
         x,y,w,h = cv2.boundingRect(c)
         cv2.rectangle(before, (x, y), (x + w, y + h), (36,255,12), 2)
         cv2.rectangle(after, (x, y), (x + w, y + h), (36,255,12), 2)
         cv2.rectangle(diff_box, (x, y), (x + w, y + h), (36,255,12), 2)
         cv2.drawContours(mask, [c], 0, (255,255,255), -1)
         cv2.drawContours(filled_after, [c], 0, (0,255,0), -1)




y = 30


def swapVal(x, y):
    x, y = y, x
    return x, y