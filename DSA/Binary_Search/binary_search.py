
class Solution:
  def binary_search(self, nums: list[int], k: int):
    
    start = 0
    end = len(nums) - 1
    
    while start <= end:
      
      mid = start + (end - start)//2
      
      if nums[mid] == k:
        return mid
      
      elif nums[mid] < k:
        start = mid + 1
        
      else:
        end = mid - 1
        
    return -1
    
    
arr = [3, 7, 11, 13, 19, 27]
k = 13

arr2 = [4, 8, 16, 22, 34]
k2 = 4

obj = Solution()
print(obj.binary_search(arr, k))
print(obj.binary_search(arr2, k2))
