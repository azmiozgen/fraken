import numpy as np
import matplotlib.pyplot as plt

def recur_Julia(z_plane, c, threshold=2, limit=1000):
	image = np.zeros(z_plane.shape)
	for [i, j], z in np.ndenumerate(z_plane):
		intensity = 0
		while (abs(z) < threshold) and (intensity < limit):
			z = z * z + c
			intensity += 1
		image[i, j] = intensity
	return image

width = 500
heigth = 500
a = np.arange(-1, 1, 2. / width)
b = -np.arange(-1, 1, 2. / heigth)
z_plane = np.array([np.complex(r, i) for i in b for r in a])
z_plane = z_plane.reshape(width, heigth)

img = recur_Julia(z_plane, c=-0.8 + 0.156j, threshold=2)
#img = img * 255 / img.max()
fig = plt.figure()
fig.add_subplot(1, 2, 1)
plt.imshow(img, cmap=plt.cm.Greys_r)
fig.add_subplot(1, 2, 2)
plt.imshow(img)
plt.show()
