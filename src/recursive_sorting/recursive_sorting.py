# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    # loop thru the first array, loop thru the second array. 
    # compare if first array < second array. if so concatnate the arrays variable. 
    
    temp_array = []

    for i in range(len(arrA)): 
      temp_array.append(arrA[i])

      for j in range(len(arrB)):
        if arrB[j] < arrA[i]:
          temp_array.append(arrB[j])
          print(temp_array)
        elif arrB[j] > arrA[i]:
          temp_array.append(arrA[i])
          
        
    return merged_arr
    
    

merge([1, 2, 3, 4, 5], [10, 11, 12, 13, 14, 15, 16])
# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
