#!/usr/bin/env python

# insert sort
# run time computation amount is O(n^2)

def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp
    return arr

def insert_sort(arr):
    for n in range(len(arr)):
        # n is the index to be focused on
        if n == 0:
            pass
        elif n == 1:
            if arr[n - 1] > arr[n]:
                swap(arr, n - 1, n)
        else:
             for i in range(n):      #for example, n = 3 => i = [0, 1, 2]
                 if arr[i] > arr[n]:
                     # insert
                     for j in range(n - i):   #swapping from backward
                         inverse_index = n - j
                         swap(arr, n - j, n - j - 1)
                     break
                 
    return arr

if __name__ == "__main__":
    arr = [3, 1, 7, 2, 4, 6, 0]
    print insert_sort(arr)
