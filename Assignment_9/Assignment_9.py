
import random
import sys


def fill_arr(size):

    arr = [0] * size

    for i in range(0, size):
        arr[i] = random.randint(0,1000)

    return arr

def bubbleSort(arr):
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n-1):
    # range(n) also work but outer loop will
    # repeat one time more than needed.
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def selectionSort(arr):
        # Traverse through all array elements
    for i in range(len(arr)):
      
        # Find the minimum element in remaining 
        # unsorted array
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
              
        # Swap the found minimum element with 
        # the first element        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertionSort(arr):
  
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
  
        key = arr[i]
  
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

def main():

    size = int(sys.argv[1])

    arr = fill_arr(size)



    print('Unsorted Array:')

    print(str(arr) + '\n')



    arr_insertion = arr[:]

    print('Insertion Sort:')

    insertionSort(arr_insertion)

    print(str(arr_insertion) + '\n')



    arr_bubble = arr[:]

    print('Bubble Sort:')

    bubbleSort(arr_bubble)

    print(str(arr_bubble) + '\n')



    arr_selection = arr[:]

    print('Selection Sort:')

    bubbleSort(arr_selection)

    print(str(arr_selection) + '\n')



if __name__ == '__main__' : main()