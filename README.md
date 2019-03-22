# Green Fractal Generator

This python script generates fractals using a variation of the Buddhabrot method discovered by Melinda Green. Melinda’s technique samples points in the complex plane, and then repeatedly applies the Mandelbrot equation to these points to see if they eventually land outside of an escape radius after a certain number of iterations.

An array of counters is used to track every point that is hit before a sample point escapes. The size of this array is chosen so that it will map directly to the pixels in the image that is being produced. Every time a point lands within the small area associated with a particular pixel it is incremented by one.

After a large number of points have been tested, this array of counters is used as a heat map to produce the image. Each count is divided by the largest value in the counters array, so that the points hit most often are set to 1. These will be the brightest pixels in the image. All other pixels will have a brightness somewhere between 0 and 1.

Here is Melinda’s own page describing her process and displaying a number of examples: [Superliminal: Buddhabrot](http://superliminal.com/fractals/bbrot/bbrot.htm)

My implementation allows for a wide variety of generating functions, rather than just the traditional Mandelbrot generator. Each term also has a coefficient applied to it, and at each step in the process the previous value is conjugated before applying the equation again. This significantly changes the character of the images produced.

Here is an example of a generating function:

```javascript
Complex z, w = 0;
Complex C = random();

for i in iterations:
  w = z.conjugate();
  z = p * w^3 + q * w^2 + r * w + C
```

`C` is the sample point for each test, which is chosen at random from points within the desired complex range.

This produces a generalized fractal based on the method developed by Green. I have called the range of fractals generated using this expanded method: Green Fractals.