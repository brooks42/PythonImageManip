
import math;
import Image;
import random;
import time;

sobelX = [ [ -1, 0, 1 ], [ -2, 0, 2 ], [ -1, 0, 1 ] ]

sobelY = [ [ 1, 2, 1 ], [ 0, 0, 0 ], [ -1, -2, -1 ] ]

def applyXFilter(image, pixelx, pixely):
	sumX = 0

	it = [ -1, 0, 1 ]
	for i in it:
		for j in it:
			if pixelx + i > 0 and pixelx + i < image.size[0] and pixely + j > 0 and pixely + j < image.size[1]:
				color = image.getpixel((pixelx + i, pixely + j))
				#print("\t(" + str(pixelx + i) + ", " + str(pixely + j) + ")->" + str(color))

				#for now this should filter by the red in the image, just to see how it works...
				sumX = sumX + (int(color[0]) * sobelX[i+1][j+1])
	#print("sumX: " + str(sumX))
	return sumX

def applyYFilter(image, pixelx, pixely):
	sumY = 0

	it = [ -1, 0, 1 ]
	for i in it:
		for j in it:
			if pixelx + i > 0 and pixelx + i < image.size[0] and pixely + j > 0 and pixely + j < image.size[1]:
				color = image.getpixel((pixelx + i, pixely + j))
				#print("\t(" + str(pixelx + i) + ", " + str(pixely + j) + ")->" + str(color))

				#for now this should filter by the red in the image, just to see how it works...
				sumY = sumY + (int(color[0]) * sobelY[i+1][j+1])
	return sumY

def sobelGradient(gx, gy):
	#return math.sqrt(pow(gx, 2) + pow(gy, 2))
	return abs(gx) + abs(gy)

def apply_sobel_filter(image, step):
	totalTime = time.time()
	
	totalgrad = 0
	pixels = 0

	#image sizes are tuples :(
	width = image.size[0];
	height = image.size[1];

	#create our filtered image
	filteredImage = Image.new("RGB", (width, height))

	# here we'll apply the sobel filter to each pixel and write the resulting
	# pixel to the filtered image
	for wx in range(0, width, step):
		for wy in range(0, height, step):
			grad = sobelGradient(wx, wy)
			totalgrad = totalgrad + grad
			pixels = pixels + 1
			sobelColor = sobelGradient(applyXFilter(image, wx, wy), applyYFilter(image, wx, wy))
			if sobelColor > 255:
				sobelColor = 255
			filteredImage.putpixel((wx, wy), (int(sobelColor), int(sobelColor), int(sobelColor)))

			# now draw the pixel based on the color of its closest point
			#image.putpixel((wx, wy), colors[closest])
	filteredImage.save("sobel_test" + str(time.time()) + "(" + str(width) + "x" + str(height) + ").bmp", None)
	print("Time: " + str(time.time() - totalTime))
	print("Average gradient: " + str(totalgrad) + " over " + str(pixels) + " pixels = " + str(totalgrad / pixels))


def main():
	#apply_sobel_filter(Image.open("filter_test(500x500).bmp"), 1);
	#apply_sobel_filter(Image.open("filter_test(500x500).bmp"), 2);
	#apply_sobel_filter(Image.open("filter_test(500x500).bmp"), 3);
	#apply_sobel_filter(Image.open("filter_test(500x500).bmp"), 5);
	#apply_sobel_filter(Image.open("filter_test(500x500).bmp"), 10);
	apply_sobel_filter(Image.open("cowboybebop.png"), 5);
	apply_sobel_filter(Image.open("cowboybebop.png"), 10);
	print("Done.")

if __name__ == "__main__":
	main();