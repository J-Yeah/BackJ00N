#include <iostream>
#include <string>
using namespace std;

int main() {
    string n;
 
    while (true) {
        int total = 0;
        cin >> n;
        if (n == "0") break;

        for (char c : n) {
            if (c == '1') total += 2;
            else if (c == '0') total += 4;
            else total += 3;
        }

        total += n.length() +1 ;
        cout << total << endl;
    }
    return 0;
}