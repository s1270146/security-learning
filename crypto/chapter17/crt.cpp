#include <iostream>
#include <tuple>

using namespace std;

tuple<int, int> exgcd(int a, int b){
    if (a == 0)
    {
        return forward_as_tuple(0, 1 / b);
    }
    int q = b / a;
    int r = b % a;
    int s, t;
    tie(s, t) = exgcd(r, a);
    return forward_as_tuple(t - q * s, s);
};

int crt(int a[], int m[], int length){
    int mm = 1;
    for (int i = 0; i < length; i++)
    {
        mm *= m[i];   
    }
    int x = 0;
    for (int i = 0; i < length; i++)
    {
        int mi = mm / m[i];
        int mi_inv, not_required;
        tie(mi_inv, not_required) = exgcd(mi, m[i]);
        while (mi_inv < 0)
        {
            mi_inv += m[i];
        }
        int ti = mi_inv % m[i];
        x += (mi*ti*a[i])%mm;        
    }
    return x % mm;
}

int main(){
    int a[3] = {2, 3, 2};
    int b[3] = {3, 5, 7};
    cout << crt(a, b, 3) << endl;
    return 0;
}