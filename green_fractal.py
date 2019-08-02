"""Generates a Green Fractal"""
from random import uniform
from math import sqrt
from PIL import Image
import numpy as np

OUTPUT_NUMBER = 7
WIDTH, HEIGHT = 1024, 1024
ITERATIONS = 200
POINTS = 10_000_000
ESCAPE_RADIUS = 3.0
REAL_RANGE, IMAG_RANGE = 4.0, 4.0
REAL_RATIO, IMAG_RATIO = WIDTH / REAL_RANGE, HEIGHT / IMAG_RANGE

def generate_heat_map(counters):
    """Produces the heat map by iterating the generator function"""
    a, b, c, d, e = 0.2, 0.2, 0.4, -0.2, -0.2

    for _ in range(POINTS):
        z = 0
        path = []
        origin = complex(uniform(-2.0, 2.0), uniform(-2.0, 2.0))

        for _ in range(ITERATIONS):
            w = z.conjugate()
            z = a * w**5 + b * w**4 + c * w**3 + d * w**2 + e * w**1 + origin
            path.extend([z.imag, z.real])

            if abs(z) > ESCAPE_RADIUS:
                while path:
                    x = int(path.pop() * REAL_RATIO) + WIDTH // 2
                    y = int(path.pop() * IMAG_RATIO) + HEIGHT // 2

                    if 0 < x < WIDTH and 0 < y < HEIGHT:
                        counters[x][y] += 1
                        counters[x][-y] += 1
                break

def main():
    """Main entry point to application"""
    counters = np.zeros((WIDTH, HEIGHT))
    img = Image.new('RGB', (WIDTH, HEIGHT), (0, 0, 0))

    generate_heat_map(counters)
    max_count = np.amax(counters)

    for x in range(WIDTH):
        for y in range(HEIGHT):
            brightness = int(255 * sqrt(counters[x][y] / max_count))
            img.putpixel((y, x), (brightness, brightness, brightness))

    img.save("./examples/green_fractal" + str(OUTPUT_NUMBER) + ".png")

if __name__ == "__main__":
    main()
