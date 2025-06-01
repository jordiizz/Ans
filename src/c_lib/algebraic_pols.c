#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include "algebraic_pols.h"

/**
 * @brief Es un archivo orientado a la 
 * manipulación de funciones en formato String
 * Proporciona herramientas para derivar, simplificar, reducir
 * Formar polinomios y expresiones algebraicas
 */

Polinomio *crear_polinomio(){
    Polinomio *polinomio = (Polinomio*)malloc(sizeof(Polinomio));
    if(polinomio){
        polinomio -> n_terminos = 0;
        polinomio ->max_grado = 0;
        polinomio -> terminos = NULL;
        return polinomio;
    }
    return NULL;   
}

Termino *crear_termino(double coef, char var, double grado){
    if (((coef && grado) > 0) && (var != '\0')){
        Termino *termino = (Termino*) malloc(sizeof(Termino));
        
        return termino;
    }
    return NULL;
}

char asignar_variable(const char *ecuacion){
    char var = '\0';
    if (ecuacion) {
        int len_ecuacion = strlen(ecuacion);
        for (int i = 0; i < len_ecuacion; i++){
            if(isalpha(ecuacion[i])){
                if(var != '\0'){
                    fprintf(stderr, "ecuation is not unidimensional");
                    exit(EXIT_FAILURE);
                }
                var = ecuacion[i];
                return var;           
            }
        }
    }
    return '\0';
}

//En un inicio no se validará
void tokenizar_ecuacion(Polinomio *polinomio, const char *ecuacion){
    int grado = 0;
    double coeficiente = 0.0;
    char variable = asignar_variable(ecuacion);
    int len_ecuacion = strlen(ecuacion);
    /*Recorre la cadena de carácteres que es la ecuación
     * En este bloque encontraremos qué caracter usamos como variable x,y,z
     * En esta parte se verificará que la encuación sea de una variable
     * Es una Función a normalizar
    */
  
    //Acá partiremos la ecuación, que es tokenizar
    //x⁴ + 3x² - 54x⁶
    for (int i = 0; i < len_ecuacion ; i++ ){

        if(ecuacion[i] == variable){
            
        }
    }

    if(variable != '\0'){
        if(srtchr(ecuacion, '^') != NULL){
            
        }
    }

}