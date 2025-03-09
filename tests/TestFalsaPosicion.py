import unittest
import numpy as np
from src.FalsaPosicion import Rango as Rango
from src.FalsaPosicion import FalsaPosicion as ReglaFalsa


class TestFalsaPosicion(unittest.TestCase):

    def testRango(self):
        pass

    def testCalc_Xr(self):
        regla_falsa = ReglaFalsa()
        es = regla_falsa.calc_Es(3)
        self.assertEqual(0.05, es)
        rango = Rango(0,1)
        X_esperado, i_esperado = 0.383539686, 9
        X_result, I_result = regla_falsa.calc_false_position((lambda x:np.e**(-5*x) - x**2),rango,es)
        print(f"Resultado de Xr : {X_result} and Expexted: {X_esperado}")
        self.assertEqual(i_esperado,I_result)
        X_result =float( "{:.9f}".format(X_result))
        self.assertEqual(X_esperado,X_result)

