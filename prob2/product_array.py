from functools import reduce
# The goal is to produce a new array, in which every
# item is the product of all the elements of the 
# original array except for the currently selected element. 
# Example: [1, 2, 3, 4] -> [24, 12, 8, 6]

def convert(array):
    """ Do conversion in two steps: 1) create lists with indexed elements removed and 2) multiply their elementsself.
        These steps follow in reverse order. """
    return list(map((lambda lst: reduce((lambda x,y: x*y), lst)), 
            list(map((lambda index: [x for i, x in enumerate(array) if i != index]), (index for index in range(len(array)))))))


def main():
    array = [2, 4, 5, 2, 3]
    print(convert(array))


if __name__ == "__main__":
    main()