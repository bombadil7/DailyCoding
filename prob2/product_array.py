from functools import reduce
# The goal is to produce a new array, in which every
# item is the product of all other elements of the 
# original array

def get_remaining(lst, ind):
    return [x for i, x in enumerate(lst) if i != ind]


def main():
        array = [2, 4, 5, 2, 3]
        all_subarrays = list(get_remaining(array, i) for i in range(len(array)))
        new_array = []
        for sub in all_subarrays:
                new_array.append(reduce((lambda x,y: x*y), sub))
        #new_array = list(reduce((lambda x,y: x*y), subarray for subarray in all_subarrays))
        print(new_array)
        #new_array = list(map(reduce((lambda x, y: x*y), sub_array for sub_array in ), sub_array))


if __name__ == "__main__":
        main()