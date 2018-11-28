/*
 * two_to_k.c
 * When supplied a list of numbers as arguments this code searches this list
 * to find if there's a pair of numbers that when summed up produces the last
 * number.  I.E.  1 3 4 5 will fail because 5 is not the sum of any two preceding numbers.
 */

// TODO: Use a hash table to store values seen and check in that table as 
// you go through the list at constant time.

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define SEED 15
#define MAX_RAND 501

bool findPair(int list[], int size, int k, int* num1, int* num2);

int main(int argc, char *argv[])
{
    // This implementation minimizes memory usage by creating the smallest
    // array that the argument list requires.
    //int numbers[50];
    int size;
    int *numbers = NULL;
    int k;
    // Verify that arguments have been provided 
    if (argc < 3) {
        printf("Use: a.exe num1, num2, ..., numN, k\n", argv[2]);
        exit(1);
    }

    if (argc > 3) {
        size = argc - 2;
        numbers = (int*) malloc(size*sizeof(int));

        // Convert arguments into an integer array
        // atoi returns zero if argument is not a number, so it is safe not to check
        for (int i = 1; i <= size; ++i) {
            numbers[i-1] = atoi(argv[i]);
        }

    } else if (argc = 3) {
        srand(SEED);
        size = atoi(argv[1]);
        numbers = (int*) malloc(size*sizeof(int));

        // Generate random list of numbers of size N and search for number k 
        for (int i = 0; i < size; ++i) {
            numbers[i] = rand() % MAX_RAND;
        }
    } 
    // The last argument is the number k, which must be equal to a
    // sum of a pair of numbers in the list.
    k = atoi(argv[argc-1]);

    int n1=0, n2=0;
    if (findPair(numbers, size, k, &n1, &n2))
        printf("Numbers %d and %d add up to %d\n", n1, n2, k);
    else
        printf("There are no numbers in this list that add up to %d\n", k);

    free(numbers);

    return 0;
}

// Return value is true if a pair has been found and false otherwise.
// The actual two numbers that add up to 'k' are returned through 
// argument list by pointer.
bool findPair(int list[], int size, int k, int* num1, int* num2)
{
    *num1 = 0;
    *num2 = 0;
    for (int i = 0; i < size; ++i)
        for (int j = i+1; j < size; ++j)
            if (list[i] + list[j] == k){
                *num1 = list[i];
                *num2 = list[j];
                return true;
            }

    return false;
}
