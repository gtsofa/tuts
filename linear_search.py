def linear_search(list_values, target_item, start=0):
  """
  method to implement linear search
    -liste_values[] => list with all the values
    - target_item => value to be found
    - n => total number of elements in the array
  """
  for i in range(start, len(list_values)):
    if list_values[i] == target_item:
      return i
    
    return 'not found!'
 
# test the implementation
list_values = [5, 34, 65, 12, 77, 35]
target_item = 77
print(linear_search(list_values,target_item))
