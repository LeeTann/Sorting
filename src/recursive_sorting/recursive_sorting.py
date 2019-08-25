# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    print("num of elements", elements)
    merged_arr = []
    cur_index_A = 0
    cur_index_B = 0

    # TO-DO

    for i in range(elements):

      # If no more items in arrA, then add items in arrB.
      if cur_index_A >= len(arrA):
        merged_arr.append(arrB[cur_index_B])
        cur_index_B += 1

      # If no more items in arrB, then add items in arrA.
      elif cur_index_B >= len(arrB):
        merged_arr.append(arrA[cur_index_A])
        cur_index_A += 1
      
      # If A < B, add item A.
      elif arrA[cur_index_A] < arrB[cur_index_B]:
        merged_arr.append(arrA[cur_index_A])
        cur_index_A += 1
      
      # else add B
      else:
        merged_arr.append(arrB[cur_index_B])
        cur_index_B += 1
    
    return merged_arr

# print(merge([5, 7], [2, 6, 8, 9]))

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # Base case
    if len(arr) == 1:
      individual_arr = arr[0]
      print("individual array: ", individual_arr)

    # recurse case
    else:
      mid = len(arr) // 2
      print("mid is", mid)
      left = merge_sort(arr[:mid])
      print("left is", left)
      right = merge_sort(arr[mid:])
      print("right is", right)
      arr = merge(left, right)

    return arr

print(merge_sort([7, 5, 1, 4, 2, 8]))
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
