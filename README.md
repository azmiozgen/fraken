# Fractal Generation Project

A fractal generation tool to create beautiful, artistic pictures.

## Why the name *Fraken* ?

Fraken = Fractal + Kraken

*Release the Krakeeen!*

## Usage (python)

You can see all options by:

`./release.py -h`

Generating default Mandelbrot fractal:

`./release.py`

Generating Julia fractal with *c=-0.8j*. Real and imaginary parts are given separately. '-o' saves image with given file name. '-v' is used not to display image.

`./release.py -m julia -c 0 -0.8 -o julia_fractal.png -v`

Image shape can be arranged with -s option (width x height). e.g.

`./release.py -m julia -c 0 -0.8 -s 1000 800 -o julia_fractal.png`

Zoom in/out option is -z, threshold -t, iteration limit -l and coloring map -r. e.g.

`./release.py -m julia -c 0 -0.8 -t 2 -l 1000 -s 800 700 -z 0.7 -r hot -o julia_fractal.png`

## Usage (c++)

c++ version significantly faster for larger sized images (1000x800 e.g.)

Execution time can be seen with '-i' option.

All options are the same with python version.

An execution example:

`./release -m julia -c 0 -0.8 -t 2 -l 1000 -s 800 700 -z 0.7 -r hot -o julia_fractal.png`

Result:

![julia fractal](julia_fractal.png)

### **TODO**
- Design fractal animations
- Add Theano version fractal generation
- Add GPU supported fractal generation
- Design a user-interface
- Research another fractal generation methods and apply them
