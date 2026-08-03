#include <stdio.h>
#include <math.h>

int main()
{
    int n, i, index = -1;

    float arr[100], key;

    printf("ASISH DIXIT\n2430021\n");

    printf("Enter the number of elements: ");
    scanf("%d", &n);

    printf("Enter the array elements:\n");

    for(i = 0; i < n; i++)
    {
        scanf("%f", &arr[i]);
    }

    printf("Enter the element to search: ");
    scanf("%f", &key);

    for(i = 0; i < n; i++)
    {
        if(fabs(arr[i] - key) < 0.001)
        {
            index = i;
            break;
        }
    }

    if(index != -1)
        printf("Element found at index = %d\n", index);
    else
        printf("Element not found\n");

    return 0;
}