Write a script that sorts a list of tuples based on the number value in the tuple. For example:

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]

# organize tuples by value
def get_order(tup):
    return tup[1]

sorted_list = sorted(unsorted_list, key=get_order)  # sort the unsorted list according to function
print(sorted_list) 
