#include <iostream>
#include <thread>

using namespace std; 

void task(){
    for(int i = 1; i <= 10; i++){
        cout << i << " ";
    }
    cout << "\n";
}

int main(){
    thread t;
    t = thread(task);

    t.join(); // no puedes seguir con la instrucción ed abajo hasta que el hilo t termine

    return 0;
}