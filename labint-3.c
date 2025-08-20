#include <stdio.h>
#include <time.h>

void quickSort(int a[], int low, int high) {
    if (low >= high) return;
    int pivot = a[high], i = low - 1;
    for (int j = low; j < high; j++)
      if (a[j] < pivot) {
        int t = a[++i]; 
            a[i] = a[j]; 
            a[j] = t;
        }
    int t = a[i + 1]; 
        a[i + 1] = a[high]; 
        a[high] = t;
    quickSort(a, low, i);
    quickSort(a, i + 2, high);
}

int main() {
    int n, a[100];
    printf("Enter number of elements: ");
    scanf("%d", &n);

    printf("Enter elements: ");
    for (int i = 0; i < n; i++) 
    scanf("%d", &a[i]);

    clock_t start = clock();
    quickSort(a, 0, n - 1);
    clock_t end = clock();

    printf("Sorted array: ");
    for (int i = 0; i < n; i++) 
    printf("%d ", a[i]);
    printf("\n");

    double time_taken = (double)(end - start) / CLOCKS_PER_SEC;
    printf("Time taken for sorting: %.6f seconds\n", time_taken);

    return 0;
}