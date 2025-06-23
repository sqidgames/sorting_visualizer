import time
from visualizer import RED, GREEN
def bubble_sort(array, draw_array, delay):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                draw_array(array, [RED if x == j or x == j + 1 else GREEN for x in range(len(array))])
                time.sleep(delay)

def selection_sort(array, draw_array, delay):
    for i in range(len(array)):
        min_idx = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_idx]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
        draw_array(array, [RED if x == i or x == min_idx else GREEN for x in range(len(array))])
        time.sleep(delay)

def insertion_sort(array, draw_array, delay):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
        draw_array(array, [RED if x == j + 1 or x == i else GREEN for x in range(len(array))])
        time.sleep(delay)

def merge_sort(array, draw_array, delay, left=0, right=None):
    if right is None:
        right = len(array) - 1
    if left < right:
        mid = (left + right) // 2
        merge_sort(array, draw_array, delay, left, mid)
        merge_sort(array, draw_array, delay, mid + 1, right)
        merge(array, draw_array, delay, left, mid, right)

def merge(array, draw_array, delay, left, mid, right):
    temp = []
    i, j = left, mid + 1
    while i <= mid and j <= right:
        if array[i] <= array[j]:
            temp.append(array[i])
            i += 1
        else:
            temp.append(array[j])
            j += 1
    while i <= mid:
        temp.append(array[i])
        i += 1
    while j <= right:
        temp.append(array[j])
        j += 1
    for i in range(len(temp)):
        array[left + i] = temp[i]
        draw_array(array, [RED if x == left + i else GREEN for x in range(len(array))])
        time.sleep(delay)

def quick_sort(array, draw_array, delay, low=0, high=None):
    if high is None:
        high = len(array) - 1
    if low < high:
        pi = partition(array, draw_array, delay, low, high)
        quick_sort(array, draw_array, delay, low, pi - 1)
        quick_sort(array, draw_array, delay, pi + 1, high)

def partition(array, draw_array, delay, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
        draw_array(array, [RED if x == j or x == i else GREEN for x in range(len(array))])
        time.sleep(delay)
    array[i + 1], array[high] = array[high], array[i + 1]
    draw_array(array, [RED if x == high or x == i + 1 else GREEN for x in range(len(array))])
    time.sleep(delay)
    return i + 1
