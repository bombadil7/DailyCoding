#include <stdio.h>

#define SIZE 5

int mul_array(int *array, int size, int *newArray);
void print(int *array, int size);

int main(void)
{
    int ar[SIZE] = {1, 2, 3, 4, 5};
    int newAr[SIZE];

    int s = mul_array(ar, SIZE, newAr);
    print(newAr, SIZE);

    return 0;
}



int mul_array(int *array, int size, int *newArray)
{
    int prod;
    for (int i = 0; i < size; ++i){
        prod = 1;
        for (int j = 0; j < size; ++j){
            if (j != i){
                prod *= array[j];
            }
        }
        newArray[i] = prod;
    }
    return size;
}


void print(int *array, int size)
{
    for (int i = 0; i < size; ++i)
        printf("%i ", array[i]);
    printf("\n");
}