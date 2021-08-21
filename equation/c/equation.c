#include <stdio.h>
#include <stdlib.h>

#define BUFF_SIZE 10

typedef struct Node {
    char c;
    struct Node* left;
    struct Node* right;
} node; 


int read_file(FILE* f) {
    char c;

    while (c = fgetc(f) != EOF) {
        printf("%c", c);
    }
}


int main(void) {
    char filename[] = "tree.dat";
    node root = { 'o', NULL, NULL };
    printf("Character: %c\n", root.c);

    char buff[BUFF_SIZE];
    FILE* f = fopen(filename, "r");
    if (!f) {
        fprintf(stderr, "Could not open file %s for reading\n", filename);
        exit(-1);
    }

    read_file(f);

    fclose(f);
    return 0;
}