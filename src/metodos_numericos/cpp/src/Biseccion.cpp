#ifndef BISECCION_H
#define BISECCION_H

#include "Rango.h"
#include <iostream>
#define BISECCION_H

#include "Rango.h"
#include <iostream>
#include <cmath>
#include <functional>

class Biseccion {

    double calc_Xr(Rango& rango) {
        return (rango.X1 + rango.Xu) / 2.0 ;
    }

    double calc_f(std::function<double(double)> funcion, double x){
        return funcion(x);
    }

    double calc_Es(int n){
        return std::abs(0.5 * pow(10, 2 - n));
    }

    double calc_Ea(double Xr,double XrA){
        return std::abs(((Xr - XrA) * (100))/(Xr));
    }

    double biseccion(std::function<double(double)> funcion, Rango rango, double Es, double XrA = 0,int contador = 1){
        double Xr = calc_Xr(rango);
        double mult_funciones = funcion(rango.X1) * funcion(Xr);

        if(contador != 1){
            double Ea = calc_Ea(Xr, XrA);
            if(Ea <= Es){
                return contador;
            }
        }
        
        if(mult_funciones < 0){
            rango.Xu = Xr;
        }else if (mult_funciones > 0){
            rango.X1 = Xr;
        }
        return biseccion(funcion, rango, Es, Xr, contador + 1);
        
    }
};

#endif