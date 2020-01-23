def binarySearch(array, left, right, x):
    
    if(right >= left):
        
        middle = left + int((right - 1)/2)
        
        if(array[middle] == x):
            return middle

        elif(array[middle] > x):
            return binarySearch(array, left, middle-1, x)
        
        else:
            return binarySearch(array, middle+1, right, x)
    else:
        return -1

array = [2, 3, 4, 10, 40]
x = 10

result = binarySearch(array, 0, len(array)-1, x)
print(result)
