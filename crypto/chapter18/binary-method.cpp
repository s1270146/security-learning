#include <iostream>

using namespace std;

int power(int m, int n, int mod){
    int a = 1;
    while (n > 0)
    {
        if (n % 2 == 1)
        {
            a = a * m;
        }
        m = m * m;
        n /= 2;
    }
    return a;    
}

int main(){
    cout << power(2, 13, 0) << endl;
    return 0;
}