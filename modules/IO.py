import pyautogui
import bezier
import numpy as np
import pyautogui
import random
import scipy
import time
from scipy import interpolate
import matplotlib.pyplot as plt
class IO:

    def moveTo(self):
        pyautogui.MINIMUM_DURATION = 0
        pyautogui.MINIMUM_SLEEP = 0
        pyautogui.PAUSE = 0

        # We'll wait 5 seconds to prepare the starting position
        start_delay = 0
        pyautogui.sleep(start_delay)

        # For this example we'll use four control points, including start and end coordinates
        start = pyautogui.position()
        end = start[0] + 600, start[1] + 200
        # Two intermediate control points that may be adjusted to modify the curve.
        control1 = [start[0] + 125, start[1] + 100]
        control2 = [start[0] + 375, start[1] + 50]

        # Format points to use with bezier
        control_points = np.array([start, control1, control2, end])
        points = np.array([control_points[:, 0], control_points[:, 1]])  # Split x and y coordinates
        nodes = np.asfortranarray([
            [100.0, 300.0, 600.0],
            [100.0, 300.0, 600.0],
        ])
        # You can set the degree of the curve here, should be less than # of control points
        degree = 3
        # Create the bezier curve
        curve = bezier.Curve(nodes, degree)
        # You can also create it with using Curve.from_nodes(), which sets degree to len(control_points)-1
        # curve = bezier.Curve.from_nodes(points)

        curve_steps = 50  # How many points the curve should be split into. Each is a separate pyautogui.moveTo() execution
        delay = 1 / curve_steps  # Time between movements. 1/curve_steps = 1 second for entire curve
        print(curve.evaluate(0.75))
        # Move the mouse
        pyautogui.mouseDown()
        for i in range(1, curve_steps + 1):
            # The evaluate method takes a float from [0.0, 1.0] and returns the coordinates at that point in the curve
            # Another way of thinking about it is that i/steps gets the coordinates at (100*i/steps) percent into the curve
            print(curve.evaluate(i / curve_steps))
            x, y = curve.evaluate(i / curve_steps)
            pyautogui.moveTo(x, y)  # Move to point in curve
            pyautogui.sleep(delay)  # Wait delay
        pyautogui.mouseUp()

    def test(self):
        x = np.random.random_sample((3,))
        y = np.random.random_sample((3,))

        cells = 10

        qwe = np.size(x, 0)
        n = qwe - 1
        i = 0
        t = np.linspace(0, 1, cells)
        b = []

        xBezier = np.zeros((1, cells))
        yBezier = np.zeros((1, cells))

        def Ni(n, i):
            return np.math.factorial(n) / (np.math.factorial(i) * np.math.factorial(n - i))

        def basisFunction(n, i , t):
              J = np.array(Ni(n, i) * (t ** i) * (1 - t) ** (n - i))
              return J

        for k in range(0, qwe):
            b.append(basisFunction(n, i, t))
            xBezier = basisFunction(n, i, t) * x[k] + xBezier
            yBezier = basisFunction(n, i, t) * y[k] + yBezier
            i += 1

