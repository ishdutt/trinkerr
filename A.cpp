#include <iostream>

using namespace std;

long long squareadder(long long number) {
    long long res = 0;
    while(number != 0) {
        int lsd = number % 10;
        res += lsd * lsd;
        number /= 10;
    }
    return res;
}

int main() {
    long long number;
    cin >> number;
    int count = 0;
    while(number / 10 != 0) {
        number = squareadder(number);
        count++;
    }
    if(number / 10 == 0) {
        if(number == 1) {
            cout << count;
            return 0;
        }
        cout << -1;
        return 0;
    }
}