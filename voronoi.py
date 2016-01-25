
import math;
import Image;
import random;
import time;

def manhattanpt(xy1, xy2):
	return manhattan(xy1[0], xy1[1], xy2[0], xy2[1])

def manhattan(a1, a2, b1, b2):
	#|x-y|+|x2-y2|
	return (abs(a1 - b1) + abs(a2 - b2))


def euclideanpt(xy1, xy2):
	return euclidean(xy1[0], xy1[1], xy2[0], xy2[1])

def euclidean(x1, y1, x2, y2):
	return math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))

def voronoi_plot_man(width, height, num_points):
	return voronoi_plot(width, height, num_points, "manhattan")

def voronoi_plot_euc(width, height, num_points):
	return voronoi_plot(width, height, num_points, "euclidean")

# does a voronoi plot with the passed distance algorithm
def voronoi_plot(width, height, num_points, algo):
	totalTime = time.time()
	totalPixels = (width * height)

	# calculates and saves an image file containing a voronoi plot of size (x, y) with num_points number of points.
	# returns the number of pixels it calculated for printing out purposes
	points = []
	for point in range(0, num_points):
		points.append((random.randint(0, width), random.randint(0, height)));

	image = Image.new("RGB", (width, height))

	# we'll generate some nice random colors real quick for the points...
	colors = {}
	for point in points:
		# generate a random color and add it to our list
		colors[point] = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))

	calcPoints = 0;
	# now in here we make it actually do pixels...
	# first we'll draw the proper color for each point. 
	for wx in range(0, width):
		for wy in range(0, height):
			# get the manhattan distance to each of our points and use that to determine the color of this pixel...
			closest = points[0]
			nearest = manhattanpt((wx, wy), closest)
			for point in points: 
				if algo == "manhattan":
					if manhattanpt((wx, wy), point) < nearest:
						closest = point
						nearest = manhattanpt((wx, wy), point)
				elif algo == "euclidean":
					if euclideanpt((wx, wy), point) < nearest:
						closest = point
						nearest = euclideanpt((wx, wy), point)
				
			calcPoints += 1
			if calcPoints % 100 == 0:
				print "progress (" + str(calcPoints) + "/" + str(totalPixels) + ")..."
			if totalPixels == calcPoints:
				print "Done!"

			# now draw the pixel based on the color of its closest point
			image.putpixel((wx, wy), colors[closest])

	for point in points:
		# for the 9 pixels in and around the selected point(s), we'll print it dark gray for visibility
		for px in range(max(0, point[0]) + 1, min(width, point[0] + 1) - 1):
			for py in range(max(0, point[1]) + 1, min(height, point[1] + 1) - 1):
				image.putpixel((px, py), (128, 128, 128))

	image.save("voronoi" + str(time.time()) + "(" + str(width) + "x" + str(height) + ")" + algo + ".bmp", None)

	print "Time: " + str(time.time() - totalTime)
	
	return points



print str(manhattan(1, 1, 2, 2)) + " " + str(manhattanpt((1, 1), (2, 2)))
print str(manhattan(-1, 1, -2, 2)) + " " + str(manhattanpt((-1, 1), (-2, 2)))
print str(manhattan(1, 4, 2, 4)) + " " + str(manhattanpt((1, 4), (2, 4)))

print voronoi_plot_man(500, 500, 50)
print voronoi_plot_euc(500, 500, 50)
print voronoi_plot_man(1000, 1000, 100)
print voronoi_plot_euc(1000, 1000, 100)
print voronoi_plot_man(5000, 5000, 500)
print voronoi_plot_euc(5000, 5000, 500)