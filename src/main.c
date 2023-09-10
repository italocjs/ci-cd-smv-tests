//include stdio, average.h

#include <stdio.h>
#include "average.h"

int main()
{
    float arr[] = {3, 7, 3, 6, 5};
    float avg = average(arr, 5);
    printf("Average: %f\n", avg);
    return 0;
}