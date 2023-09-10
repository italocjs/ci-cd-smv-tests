#include "average.h"

float average(float array[], int size)
{
    float sum = 0;
    for (int i = 0; i < size; i++)
    {
        sum += array[i]; // sum = sum + arr[i]
    }
    return sum / size;
}