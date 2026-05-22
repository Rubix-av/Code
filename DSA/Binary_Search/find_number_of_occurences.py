
class Solution:
  def first_and_last(self, nums: list[int], k: int):
    
    first_occur = -1
    last_occur = -1
    
    prev_start = 0
    prev_end = len(nums) - 1
    
    start = 0
    end = len(nums) - 1
    
    # Finding first occurence
    while start <= end:
      
      mid = (start + end)//2
      
      if nums[mid] == k:
        first_occur = mid
        start = prev_start
        end = mid - 1
        
      elif nums[mid] < k:
        start = mid + 1
        prev_start = mid
        
      else:
        end = mid - 1
        
    # Finding last occurence
    start = first_occur
    end = len(nums) - 1

    while start <= end:
      
      mid = (start + end)//2
      
      if nums[mid] == k:
        last_occur = mid
        end = prev_end
        start = mid + 1
        
      elif nums[mid] < k:
        start = mid + 1
        
      else:
        end = mid - 1
        prev_end = mid
        
    return last_occur-first_occur+1
  

arr2 = [0, 0, 1, 1, 2, 2, 2, 2]
obj = Solution()
print(obj.first_and_last(arr2, k=2))
  