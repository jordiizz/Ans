import numpy as np

class RungeKutta:

    def rk1(x_i, y_i, step, main_function):
        k1 = step * main_function(x_i, y_i)
        return y_i + k1
    
    def rk2(x_i, y_i, step, main_function):
        k1 = step * main_function(x_i, y_i)
        k2 = step * main_function(x_i + step, y_i + k1)
        return y_i + 0.5 * (k1 + k2)
    
    def rk3(x_i, y_i, step, main_function):
        k1 = step * main_function(x_i, y_i)
        k2 = step * main_function(x_i + step / 2, y_i + k1 / 2)
        k3 = step * main_function(x_i + step, y_i - k1 + 2 * k2)
        return y_i + (1 / 6) * (k1 + 4 * k2 + k3)

    def rk4(x_i, y_i, step, main_function):
        k1 = step * main_function(x_i,y_i) 
        k2 = step * main_function(x_i + (step / 2), y_i + (k1 / 2))
        k3 = step * main_function(x_i + (step / 2), y_i + (k2 / 2))
        k4 = step * main_function(x_i + step, y_i + k3)
        return y_i + ((k1 + (2 *k2) + (2 * k3) + k4) / 6)

    rks = {
        1:rk1,
        2:rk2,
        3:rk3,
        4:rk4
    }
     
    def calc_step(self, x_zero, x_final, n_intervals):
        return (x_final - x_zero) / n_intervals

    def runge_kutta(self, main_function, x_zero, y_zero, x_final, n_intervals,step=None, order=4):

        """_summary_
        Args:
            main_function (lambda): be defined as a lambda with x,y params
            step (float): step, amount to move foward
        """
        try:
            if step is None: step = self.calc_step(x_zero, x_final, n_intervals)
            y_i = y_zero
            x_i = x_zero
            while(x_i < x_final): #Probaremos con la condicional y con n_intervals siendo igual al numero de intervalos = numero de pasos
                y_i = self.rks[order](x_i, y_i, step, main_function)
                x_i += step
            return y_i
        except:
            print(f'Order Outta Range Max = 4, Current = {order}')