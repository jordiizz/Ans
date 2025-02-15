import unittest 
import sys 
sys.path.append('../src')
from AnsError import AnsError
from Rango import Range

class TestAnsError(unittest.TestCase):
    def test_calc_r(self):
        exp_calc_r = 9 #[6,12]
        ans_error = AnsError()
        intervalo = Range(6,12)

        calc_r = ans_error.calc_Xr(intervalo)
        self.assertEqual(calc_r, exp_calc_r)
    
    def test_valor_cercano(self):
        pass        

    
if __name__ == "__main__":
    unittest.main()