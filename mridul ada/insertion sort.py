def insertion_sort(array):
  
    for i in range(1, len(array)):
        key = array[i] 
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key  
    return array


numbers = [12, 4, 7, 9, 1, 3]
print("Original list:", numbers)
print("Sorted list:", insertion_sort(numbers))