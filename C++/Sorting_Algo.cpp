#include <iostream>
#include <vector>
#include <algorithm>
#include <chrono>
#include <thread>

// Function to generate random data
std::vector<int> generate_random_data(int size) {
    std::vector<int> data;
    for (int i = 0; i < size; ++i) {
        data.push_back(rand() % 391 + 10); // Random value between 10 and 400
    }
    return data;
}

// Function to print the data
void print_data(const std::vector<int>& data) {
    for (int num : data) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
}

// Sorting algorithms

void selection_sort(std::vector<int>& data) {
    int n = data.size();
    for (int i = 0; i < n - 1; ++i) {
        int min_index = i;
        for (int j = i + 1; j < n; ++j) {
            if (data[j] < data[min_index]) {
                min_index = j;
            }
        }
        std::swap(data[i], data[min_index]);
    }
}

void bubble_sort(std::vector<int>& data) {
    int n = data.size();
    for (int i = 0; i < n - 1; ++i) {
        for (int j = 0; j < n - i - 1; ++j) {
            if (data[j] > data[j + 1]) {
                std::swap(data[j], data[j + 1]);
            }
        }
    }
}

void insertion_sort(std::vector<int>& data) {
    int n = data.size();
    for (int i = 1; i < n; ++i) {
        int current_value = data[i];
        int j = i - 1;
        while (j >= 0 && data[j] > current_value) {
            data[j + 1] = data[j];
            --j;
        }
        data[j + 1] = current_value;
    }
}

void merge(std::vector<int>& data, int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;
    std::vector<int> left_half(n1), right_half(n2);
    for (int i = 0; i < n1; ++i) {
        left_half[i] = data[left + i];
    }
    for (int i = 0; i < n2; ++i) {
        right_half[i] = data[mid + 1 + i];
    }
    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (left_half[i] <= right_half[j]) {
            data[k] = left_half[i];
            ++i;
        } else {
            data[k] = right_half[j];
            ++j;
        }
        ++k;
    }
    while (i < n1) {
        data[k] = left_half[i];
        ++i;
        ++k;
    }
    while (j < n2) {
        data[k] = right_half[j];
        ++j;
        ++k;
    }
}

void merge_sort(std::vector<int>& data, int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        merge_sort(data, left, mid);
        merge_sort(data, mid + 1, right);
        merge(data, left, mid, right);
    }
}

int partition(std::vector<int>& data, int low, int high) {
    int pivot = data[high];
    int i = (low - 1);
    for (int j = low; j <= high - 1; ++j) {
        if (data[j] <= pivot) {
            ++i;
            std::swap(data[i], data[j]);
        }
    }
    std::swap(data[i + 1], data[high]);
    return (i + 1);
}

void quick_sort(std::vector<int>& data, int low, int high) {
    if (low < high) {
        int pi = partition(data, low, high);
        quick_sort(data, low, pi - 1);
        quick_sort(data, pi + 1, high);
    }
}

void heapify(std::vector<int>& data, int n, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;
    if (left < n && data[left] > data[largest]) {
        largest = left;
    }
    if (right < n && data[right] > data[largest]) {
        largest = right;
    }
    if (largest != i) {
        std::swap(data[i], data[largest]);
        heapify(data, n, largest);
    }
}

void heap_sort(std::vector<int>& data) {
    int n = data.size();
    for (int i = n / 2 - 1; i >= 0; --i) {
        heapify(data, n, i);
    }
    for (int i = n - 1; i > 0; --i) {
        std::swap(data[0], data[i]);
        heapify(data, i, 0);
    }
}

// ... (Counting sort, Radix sort, Bucket sort functions here)

// Function to clear the console screen
void clear_screen() {
    #if defined(_WIN32) || defined(_WIN64)
        system("cls");
    #else
        system("clear");
    #endif
}

int main() {
    srand(time(nullptr));

    std::vector<int> data;
    int choice, size;
    while (true) {
        std::cout << "Sorting Algorithm Visualizer" << std::endl;
        std::cout << "1. Generate New Random Data" << std::endl;
        std::cout << "2. Selection Sort" << std::endl;
        std::cout << "3. Bubble Sort" << std::endl;
        std::cout << "4. Insertion Sort" << std::endl;
        std::cout << "5. Merge Sort" << std::endl;
        std::cout << "6. Quick Sort" << std::endl;
        std::cout << "7. Heap Sort" << std::endl;
        std::cout << "8. Counting Sort" << std::endl;
        std::cout << "9. Radix Sort" << std::endl;
        std::cout << "10. Bucket Sort" << std::endl;
        std::cout << "11. Exit" << std::endl;
        std::cout << "Enter your choice: ";
        std::cin >> choice;

        if (choice == 1) {
            std::cout << "Enter the size of the data: ";
            std::cin >> size;
            data = generate_random_data(size);
            std::cout << "Random data generated." << std::endl;
            print_data(data);
        } else if (choice >= 2 && choice <= 10) {
            clear_screen();
            std::cout << "Sorting Algorithm: " << choice << std::endl;
            std::cout << "Original data: ";
            print_data(data);
            std::cout << "Sorting..." << std::endl;

            switch (choice) {
                case 2: selection_sort(data); break;
                case 3: bubble_sort(data); break;
                case 4: insertion_sort(data); break;
                case 5: merge_sort(data, 0, data.size() - 1); break;
                case 6: quick_sort(data, 0, data.size() - 1); break;
                case 7: heap_sort(data); break;
                // ... (Counting sort, Radix sort, Bucket sort calls here)
            }

            std::cout << "Sorted data: ";
            print_data(data);
            std::this_thread::sleep_for(std::chrono::seconds(1));
        } else if (choice == 11) {
            std::cout << "Exiting..." << std::endl;
            break;
        } else {
            std::cout << "Invalid choice. Please try again." << std::endl;
        }
    }

    return 0;
}
