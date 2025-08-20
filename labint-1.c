#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int n;
    printf("Enter number of elements: ");
    scanf("%d", &n);

    int arr[n];
    srand(time(0));
    for (int i = 0; i < n; i++) arr[i] = rand() % 100;

    printf("Before sorting:\n");
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);
    printf("\n");

    clock_t start = clock();

    for (int i = 1; i < n; i++) {
        int key = arr[i], j = i - 1;
        while (j >= 0 && arr[j] > key) arr[j + 1] = arr[j--];
        arr[j + 1] = key;
    }

    clock_t end = clock();

    printf("After sorting:\n");
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);
    printf("\nTime taken: %.6f seconds\n", (double)(end - start) / CLOCKS_PER_SEC);

    return 0;
}