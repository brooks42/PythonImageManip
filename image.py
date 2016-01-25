import Image
import sys


width = sys.argv[1]
height = sys.argv[2]
print(" width: " + str(width) + " height: " + str(height))
image = Image.new("RGB", (int(width), int(height)), "black")
image.save("image" + width + "x" + height + ".png", None)