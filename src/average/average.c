#include "average.h"

float average(float array[], unsigned int size)
{
    if (size == 0) //check for errors, example null array
    {
        return 0.0;
    }

    float sum = 0;
    for (unsigned int i = 0; i < size; i++)
    {
        sum += array[i]; // sum = sum + arr[i]
    }
    return sum / (float)size;
}