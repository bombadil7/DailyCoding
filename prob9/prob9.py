#
#This problem was asked by Airbnb.
#
#Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
#
#For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
#
#Follow-up: Can you do this in O(N) time and constant space?

def largestSum(numbers):
    if numbers[0] > numbers[1]:
        largest = numbers[0]
    else:
        largest = numbers[1]

#    for i, num in enum(range(size(numbers))):



    return largest

def main():
    l = [2, 4, 6, 2, 5]
    largest = largestSum(l)
    print(largest)

if __name__ == "__main__":
    main()