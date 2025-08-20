#include <stdio.h>

void sort(int p[], int w[], float r[], int n) {
    for (int i = 1; i < n; i++)
        for (int j = 0; j < n - i; j++)
            if (r[j] < r[j + 1]) {
            float tr = r[j];
                r[j] = r[j + 1];
                r[j + 1] = tr;
        int tp = p[j]; 
           p[j] = p[j + 1];  
           p[j + 1] = tp;
       int tw = w[j];
          w[j] = w[j + 1];  
          w[j + 1] = tw;
            }
}

float knapsack(int M, int p[], int w[], int n) {
    float profit = 0;
    for (int i = 0; i < n && M > 0; i++) {
        if (w[i] <= M) profit += p[i], M -= w[i];
        else profit += p[i] * ((float)M / w[i]), M = 0;
    }
    return profit;
}

int main() {
    int n, M, p[100], w[100];
    float r[100];

    printf("Enter max weight and number of items: ");
    scanf("%d %d", &M, &n);

    printf("Enter weights: ");
    for (int i = 0; i < n; i++) 
    scanf("%d", &w[i]);

    printf("Enter profits: ");
    for (int i = 0; i < n; i++) {
        scanf("%d", &p[i]);
        r[i] = (float)p[i] / w[i];
    }

    sort(p, w, r, n);
    printf("Maximum profit: %.2f\n", knapsack(M, p, w, n));
    return 0;
}
        