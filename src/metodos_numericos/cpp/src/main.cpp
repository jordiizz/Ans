#include <iostream>

int main(){
    int numero;

    std::cout << "Impresión número 1 en pantalla" << std::endl;
    std::cin >> numero;
    std::cout << "Desplazamiento de bits en uno " << (numero << 2) <<std::endl;
    std::cerr << "Este es un mensaje de error" << std::endl;
    return 0;
}