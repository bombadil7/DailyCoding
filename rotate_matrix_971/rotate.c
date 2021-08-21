/* Given a square N by N matrix write a function that would 
 * rotate it clockwise by 90 degrees, such that a matrix:
 * [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

    becomes:
 * [[7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]]

 */

#include <stdio.h>
#include <stdlib.h>

#define DIM     4

void printm(int dim, int* m) {
    printf("[");
    for (int i = 0; i < dim; i++) {
        if (i > 0) printf(",\n ");
        printf("[");
        for (int j = 0; j < dim; j++) {
            if (j > 0) printf(", ");
            printf("%2d", m[i * dim + j]);
        }
        printf("]");
    }
    printf("]\n");
}

int* rotate(int dim, int* m) {
    int* mm = malloc(dim * dim * sizeof(int));
    for (int i = 0; i < dim; i++) {
        for (int j = 0; j < dim; j++) {
            // new_row = old_col
            // new_col = dim - 1 - old_row
            mm[j * dim + (dim - i - 1)] = m[i * dim + j];
        }
    }

    return mm;
}

int main(void) {
/*
    int m[DIM][DIM] = {
        {1, 2, 3}, 
        {4, 5, 6}, 
        {7, 8, 9}
        };
*/
    int m[DIM][DIM] = {
        {1, 2, 3, 4}, 
        {5, 6, 7, 8}, 
        {9, 10, 11, 12},
        {13, 14, 15, 16}
        };

        printf("Original matrix: \n");
        printm(DIM, (int*) m);

        int* mm = rotate(DIM, (int*) m);
        if (mm != NULL) {
            printf("Rotated by 90 deg matrix: \n");
            printm(DIM, (int*) mm);
            free(mm);
        }

    return 0;
}