from PIL import Image
import sys  # to access the system
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
image = Image.open('right.jpg')

print("Filename: ", image.filename)
print("Format: ", image.format)
print("Mode: ", image.mode)
print("Size: ", image.size)
print("Width: ", image.width)
print("Height: ", image.height)
print("Is Animated: ", (getattr(image, "is_animated", False)))

image.close()  # close image file



plt.title("Sheep Image")
plt.xlabel("X pixel scaling")
plt.ylabel("Y pixels scaling")

image = mpimg.imread(f"./images/pets1.jpg")
plt.imshow(image)
plt.show()
prompt = str(input("is this your product?"))
if prompt == "n".casefold() or prompt == "no".casefold():
  for i in range(10):
      image = mpimg.imread(f"./images/pets{i}.jpg")
      plt.imshow(image)
      plt.show()
      prompt = str(input("was this you are looking for?"))
      if prompt == "y".casefold() or prompt == "yes".casefold():
          break