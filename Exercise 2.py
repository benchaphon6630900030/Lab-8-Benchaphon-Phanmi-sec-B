array = [ ]
print(" ")

array = [29,10,14,37,14,20,7,16,12]
print("\n""Array is Unsorted : ")

def partition(array, min, max): 
    pivot = array[max]
    i = min - 1
    for j in range(min, max):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[max]) = (array[max], array[i + 1])
    return i + 1

def quick(array, min, max):
    if min < max:
        sub_array = partition(array, min, max)
        quick(array, min, sub_array - 1)
        quick(array, sub_array + 1, max)

print(array)

size = len(array)
quick(array, 0, size - 1)

print("\n""Array is Sorted : ")
print(array)
