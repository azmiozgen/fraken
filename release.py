#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import argparse
from time import time

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--model", type=str, default='mandelbrot', help="Model name. 'mandelbrot' or 'julia'. default='mandelbrot'")
parser.add_argument("-c", "--constant", type=float, default=None, nargs='*', help="Constant 'c' for julia set. default=None")
parser.add_argument("-t", "--threshold", type=int, default=2, help="Threshold value for escaping. default=2")
parser.add_argument("-l", "--limit", type=int, default=1000, help="Limit iteration value. default=1000")
parser.add_argument("-s", "--shape", type=int, default=[300, 200], nargs='*', help="Image shape. e.g. -s 300 200. default=300 200")
parser.add_argument("-z", "--zoom", type=float, default=0.65, help="Zoom ratio. e.g. -z 0.65. default=0.65")
parser.add_argument("-r", "--color", type=str, default='hot', help="Coloring map. default='hot'")
parser.add_argument("-v", "--no_show", action='store_true', default=False, help="Do not show image")
parser.add_argument("-o", "--output", type=str, help="Save image on given path")
parser.add_argument("-i", "--exec_time", action='store_true', help="Show execution time")
args = vars(parser.parse_args())
model = args["model"]
if args["constant"] != None:
	constant = complex(args["constant"][0], args["constant"][1])
else:
	constant = None
threshold = args["threshold"]
limit = args["limit"]
shape = args["shape"]
zoom = args["zoom"]
color = args["color"]
no_show = args["no_show"]
output = args["output"]
exec_time = args["exec_time"]

def make_z_plane(width=300, height=200, zoom=0.60):
	bound = round((1. / zoom), 1)
	a = np.arange(-bound, bound, 2. * bound / width)
	b = -np.arange(-bound, bound, 2. * bound / height)
	z_plane = np.array([np.complex(r, i) for i in b for r in a])
	z_plane = z_plane.reshape(height, width)
	return z_plane

def release(z_plane, model="mandelbrot", c=None, threshold=2, limit=1000):
	image = np.zeros(z_plane.shape, dtype=np.uint8)
	for [i, j], z in np.ndenumerate(z_plane):
		if model == "mandelbrot":
			c = z
		elif model == "julia":
			if c == None:
				raise ValueError("c must be given!")
		else:
			raise ValueError("Model not found!")
		intensity = 0
		while (abs(z) < threshold) and (intensity < limit):
			z = z * z + c
			intensity += 1
		image[i, j] = intensity
	return image

if __name__ == "__main__":
	t0 = time()
	z_plane = make_z_plane(width=shape[0], height=shape[1], zoom=zoom)
	img = release(z_plane, model=model, c=constant, threshold=threshold, limit=limit)
	if exec_time:
		print time() - t0, "seconds"
	plt.imshow(img, cmap=color)
	plt.xticks([])
	plt.yticks([])
	if output:
		plt.savefig(output, bbox_inches='tight', pad_inches=0)
	if not no_show:
		plt.show()
