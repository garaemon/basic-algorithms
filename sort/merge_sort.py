#!/usr/bin/env python

# merge sort
# run time computation amount is O(nlogn

def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp
    return arr


def merge_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        middle_index = len(arr) / 2
        before_arr = merge_sort(arr[0:middle_index])
        after_arr = merge_sort(arr[middle_index:])
        merged_arr = [None] * len(arr)
        i = 0
        j = 0
        while True:
            if i == len(before_arr) and j == len(after_arr):
                return merged_arr         #end of sorting
            if i == len(before_arr):
                merged_arr[i + j] = after_arr[j]
                j = j + 1
            elif j == len(after_arr):
                merged_arr[i + j] = before_arr[i]
                i = i + 1
            elif before_arr[i] < after_arr[j]:
                merged_arr[i + j] = before_arr[i]
                i = i + 1
            else:
                merged_arr[i + j] = after_arr[j]
                j = j + 1

                


if __name__ == "__main__":
    arr = [3, 1, 7, 2, 4, 6, 0]
    print merge_sort(arr)
