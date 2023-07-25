# N-Repeated-Element
N Repeated Element
You are given an integer array, nums, which contains 2N elements. Within nums there are N + 1 unique elements and a specific element occurs N times. Return the element within nums that appears N times. 

Ex: Given the following nums…
nums = [3, 3, 5, 1], return 3.
Ex: Given the following nums…
nums = [4, 2, 4, 5, 4, 1], return 4.


Solution
--------

This code follows the following steps to find the mode of the given array:

Create a dictionary to store the number of times each element appears in the array.
Find the element with the maximum count.
Return the element with the maximum count.
The code also includes two test cases to verify that it works correctly.

To use this code, you would first need to create an array of integers. Then, you would call the find_mode() function on the array. The function would return the element in the array that appears the most often.

For example, the following code would find the mode of the array nums = [3, 3, 5, 1]:

nums = [3, 3, 5, 1]
mode = find_mode(nums)

print(mode)

This code would print the value 3, which is the mode of the array.
