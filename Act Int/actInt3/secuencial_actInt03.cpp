//
//  Joanna Nicole Uriostegui Magaña - A01711853
//  *Actividad Integradora 3*
//
//  Secuencial 
//  Tiempo: 1078.425 ms
//
#include <iostream>
#include <iomanip>
#include <chrono>
#include "utils.h"

using namespace std;
using namespace std::chrono;

const int SIZE = 5000000;

bool es_primo(int n){
    if(n < 2){
        return false;
    }

    double n2 = sqrt(n);
    for(int i = 2; i <= n2; i++){
        if(n % i == 0){
            return false;
        }
    }
    return true;
}

long long sumar_primos(int size) {
    long long suma = 0;
    for (int i = 0; i < size; i++) {
        if(es_primo(i)){
            suma+= i;
        }
    }
    return suma;
}

int main(int argc, char* argv[]) {

    // These variables are used to keep track of the execution time.
    high_resolution_clock::time_point start, end;
    double timeElapsed;

    cout << "Starting...\n";
    timeElapsed = 0;
    long long suma = 0;

    for (int j = 0; j < N; j++) {
    start = high_resolution_clock::now();

        suma = sumar_primos(SIZE);

        end = high_resolution_clock::now();
        timeElapsed += 
            duration<double, std::milli>(end - start).count();
    }
    
    cout << "avg time = " << fixed << setprecision(3) 
    << (timeElapsed / N) <<  " ms\n";

    cout << "Suma de primos hasta "<< SIZE << ": " << suma << endl;

    return 0;
}