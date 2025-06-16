//
//  Joanna Nicole Uriostegui Magaña - A01711853
//  *Actividad Integradora 3*
//
//  CUDA  
//  Tiempo: 49.392 ms
//
//  Sp = 21.8340
//  E = 0.0426 = 4.2644%
//

#include <iostream>
#include <iomanip>
#include <chrono>
#include <cuda_runtime.h>
#include "utils.h"

using namespace std;
using namespace std::chrono;

#define SIZE    5000000
#define THREADS 512
#define BLOCKS  min(1024, ((SIZE + THREADS - 1) / THREADS))

__device__ bool es_primo(int n){
    if(n < 2){
        return false;
    }

    int n2 = (int)sqrtf((float)n);
    for(int i = 2; i <= n2; i++){
        if(n % i == 0){
            return false;
        }
    }
    return true;
}

__global__ void sumar_primos(long long *partial) {
    __shared__ long long cache[THREADS];

    int index = threadIdx.x + blockIdx.x * blockDim.x;
    int stride = blockDim.x * gridDim.x;
    int cacheIdx = threadIdx.x;

    long long local_sum = 0;

    for (int i = index; i <= SIZE; i += stride) {
        if (es_primo(i)) {
            local_sum += i;
        }
    }

    cache[cacheIdx] = local_sum;
    __syncthreads();

    // Reducción en el bloque
    int i = blockDim.x / 2;
    while (i > 0) {
        if (cacheIdx < i) {
            cache[cacheIdx] += cache[cacheIdx + i];
        }
        __syncthreads();
        i /= 2;
    }

    if (cacheIdx == 0) {
        partial[blockIdx.x] = cache[0];
    }
}

int main(int argc, char* argv[]) {
    long long *partial, *d_partial;

    // Variables de tiempo
    high_resolution_clock::time_point start, end;
    double timeElapsed;

    partial = new long long[BLOCKS];

    cudaMalloc((void**) &d_partial, BLOCKS * sizeof(long long));

    cout << "Starting...\n";
    timeElapsed = 0;

    for (int j = 0; j < N; j++) {
        start = high_resolution_clock::now();

        sumar_primos<<<BLOCKS, THREADS>>>(d_partial);
        cudaDeviceSynchronize();

        end = high_resolution_clock::now();
        timeElapsed += duration<double, std::milli>(end - start).count();
    }

    cudaMemcpy(partial, d_partial, BLOCKS * sizeof(long long), cudaMemcpyDeviceToHost);

    long long total = 0;
    for (int i = 0; i < BLOCKS; i++) {
        total += partial[i];
    }

    cout << "Suma de primos hasta "<< SIZE << ": " << total << endl;
    cout << "avg time = " << fixed << setprecision(3)
         << (timeElapsed / N) <<  " ms\n";

    delete[] partial;

    cudaFree(d_partial);

    return 0;
}
