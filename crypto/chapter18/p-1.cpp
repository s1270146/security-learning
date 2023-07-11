#include <iostream>
#include <math.h>
#include <random>

using namespace std;

bool isPrime(uint64_t n){
    if (n < 2) return false;
    else if (n == 2) return true;
    else if (n % 2 == 0) return false;

    double sqrtNum = sqrt(n);
    for (int i = 3; i <= sqrtNum; i += 2)
    {
        if (n % i == 0)
        {
            return false;
        }
    }
    return true;
}

uint64_t getRandRange(uint64_t min_val, uint64_t max_val){
    static std::mt19937_64 mt64(0);
    // [min_val, max_val] の一様分布整数 (int) の分布生成器
    std::uniform_int_distribution<uint64_t> get_rand_uni_int( min_val, max_val );

    // 乱数を生成
    return get_rand_uni_int(mt64);
}

uint64_t getPrime(int bit_num){
    uint64_t min_val = pow(2, bit_num - 1) + 1;
    uint64_t max_val = pow(2, bit_num) - 1;
    uint64_t p = getRandRange(min_val, max_val);
    while (!isPrime(p))
    {
        p = (p + 1);
        if (p > pow(2, bit_num) - 1){
            p = pow(2, bit_num - 1) + 1;
        }
    }
    return p;
}

uint64_t nextPrime(uint64_t x){
    while (1)
    {
        x++;
        if (isPrime(x)){
            break;
        }
    }
    return x;
}

int main(){
    int bit_num;
    cin >> bit_num;
    cout << "Generating prime number ..." << endl;
    uint64_t p = getPrime(bit_num);
    cout << "p: " << p << endl;
}