#include <iostream>
using namespace std;

int main() {
    int ti[8][2] = {
        {390, 540},
        {590, 600},
        {650, 660},
        {710, 720},
        {770, 830},
        {880, 890},
        {940, 950},
        {1000, 1370}
    };
    
    int h, m, t = 0;
    cin >> h >> m;
    int a = h*60 + m;
    
    for (int i = 0; i < 8; i++) {
        if (ti[i][0] <= a && a <= ti[i][1]) {
            t = 1;
            break;
        }
    }
    
    if (t==1) cout << "Yes"; 
    else cout << "No";
    return 0;
}