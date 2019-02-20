import numpy as np
from math import sqrt
from random import uniform
from PIL import Image, ImageDraw

width, height = 512, 512
counters = np.zeros((width, height))
img = Image.new('RGB', (width, height), (0, 0, 0))

iterations = 200
points = 2000000
esc_radius = 30.0
real_dim, imag_dim = 4.0, 4.0
real_ratio = width / real_dim
imag_ratio = height / imag_dim
a, b, c, d, e = -0.1, -0.2, -0.4, -0.8, -1.0

for i in xrange(points):
  z = 0
  path = []
  P = complex(uniform(-2.0, 2.0), uniform(-2.0, 2.0))

  for j in xrange(iterations):
    w = z.conjugate()
    z = a * w**5 + b * w**4 + c * w**3 + d * w**2 + e * w**1 + P
    path.extend([z.imag, z.real])

    if abs(z) > esc_radius:
      while path:
        x = int(path.pop() * real_ratio) + width / 2
        y = int(path.pop() * imag_ratio) + height / 2

        if x > 0 and y > 0 and x < width and y < height:
          counters[x][y] += 1
          counters[x][-y] += 1
      break

max_count = np.amax(counters)

for x in xrange(width):
  for y in xrange(height):
    brightness = int(255 * sqrt(counters[x][y] / max_count))
    img.putpixel((y, x), (brightness - 10,  brightness - 20, brightness - 30))

img.save("./examples/green-fractal.png")
