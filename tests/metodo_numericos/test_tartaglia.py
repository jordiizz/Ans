import unittest
from src.Cortos.corto_uno import normalizar_ecuacion, tartaglia


class TestTartaglia(unittest.TestCase):
    
    def testNormalizar_ecuacion(self):
        a, b, c = normalizar_ecuacion(1, 2, 3, 4)
        self.assertEqual(a,2)
        self.assertEqual(b,3)
        self.assertEqual(c,4)
    
    def testTartaglia(self):
        #Se mostraán resultados Raw para confirmar, además se aproximará para que coincidadan
        #Se usará un almostEqual por la naturaleza de los métodos numéricos

        #Primer Caso: Una Raíz Triple
            #Ejemplo 1
        x_1e, x_2e, x_3e = 3, 3, 3
        x_1, x_2, x_3 = tartaglia(2, -18, 54, -54)
        print(f'Lista Result {x_1};{x_2};{x_3}')
        self.assertAlmostEqual(x_1, x_1e, delta=0.05)
        self.assertAlmostEqual(x_2, x_2e, delta=0.05)
        self.assertAlmostEqual(x_3, x_3e, delta=0.05)
            #Ejemplo 2
        x_1e, x_2e, x_3e = -4, -4, -4
        x_1, x_2, x_3 = tartaglia(1, 12, 48, 64)
        print(f'Lista Result {x_1};{x_2};{x_3}')
        self.assertAlmostEqual(x_1, x_1e, delta=0.05)
        self.assertAlmostEqual(x_2, x_2e, delta=0.05)
        self.assertAlmostEqual(x_3, x_3e, delta=0.05)

        #Segundo Caso: Una Real, Dos imaginarias
            #Ejemplo 1
        x_1e, x_2e, x_3e = 0, 2 + 1j, 2 - 1j
        x_1, x_2, x_3 = tartaglia(1, -4, 5, 0)
        print(f'Lista Result {x_1};{x_2};{x_3}')
        self.assertAlmostEqual(x_1, x_1e, delta=0.05)
        self.assertAlmostEqual(x_2, x_2e, delta=0.05)
        self.assertAlmostEqual(x_3, x_3e, delta=0.05)
            #Ejemplo 2
        x_1e, x_2e, x_3e = -1, 3j, -3j
        x_1, x_2, x_3 = tartaglia(1, 1, 9, 9)
        print(f'Lista Result {x_1};{x_2};{x_3}')
        self.assertAlmostEqual(x_1, x_1e, delta=0.05)
        self.assertAlmostEqual(x_2, x_2e, delta=0.05)
        self.assertAlmostEqual(x_3, x_3e, delta=0.05)
        
        #Tercer Caso: Tres Raíces Reales Simples
            #Ejemplo 1
        x_1e, x_2e, x_3e = 5, -4, 3
        x_1, x_2, x_3 = tartaglia(1, -4, -17, 60)
        print(f'Lista Result {x_1};{x_2};{x_3}')
        self.assertAlmostEqual(x_1, x_1e, delta=0.05)
        self.assertAlmostEqual(x_2, x_2e, delta=0.05)
        self.assertAlmostEqual(x_3, x_3e, delta=0.05)
            #Ejemplo 2
        x_1e, x_2e, x_3e = -1, -2, -1.5
        x_1, x_2, x_3 = tartaglia(-2, -9, -13, -6)
        print(f'Lista Result {x_1};{x_2};{x_3}')
        self.assertAlmostEqual(x_1, x_1e, delta=0.05)
        self.assertAlmostEqual(x_2, x_2e, delta=0.05)
        self.assertAlmostEqual(x_3, x_3e, delta=0.05)

        #Cuarto Caso: Raíz doble
            #Ejemplo 1
        x_1e, x_2e, x_3e = 1, 1, -2
        x_1, x_2, x_3 = tartaglia(1, 0, -3, 2)
        print(f'Lista Result {x_1};{x_2};{x_3}')
        self.assertAlmostEqual(x_1, x_1e, delta=0.05)
        self.assertAlmostEqual(x_2, x_2e, delta=0.05)
        self.assertAlmostEqual(x_3, x_3e, delta=0.05)
            #Ejemplo 2
        x_1e, x_2e, x_3e = 0, 0, 3
        x_1, x_2, x_3 = tartaglia(1, -3, 0, 0)
        print(f'Lista Result {x_1};{x_2};{x_3}')
        self.assertAlmostEqual(x_1, x_1e, delta=0.05)
        self.assertAlmostEqual(x_2, x_2e, delta=0.05)
        self.assertAlmostEqual(x_3, x_3e, delta=0.05)
            








  

    