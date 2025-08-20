#include<stdio.h>
#include<stdlib.h>
#include<time.h>
void main()
{
    int a[6000],n,i,j,key;
    clock_t start,end;
    printf("enter the numbers of elements:");
    scanf("%d",&n);
    for(i=0;i<n;i++){
        a[i]=rand()%1000;
        start=clock();
        }
        for(i=1;i<n;i++){
            key=a[i];
            j=i-1;
            while(j>=0&&a[j]>key){
                a[j+1]=a[j];
                j--;
            }
        a[j+1]=key;
        }
        end=clock();
        double t=((double)(end-start))/CLOCKS_PER_SEC;
        printf("time is %f sec",t);
}