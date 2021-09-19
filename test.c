#include<stdio.h>
int main(){
    int a[3]={1,2,3};
    int *p=a;
    printf("%p %p",p,a);
    return 0;
}