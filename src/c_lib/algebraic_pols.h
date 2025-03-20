

/**
 * @brief Estructura para manejar cada término de un polinomio, manejando su grado y su coeficiente
 * 
 */
typedef struct termino
{
    int grado_polinomio;
    double coeficiente;
    char var;
}Termino;

/**
 * @brief Representará el polinomio
 * Toma el número de términos de cada polinomio
 * EL máximo grado del polinomio
 * Un Puntero a un array de términos
 */
typedef struct polinomio
{
    int max_grado;
    int n_terminos;
    char var;
    Termino * terminos;
}Polinomio;

/**
 * @brief Funcion que inicializa un polinomio vacío en memoria
 * 
 * @return Polinomio* 
 */
Polinomio *crear_polinomio();

/**
 * @brief Es una función que analiza una cadena de carácteres
 * (Un String) y que agrega los términos a la struct Polinomio
 * 
 * @param polinomio EL * del polinomio 
 * @param term Polinomio en cadena de carácteres (array), const
 */
void tokenizar_ecuacion(Polinomio *polinomio, const char *term, int grado);

/**
 * @brief comprueba la dimension de una ecuación
 * 
 * @return int {1: Invalido, 0:una dimension}
 */
char asignar_variable();