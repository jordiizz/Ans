import unittest
from src.metodos_numericos.python.runge_kutta import RungeKutta

class TestRungeKutta(unittest.TestCase):

    def testRk1(self):
        rk = RungeKutta()
        x0, y0, Xn, n = 0, 1, 1, 2
        func = lambda x,y: x+y
        y_expected, y_result = 2.5, rk.runge_kutta(main_function=func, x_zero=x0, y_zero=y0, x_final=Xn, n_intervals=n, order=1)
        self.assertAlmostEqual(y_expected, y_result, delta=0.05)
        print(y_expected)

    def testRk2(self):
        rk = RungeKutta()
        x0, y0, Xn, n = 0, 1, 1, 2
        func = lambda x,y: x+y
        y_expected, y_result = 3.28, rk.runge_kutta(main_function=func, x_zero=x0, y_zero=y0, x_final=Xn, n_intervals=n, order=2)
        self.assertAlmostEqual(y_expected, y_result, delta=0.05)
        print(y_expected)

    def testRk3(self):
        rk = RungeKutta()
        x0, y0, Xn, n = 0, 1, 1, 2
        func = lambda x,y: x+y
        y_expected, y_result = 3.4347, rk.runge_kutta(main_function=func, x_zero=x0, y_zero=y0, x_final=Xn, n_intervals=n, order=3)
        self.assertAlmostEqual(y_expected, y_result, delta=0.05)
        print(y_expected)

    def testRk4(self):
        rk = RungeKutta()
        x0, y0, Xn, n = 0, 1, 1, 2
        func = lambda x,y: x+y
        y_expected, y_result = 3.4347, rk.runge_kutta(main_function=func, x_zero=x0, y_zero=y0, x_final=Xn, n_intervals=n, order=4)
        self.assertAlmostEqual(y_expected, y_result, delta=0.05)
        print(y_expected)
        