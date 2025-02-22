#include <iostream>
#include <vector>
#include <stdexcept>
#include <cassert>

int minimum_index(const std::vector<int>& seq) {
    if (seq.empty()) {
        throw std::invalid_argument("Cannot get the minimum value index from an empty sequence");
    }
    
    int min_idx = 0;
    for (size_t i = 1; i < seq.size(); i++) {
        if (seq[i] < seq[min_idx]) {
            min_idx = i;
        }
    }
    return min_idx;
}

class TestDataEmptyArray {
public:
    static std::vector<int> get_array() {
        return {};
    }
};

class TestDataUniqueValues {
public:
    static std::vector<int> get_array() {
        return {5, 3, 8, 1, 7};
    }
    
    static int get_expected_result() {
        return 3;
    }
};

class TestDataExactlyTwoDifferentMinimums {
public:
    static std::vector<int> get_array() {
        return {2, 1, 4, 1, 6};
    }
    
    static int get_expected_result() {
        return 1;
    }
};

void run_tests() {
    try {
        auto arr = TestDataEmptyArray::get_array();
        minimum_index(arr);
        assert(false);
    } catch (const std::invalid_argument&) {
    }

    auto arr1 = TestDataUniqueValues::get_array();
    int result1 = minimum_index(arr1);
    assert(result1 == TestDataUniqueValues::get_expected_result());

    auto arr2 = TestDataExactlyTwoDifferentMinimums::get_array();
    int result2 = minimum_index(arr2);
    assert(result2 == TestDataExactlyTwoDifferentMinimums::get_expected_result());

    std::cout << "OK" << std::endl;
}

int main() {
    run_tests();
    return 0;
}
