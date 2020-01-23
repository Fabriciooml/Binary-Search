def binarySearch(array, left, right, x):
    
    if(right >= left):
        
        middle = left + (right - 1)/2
        
        if(array[middle] == x):
            return middle

        elif(array[middle] > x):
            return binarySearch(array, left, middle-1, x)
        
        else:
            return binarySearch(array, middle+1, right, x)
    else:
        return -1
