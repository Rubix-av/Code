
arr1 = [1, 1, 2, 3]
arr2 = [3, 4]

# Solution-1

# class Solution:
  # """
  # Iterate through sets of both the arrays separately, and increment the count frequency in dictionary.
  # Check for keys with value >1 in dictionary and append those keys to "commons" list
  # Lastly, if list is empty, return -1 else return the list
  # """
  # def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
  #   commons = []
  #   freq = {}
    
  #   for num in set(nums1):
  #     freq[num] = freq.get(num, 0) + 1
      
  #   for num in set(nums2):
  #     freq[num] = freq.get(num, 0) + 1
    
  #   for key, value in freq.items():
  #     if value > 1:
  #       commons.append(key)
        
  #   return (-1 if commons == [] else commons)

# Solution-2
class Solution:
  def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
    """
    Maintain two pointers for both the arrays. Compare the values at each index and add to commons if equal.
    Start at 0th index of both arrays, compare them, if equal, add to array, if not equal, then increment the index
    pointer by 1 for array having the lesser value.
    Repeat till the end
    """
    
    # nums1 = [1, 4, 5]
    # nums2 = [3, 4, 5]
    nums1.sort()
    nums2.sort()
    
    common = []
    i = 0
    j = 0

    while i < len(nums1) and j < len(nums2):
      if nums1[i] == nums2[j]:
        common.append(nums1[i])
        i += 1
        j += 1
      
      elif nums1[i] < nums2[j]:
        i += 1
      
      elif nums1[i] > nums2[j]:
        j += 1
        
    return common

# arr1 = [1, 4, 5]
# arr2 = [3, 4, 5]
arr1 = [4,9,5]
arr2 = [9,4,9,8,4]

obj = Solution()
print(obj.intersection(arr1, arr2))
