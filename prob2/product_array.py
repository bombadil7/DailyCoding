from functools import reduce
# The goal is to produce a new array, in which every
# item is the product of all the elements of the 
# original array except current element

def convert(array):
    # Create a list of new lists with required elements removed
    all_subarrays = list(map((lambda index: [x for i, x in enumerate(array) if i != index]), (index for index in range(len(array)))))

    # Reduce each sub-list to a single number, which is a product of all elements
    return list(map((lambda lst: reduce((lambda x,y: x*y), lst)), (lst for lst in all_subarrays)))


def main():
    array = [2, 4, 5, 2, 3]
    print(convert(array))


if __name__ == "__main__":
    main()