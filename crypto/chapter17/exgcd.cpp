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

int main(){
    int a, b;
    cout << "aの値: ";
    cin >> a;
    cout << "bの値: ";
    cin >> b;

    int x, y;
    tie(x,y) = exgcd(a, b);

    cout << "(" << x << ", " << y << ")" << endl;
    return 0;
}

