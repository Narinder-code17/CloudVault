#include <stdio.h>
#include <time.h>

int main() {
    int v, i, j;
    printf("Enter the number of vertices: ");
    scanf("%d", &v);

    int w[v][v], selected[v], edges = 0, sum = 0;
    printf("Enter the weights (use 0 for no edge):\n");
    for (i = 0; i < v; i++)
        for (j = 0; j < v; j++)
            scanf("%d", &w[i][j]);

    for (i = 0; i < v; i++) selected[i] = 0;
    selected[0] = 1;

    clock_t start = clock();

    printf("\nEdges in the Minimum Spanning Tree:\n");
    while (edges < v - 1) {
        int min = 9999, u = -1, v_index = -1;
        for (i = 0; i < v; i++)
            if (selected[i])
                for (j = 0; j < v; j++)
                    if (!selected[j] && w[i][j] && w[i][j] < min)
                        min = w[i][j], u = i, v_index = j;

        selected[v_index] = 1;
        printf("Edge %d - %d, weight = %d\n", u, v_index, min);
        sum += min;
        edges++;
    }

    clock_t end = clock();
    printf("Total weight of MST: %d\n", sum);
    printf("Time taken: %.6f seconds\n", (double)(end - start) / CLOCKS_PER_SEC);
    return 0;
}
