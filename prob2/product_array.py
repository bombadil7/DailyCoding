from functools import reduce
# The goal is to produce a new array, in which every
# item is the product of all the elements of the 
# original array except current element

def main():
    array = [2, 4, 5, 2, 3]

    # Given a list and index of one element we remove that element from the list
    remove_current_element = lambda lst, index: [x for i, x in enumerate(lst) if i != index]

    # Given a list we multiply all elements of it and return as a single number
    multiply_elements = lambda lst: reduce((lambda x,y: x*y), lst)

    # Create a list of new lists with required elements removed
    all_subarrays = list(remove_current_element(array, i) for i in range(len(array)))

    # Reduce each sub-list to a single number, which is a product of all elements
    new_array = list(map(multiply_elements,[x for x in all_subarrays]))

    print(new_array)


if __name__ == "__main__":
    main()