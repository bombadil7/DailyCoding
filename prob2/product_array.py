from functools import reduce
# The goal is to produce a new array, in which every
# item is the product of all the elements of the 
# original array except current element

def remove_current_element(lst, index):
    """ Given a list and index of one element we remove that element from the list """
    return [x for i, x in enumerate(lst) if i != index]

def multiply_elements(lst):
    """ Given a list we multiply all the element of it and return as a single number """
    return reduce((lambda x,y: x*y), lst)

def main():
    array = [2, 4, 5, 2, 3]

    all_subarrays = list(remove_current_element(array, i) for i in range(len(array)))
    new_array = list(map(multiply_elements,[x for x in all_subarrays]))

    print(new_array)


if __name__ == "__main__":
    main()