#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n[3] = {56,57 ,58};
    int (*p)[3];
    p = &n;
    printf("%p\n", *p);
    printf("%p\n", &n[0]);
    for (int i = 0; i < 3; i++)
        printf("%d ", n[i]);
    putchar('\n');
    p++;
    printf("%p\n", p);
    return (0);
    
}
