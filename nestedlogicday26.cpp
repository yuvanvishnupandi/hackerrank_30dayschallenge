#include <iostream>

int main() {
    int d1, m1, y1; // Returned date
    int d2, m2, y2; // Due date
    
    std::cin >> d1 >> m1 >> y1;
    std::cin >> d2 >> m2 >> y2;

    int fine = 0;

    if (y1 > y2) {
        fine = 10000;
    } else if (y1 == y2) {
        if (m1 > m2) {
            fine = 500 * (m1 - m2);
        } else if (m1 == m2 && d1 > d2) {
            fine = 15 * (d1 - d2);
        }
    }

    std::cout << fine << std::endl;
    
    return 0;
}
