# function that finds target value inside array using Binary Search.
def search(arr,target):
    mid = len(arr)//2 
    steps = 0                  # since "mid" variable will get updated each time inside loop, we cannot return mid as index of variable.
                               # we need an additional variable "steps", to store index relative to orginal array.
    while mid > 0 or len(arr) >= 1:    
        if arr[mid] == target:                       # if found
            return steps + mid                       # return counter + mid
        elif len(arr) == 1 and arr[mid] != target:   # breaking condition i.e., if len of array is 1 and is not equal to target
            break
        elif target > arr[mid]: 
            steps = steps + mid                      # update step
            arr = arr[mid:]        
        elif target < arr[mid]:    
            arr = arr[:mid]                          # no need to update step, if we move right, since it is initializrd zero
        mid = len(arr) // 2                          # find mid
    return -1 
