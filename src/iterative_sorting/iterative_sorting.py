# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1): # loop through the array. start with current index. set it to smallest.
        cur_index = i
        smallest_index = cur_index
        
        for j in range(cur_index + 1, len(arr)): # loop through the rest of array and compare a second time called j
            if arr[j] < arr[smallest_index]: # if actual value of j is less than the actual value of smallest index
                smallest_index = j # set the index j to index of smallest value

        # TO-DO: swap
        smallest_value = arr[smallest_index] # move actual value of smallest index to a temporary variable.
        arr[smallest_index] = arr[cur_index] # move actual value of current index to actual value of smallest index
        arr[cur_index]= smallest_value # move temporary value to actual value of current index

    return arr

print(selection_sort(arr=[5, 2, 8, 4, 7, 1, 6]))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( bubble_arr ): 
    for i in range(len(bubble_arr)): # loop through the array

        for j in range(len(bubble_arr) - 1): # loop through the array a second time with j. minus len - 1
            
            if bubble_arr[j] > bubble_arr[j + 1]: # compare if 1st value > second value:
                # Swap
                temp = bubble_arr[j]
                bubble_arr[j] = bubble_arr[j + 1]
                bubble_arr[j + 1] = temp
                
    return bubble_arr

print(bubble_sort(bubble_arr=[3, 1, 4, 5, 2, 9, 7, 6, 8, 10, 11]))


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr