import numpy as np
import matplotlib.pyplot as plt

def make_z_plane(width=300, height=200, zoom=0.60):
	bound = round((1. / zoom), 1)
	a = np.arange(-bound, bound, 2. / width)
	b = -np.arange(-bound, bound, 2. / height)
	z_plane = np.array([np.complex(r, i) for i in b for r in a])
	z_plane = z_plane.reshape(int(height * bound), int(width * bound))
	return z_plane

def release(z_plane, model="mandelbrot", c=None, threshold=2, limit=1000):
	image = np.zeros(z_plane.shape, dtype=np.uint8)
	for [i, j], z in np.ndenumerate(z_plane):
		if model == "mandelbrot":
			c = z
		elif model == "julia":
			if c == None:
				raise ValueError("c must be given!")
			intensity = 0
			while (abs(z) < threshold) and (intensity < limit):
				z = z * z + c
				intensity += 1
			image[i, j] = intensity
		else:
			raise ValueError("Model not found!")
	return image

z_plane = make_z_plane(width=300, height=200)
img = release(z_plane, model="julia", c=-0.8 + 0.156j, threshold=2, limit=1000)
plt.imshow(img, cmap=plt.cm.cubehelix)
plt.show()
