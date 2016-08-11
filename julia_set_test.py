from cmath import exp
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

x_size = 200
y_size = 200
image = []

def abs(z):
	return sqrt(z.real**2 + z.imag**2)

def f(z):
	return z**2 - 0.8 + 0.156j

for x in xrange(-x_size/2, x_size/2):
	print x
	row = []
	for y in xrange(-y_size/2, y_size/2):
		z = complex(x / (x_size / 2.), y / (y_size / 2.))

		intensity = 0
		while (abs(z) < 2) and (intensity < 1000):
			z = f(z)
			intensity += 1
		row.append(intensity)

	image.append(row)

image = np.array(image).transpose()
image = image * 255 / image.max()

fig = plt.figure()
fig.add_subplot(1, 2, 1)
plt.imshow(image, cmap=plt.cm.Greys_r)
fig.add_subplot(1, 2, 2)
plt.imshow(image)
plt.show()
