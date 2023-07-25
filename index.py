def find_mode(nums):
  """
  Finds the mode of the given array.

  Args:
    nums: The array to find the mode of.

  Returns:
    The mode of the array.
  """

  # Create a dictionary to store the number of times each element appears in the array.
  counts = {}
  for num in nums:
    if num not in counts:
      counts[num] = 0
    counts[num] += 1

  # Find the element with the maximum count.
  max_count = 0
  mode = None
  for num, count in counts.items():
    if count > max_count:
      max_count = count
      mode = num

  return mode


if __name__ == "__main__":
  # Test cases
  nums1 = [3, 3, 5, 1]
  assert find_mode(nums1) == 3

  nums2 = [4, 2, 4, 5, 4, 1]
  assert find_mode(nums2) == 4

  print("All tests passed!")
