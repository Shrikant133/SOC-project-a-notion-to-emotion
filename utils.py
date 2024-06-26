def findmax(array):
    max= array[0]
    for i in array:
        if max<=i:
            max= i
    return max
