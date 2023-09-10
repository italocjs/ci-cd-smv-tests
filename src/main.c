//include stdio, average.h

#include <stdio.h>
#include "average.h"

int main()
{
    float arr[] = {1, 2, 3, 4, 5};
    float avg = average(arr, 5);
    printf("Average: %f\n", avg);
    return 0;
}