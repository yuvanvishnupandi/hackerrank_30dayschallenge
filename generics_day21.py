#include <iostream>
#include <vector>

using namespace std;

template <typename T>
void printArray(vector<T> arr) {
    for (const T& element : arr) {
        cout << element << endl;
    }
}

int main() {
    vector<int> intArray = {1, 2, 3};
    vector<string> stringArray = {"Hello", "World"};
    
    printArray(intArray);
    printArray(stringArray);
    
    return 0;
}