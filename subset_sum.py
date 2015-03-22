# subsetsum
# Benjamin Carroll
# 2/6/15

import unittest

# Test lists:
TEST_LIST = [2, 5, 6, 6]
TEST_LIST1 = [3, 4, 2, 9, 11]

# Define the subset sum function. This function will check to see if there
# is a possible combination of a given list that adds up to a target number


def subset_sum(ropes, target, test_sum=[]):
    # Get the sum of the legths of rope
    s = sum(test_sum)

    # Check if the test sum is equals to target. If it does then return True.
    if s == target:
        return True

    # Go through each length of rope in the list and then make a recursive
    # call of subset_sum. If the subset_sum returns True, then return True.
    for i, rope in enumerate(ropes):
        remaining = ropes[i+1:]
        if subset_sum(remaining, target, test_sum + [rope]):
            return True

    # If there are no possible combinations for the target, then return False.
    return False

# Make a class for the tests using "unittest.TestCase"


class DrRopesTest(unittest.TestCase):
    # Various tests with the sample list. What each test does is that it
    # passes a list through the "subset_sum" function and checks its
    # return value
    def test_basic(self):
        result = subset_sum(TEST_LIST, 7)
        self.assertEqual(result, True)

    def test_basic1(self):
        result = subset_sum(TEST_LIST, 15)
        self.assertEqual(result, False)

    def test_basic2(self):
        result = subset_sum(TEST_LIST, 12)
        self.assertEqual(result, True)

    # Tests with a different list. Because of the size of
    # this list the outcome of "subset_sum" remains predictable.
    def test_basic3(self):
        result = subset_sum(TEST_LIST1, 30)
        self.assertEqual(result, False)

    def test_basic4(self):
        result = subset_sum(TEST_LIST, 11)
        self.assertEqual(result, True)

# If the tests were to be in another module,
# "if __name__ == '__main__':" would be nessesary
unittest.main()
