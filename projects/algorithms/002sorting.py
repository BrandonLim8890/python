'''
Author: Brandon Lim
Project: sorting.py
Description: Merge and bubble sort
'''

def bubbleSort(arr):
    for i in range(0, len(arr)):
        for j in range(1, len(arr)):
            if arr[i] < arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr


def runner():
    arr = [8,5,2,4,7,8]
    print(bubbleSort(arr))

runner()
    