

# class Solution:
  
#     def sortColors(self, arr: list[int]) -> None:
#       freq = {}
      
#       for num in arr:
#         freq[num] = freq.get(num, 0) + 1
        
#       freq = dict(sorted(freq.items()))
      
#       new_list = []
#       for key, value in freq.items():
#         new_list.extend(([key]*value))
        
#       return new_list

class Solution:
  
    def sortColors(self, nums: list[int]) -> None:
      
      low = 0
      mid = 0
      high = len(nums) - 1
      
      while mid <= high:
        
        if nums[mid] == 0:
          nums[low], nums[mid] = nums[mid], nums[low]
          low = low + 1
          mid = mid + 1
          
        elif nums[mid] == 1:
          mid = mid + 1
          
        else:
          nums[mid], nums[high] = nums[high], nums[mid]
          high = high - 1
          
      return nums
    
    
arr1 = [0, 1, 1, 0, 0, 1]
arr2 = [2, 0, 1, 2, 2, 1, 0, 2, 0, 1]

# [1, 0, -, -, -, -, -, -, 0, 2]

obj = Solution()
print(obj.sortColors(arr1))
print(obj.sortColors(arr2))
