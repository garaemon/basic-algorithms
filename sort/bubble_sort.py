#!/usr/bin/env python

# bubble sort
# run time computation amount is O(n^2)

def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp
    return arr

def bubble_sort(arr):
    if len(arr) == 0 or len(arr) == 1:
        return arr
    else:
        for i in range(len(arr) - 1):
            for n in range(len(arr) - 1):
                # compare n and n + 1
                if arr[n] > arr[n + 1]:
                    swap(arr, n, n + 1)
        return arr


if __name__ == "__main__":
   arr = [3, 1, 7, 2, 4, 6, 0]
   print bubble_sort(arr)
   
