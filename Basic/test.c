#include <stdio.h>
int main()
{
    int n;
    scanf("%d", &n);
rifat:
    printf("%d ", n);
    n++;
    if (n <= 10)
    {
        goto rifat;
    }
    return 0;
}