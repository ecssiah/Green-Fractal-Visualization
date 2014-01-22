import os
import numpy as np
from math import sqrt
from random import uniform
import Image
 
#===============================================================================
# Randomly choose points in a specified complex region. Use an array to keep
# track of the path a divergent initial condition takes through the complex
# region. Finally, map that array of pixel hit counts to the screen as a grid
# of scaled color data.
#===============================================================================
 
WIDTH, HEIGHT = 1000, 1000
 
iterations = 100 #Number of series terms to sum
points = 1000000 #Number of randomly chosen test points
escapeRadius = 500.0 #"Bailout radius" for determining C diverges
 
cRealSize = 3.1 #Range of the real component of C
cImagSize = 2.6 #Range of the imag component of C
ratioReal = WIDTH / cRealSize #Ratios for transforming C to screen
ratioImag = HEIGHT / cImagSize
counters = np.zeros( ( WIDTH, HEIGHT ) ) #Array to track the paths of each C
 
img = Image.new( 'RGB', ( WIDTH, HEIGHT ), ( 0, 0, 0 ) ) #Setup new blank image
 
for i in xrange( points ):
#===========================================================================
# Look for a complex point C that is not in one of the two main Mandelbrot
# bulbs.
#===========================================================================
check = True
while check:
realPart = uniform( -2.0, 0.7 )
imagPart = uniform( -1.3, 1.3 )
q = ( realPart - 1./4. )**2 + imagPart**2
check = q * ( q + ( realPart - 1./4. ) ) < ( 1./4. * imagPart**2 )
#===========================================================================
# Iterate through the sequence and keeep track of the path through the
# complex region being mapped to the screen.
#===========================================================================
z = 0
path = []
C = complex( realPart, imagPart )
for j in xrange( iterations ):
z = z**2 + C
path.extend( [ z.imag, z.real ] )
if abs( z ) > escapeRadius:
while path:
xValue = int( path.pop() * ratioReal ) + WIDTH / 2
yValue = int( path.pop() * ratioImag ) + HEIGHT / 2
if xValue > 0 and yValue > 0 and xValue < WIDTH and yValue < HEIGHT:
counters[ xValue ][ yValue ] += 1
counters[ xValue ][ -yValue ] += 1
break
 
#===============================================================================
# Create the image by converting the hit counts into scaled color data for each
# pixel on the screen. Save image and start default image viewer from the OS.
#===============================================================================
maxCount = np.amax( counters )
for x in xrange( WIDTH ):
for y in xrange( HEIGHT ):
tmp = int( 255 * ( sqrt( counters[x][y] / maxCount ) ) )
img.putpixel( ( y, x ), ( tmp, tmp, tmp ) )
img.save( "C:/PythonWorkspace/Images/ganeshfractal.png" )
os.startfile( "C:/PythonWorkspace/Images/ganeshfractal.png" )
