import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Algorithm Visualizer")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Delay in milliseconds for visualization (adjust as needed)
DELAY = 10

# Function to generate random data
def generate_random_data(size):
    return [random.randint(10, 400) for _ in range(size)]

# Sorting algorithms

def selection_sort(data):
    n = len(data)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if data[j] < data[min_index]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]
        draw_data(data, [GREEN if x == i or x == min_index else WHITE for x in range(n)])
        pygame.time.delay(DELAY)
        update_display()

def bubble_sort(data):
    n = len(data)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                draw_data(data, [GREEN if x == j or x == j + 1 else WHITE for x in range(n)])
                pygame.time.delay(DELAY)
                update_display()

def insertion_sort(data):
    n = len(data)
    for i in range(1, n):
        current_value = data[i]
        j = i - 1
        while j >= 0 and data[j] > current_value:
            data[j + 1] = data[j]
            j -= 1
            draw_data(data, [GREEN if x == i else WHITE if x == j + 1 else WHITE for x in range(n)])
            pygame.time.delay(DELAY)
            update_display()
        data[j + 1] = current_value

def merge_sort(data):
    if len(data) > 1:
        mid = len(data) // 2
        left_half = data[:mid]
        right_half = data[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i, j, k = 0, 0, 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                data[k] = left_half[i]
                i += 1
            else:
                data[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            data[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            data[k] = right_half[j]
            j += 1
            k += 1

        draw_data(data, [GREEN if x >= mid else BLUE for x in range(len(data))])
        pygame.time.delay(DELAY)
        update_display()

def quick_sort(data, low, high):
    if low < high:
        pivot_index = partition(data, low, high)
        quick_sort(data, low, pivot_index)
        quick_sort(data, pivot_index + 1, high)

def partition(data, low, high):
    pivot = data[low]
    left = low + 1
    right = high
    done = False
    while not done:
        while left <= right and data[left] <= pivot:
            left = left + 1
        while data[right] >= pivot and right >= left:
            right = right - 1
        if right < left:
            done = True
        else:
            data[left], data[right] = data[right], data[left]
    data[low], data[right] = data[right], data[low]
    return right

def heapify(data, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and data[left] > data[largest]:
        largest = left
    if right < n and data[right] > data[largest]:
        largest = right
    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        heapify(data, n, largest)

def heap_sort(data):
    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i)
    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        heapify(data, i, 0)
        draw_data(data, [GREEN if x == i else WHITE for x in range(n)])
        pygame.time.delay(DELAY)
        update_display()

def counting_sort(data):
    max_value = max(data)
    min_value = min(data)
    range_of_elements = max_value - min_value + 1
    count = [0] * range_of_elements
    output = [0] * len(data)

    for num in data:
        count[num - min_value] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in range(len(data) - 1, -1, -1):
        output[count[data[i] - min_value] - 1] = data[i]
        count[data[i] - min_value] -= 1

    data.clear()
    data.extend(output)

def radix_sort(data):
    max_value = max(data)
    exp = 1
    while max_value // exp > 0:
        counting_sort(data, exp)
        exp *= 10

def bucket_sort(data):
    num_buckets = len(data)
    max_value = max(data)
    min_value = min(data)
    bucket_range = (max_value - min_value) / num_buckets

    buckets = [[] for _ in range(num_buckets)]
    for num in data:
        index = int((num - min_value) / bucket_range)
        if index != num_buckets:
            buckets[index].append(num)
    
    for i in range(num_buckets):
        insertion_sort(buckets[i])
    
    sorted_data = []
    for bucket in buckets:
        sorted_data.extend(bucket)

    data.clear()
    data.extend(sorted_data)

def update_plot(arr):
    plt.clf()
    plt.bar(range(len(arr)), arr, align='edge', alpha=0.7)
    plt.draw()
    plt.pause(0.1)

if __name__ == "__main__":
    array_size = 20
    data = np.random.randint(1, 100, array_size)

    sorting_algorithms = {
        1: ("Bubble Sort", bubble_sort),
        2: ("Selection Sort", selection_sort),
        3: ("Insertion Sort", insertion_sort),
        4: ("Merge Sort", merge_sort),
        5: ("Quick Sort", quick_sort),
        6: ("Heap Sort", heap_sort),
        7: ("Counting Sort", counting_sort),
        8: ("Radix Sort", radix_sort),
        9: ("Bucket Sort", bucket_sort)
    }

    print("Choose a sorting algorithm:")
    for key, value in sorting_algorithms.items():
        print(f"{key}. {value[0]}")

    choice = int(input("Enter your choice: "))

    plt.bar(range(len(data)), data, align='edge', alpha=0.7)
    plt.draw()
    plt.pause(1)

    if choice in sorting_algorithms:
        sort_name, sort_function = sorting_algorithms[choice]
        sort_function(data)
        plt.title(f"{sort_name} Result")
        plt.show()
    else:
        print("Invalid choice")
