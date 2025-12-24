import matplotlib.pyplot as plt
import numpy as np
import random
from scipy.integrate import quad


def f(x):
    return x**2 + 10


def is_inside(x, y):
    return y <= f(x)


def get_S_box(a, b):
    width = b - a
    height = f(b)
    return width * height


def get_area(inside_points, points, S_box):
    M = len(inside_points)
    N = len(points)
    return (M / N) * S_box


def monte_carlo_simulation(a, b, num_experiments):
    average_area = 0
    S_bpx = get_S_box(a, b)

    for _ in range(num_experiments):
        points = [(random.uniform(a, b), random.uniform(0, f(b))) for _ in range(15000)]

        inside_points = [point for point in points if is_inside(point[0], point[1])]
        area = get_area(inside_points, points, S_bpx)
        average_area += area

    result = average_area / num_experiments
    return result


def main():
    a = 0
    b = 2
    num_experiments = 1000

    mc_result = monte_carlo_simulation(a, b, num_experiments)
    quad_result, quad_error = quad(f, a, b)
    abs_error = abs(mc_result - quad_result)
    rel_error = abs_error / quad_result * 100

    print(f"Definite integral ∫ f(x) dx on the interval [{a}, {b}]")
    print("-" * 60)
    print(f"Monte Carlo method: {mc_result:.6f}")
    print(f"SciPy quad result:  {quad_result:.6f}")
    print(f"quad error estimate: {quad_error:.2e}")
    print("-" * 60)
    print(f"Absolute error: {abs_error:.6f}")
    print(f"Relative error: {rel_error:.4f} %")


if __name__ == "__main__":
    main()
