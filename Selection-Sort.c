#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int n, a[100];
    printf("Enter number of elements: ");
    scanf("%d", &n);

    srand(time(0));
    for (int i = 0; i < n; i++) a[i] = rand() % 100;

    printf("Unsorted:\n");
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");

    clock_t start = clock();
    for (int i = 0; i < n - 1; i++) {
        int min = i;
        for (int j = i + 1; j < n; j++)
            if (a[j] < a[min]) min = j;
        int t = a[i]; a[i] = a[min]; a[min] = t;
    }
    clock_t end = clock();

    printf("Sorted:\n");
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\nTime: %.6f sec\n", (double)(end - start) / CLOCKS_PER_SEC);
    return 0;
}