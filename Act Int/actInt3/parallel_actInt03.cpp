//
//  Joanna Nicole Uriostegui Magaña - A01711853
//  *Actividad Integradora 3*
//
//  Parelelo A
//  Tiempo: 312.428 ms
//
//  Sp = 3.4517
//  E = 0.8629 = 86.29%
//
#include <iostream>
#include <iomanip>
#include <chrono>
#include <thread>
#include "utils.h"

using namespace std;
using namespace std::chrono;

#define THREADS std::thread::hardware_concurrency()

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

void sumar_primos(int start, int end, long long *result) {
    long long suma = 0;
    for (int i = start; i <= end; i++) {
        if(es_primo(i)){
            suma+= i;
        }
    }
    *result = suma;
}

int main(int argc, char* argv[]) {

    high_resolution_clock::time_point startTime, endTime;
    double timeElapsed = 0;

    int block_size = SIZE / THREADS;
    int remainder = SIZE % THREADS;

    thread threads[THREADS];
    long long results[THREADS] = {0};

    cout << "Starting...\n";

    long long suma = 0;

    for (int j = 0; j < N; j++) {
        startTime = high_resolution_clock::now();

        long start = 0;
        for (int i = 0; i < THREADS; i++) {
            int end = start + block_size + (i < remainder ? 1 : 0);
            threads[i] = thread(sumar_primos, start, end, &results[i]);
            start = end;
        }

        for (int i = 0; i < THREADS; i++) {
            threads[i].join();
        }

        suma = 0;
        for (int i = 0; i < THREADS; i++) {
            suma += results[i];
        }

        endTime = high_resolution_clock::now();
        timeElapsed += duration<double, std::milli>(endTime - startTime).count();
    }

    cout << "avg time = " << fixed << setprecision(3)
         << (timeElapsed / N) << " ms\n";

    cout << "Suma de primos hasta "<< SIZE << ": " << suma << endl;

    return 0;
}