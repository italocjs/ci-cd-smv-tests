#include "CppUTest/TestHarness.h"

extern "C" {
    #include "sum.h"
}

// Create a test group
TEST_GROUP(sum_test_group)
{
    void setup()
    {
        // Initialize before each test
    }
    
    void teardown()
    {
        // Deinitialize after each test
    }
};

// Test the sum function
TEST(sum_test_group, simple_test)
{
    float result = sum(2, 5);
    CHECK_EQUAL(result, 2 + 5);
}

// Test null array
TEST(sum_test_group, null_test)
{
    float result = sum(1, 0);
    CHECK_EQUAL(result, 1);
}