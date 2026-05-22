
class Solution:
  
  def peakIndexInMountainArray(self, nums: list[int]) -> int:
    
    start = 0
    end = len(nums) - 1
    peak = -1
    
    while start <= end:
      
      mid = (start + end) // 2
      
      if nums[mid-1] < nums[mid] > nums[mid+1]:
        peak = mid
        break
      
      elif nums[mid] < nums[mid+1]:
        start = mid + 1
        
      else:
        end = mid - 1

    return peak
  
arr1 = [0, 5, 10, 2]
arr2 = [0, 10, 5, 2]
arr3 = [0, 2, 1, 0]
arr4 = [3, 4, 5, 1]

obj = Solution()
print(obj.find_peak(arr1))
print(obj.find_peak(arr2))
print(obj.find_peak(arr3))
print(obj.find_peak(arr4))
