import numpy as np
import os, subprocess, time
import Image, ImageFont, ImageDraw
from math import sqrt
from random import uniform

count = 30
filename = "/home/kabbotta/workspace/Python/Projects/pathfractal/images/pathfractal_%s.png" % count
 
iterations = 2000
points = 2000000
esc_radius = 60.0

a, b, c, d, e = -0.1, -0.2, -0.4, -0.8, -1.0
real_dim, imag_dim = 4.0, 4.0

width, height = 1000, 1000
real_ratio = width / real_dim
imag_ratio = height / imag_dim
counters = np.zeros((width, height))
img = Image.new('RGB', (width, height), (0, 0, 0))

# Start Timer
start_time = time.time()
 
for i in xrange(points):
  z = 0
  path = []
  C = complex(uniform(-2.0, 2.0), uniform(-2.0, 2.0))

  for j in xrange(iterations):
    w = z.conjugate()
    z = a*w**5 + b*w**4 + c*w**3 + d*w**2 + e*w**1 + C
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
    img.putpixel((y, x), (brightness - 20,  brightness - 20, brightness - 10))

# Stop Timer
elapsed = (time.time() - start_time) / 60

# Draw Debug Info
font_size = 12
font_color = 255, 255, 255
font = ImageFont.truetype("/usr/share/fonts/truetype/droid/DroidSerif-Regular.ttf", font_size)

draw = ImageDraw.Draw(img)
draw.text((0, 0*(font_size + 2)), 
  "a b c d e = %.1f %.1f %.1f %.1f %.1f" % (a, b, c, d, e), 
  font_color, font=font)
draw.text((0, 1*(font_size + 2)), "iter: %i" % iterations, font_color, font=font)
draw.text((0, 2*(font_size + 2)), "points: %i" % points, font_color, font=font)
draw.text((0, 3*(font_size + 2)), "radius: %.1f" % esc_radius, font_color, font=font)
draw.text((0, 4*(font_size + 2)), "time: %.1f" % elapsed, font_color, font=font)

img.save(filename)
