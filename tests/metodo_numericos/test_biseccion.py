import unittest  
import time
import numpy as np
from src.Rango import Rango as Range
from src.Biseccion import Biseccion


class TestBiseccion(unittest.TestCase):
    
    def testCalc_Xr(self):
        biseccion = Biseccion()
        exp_calc_r = 9 #[6,12]
        intervalo = Range(6,12)
        calc_r = biseccion.calc_Xr(intervalo)
        self.assertEqual(calc_r, exp_calc_r)
    
    def testCalc_Ea(self):
        biseccion = Biseccion()
        v_expected = 100 / 3
        v_result = biseccion.calc_Ea(1.5, 1)
        self.assertAlmostEqual(v_expected, v_result)
        self.assertEqual(v_expected, v_result)

    def testCalc_Es(self):
        biseccion = Biseccion()
        v_expected = 0.05
        v_result = biseccion.calc_Es(3)
        self.assertEqual(v_expected, v_result)

    def testBiseccion(self):
        biseccion = Biseccion()
        intervalo = Range(0, 1)
        es = biseccion.calc_Es(3)
        start_time = time.time()
        Xr, i = biseccion.biseccion(lambda X:(np.e**(-X)) - X , intervalo, es)
        end_time = time.time()
        total_time = end_time - start_time
        print(f"Tiempo Ejecución: {total_time:.15f} segundos")
        self.assertEqual(i, 12)


if __name__ == "__main__":
    unittest.main()