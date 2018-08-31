import time as t
import numpy as np

inefficient_poly = lambda x: x**4 - 3*x**3 + 7*x**2 + x - 5
efficient_poly = lambda x: x*(1 + x*(7 + x*(-3 + x))) - 5

def benchmark(it, poly, name):
    start = t.perf_counter()
    for x in it:
        poly(x)
    end = t.perf_counter()

    print('Elapsed Time for', name, '\t', end - start)


xs = np.random.randn(10000000)
benchmark(xs, efficient_poly, 'efficient poly')
benchmark(xs, inefficient_poly, 'Inefficient poly')

input('')