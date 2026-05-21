
class Solution:
  
  def remove_duplicates(self, dup_list: list[list[int]]) -> list[list[int]]:
    
    unique = []
    seen = set()
    
    for sub in dup_list:
      key = tuple(sorted(sub))
      
      if key not in seen:
        seen.add(key)
        unique.append(sub)
        
    return unique
  
  def threeSum(self, nums: list[int], k=0) -> list[list[int]]:    
    triplets = []
    for i in range(len(nums)):
      
      m = i+1
      n = i+2
      
      while m < len(nums)-1 and n < len(nums):
        if nums[i] + nums[m] + nums[n] == k:
          triplets.append([nums[i], nums[m], nums[n]])
          
          if n == len(nums) - 1:
            m += 1
            n = m + 1
          else:
            n += 1
        
        elif n != len(nums)-1:
          n += 1
        
        else:
          m += 1
          n = m+1
          
    return self.remove_duplicates(triplets)
          
# arr = [1, 2, 3, 4, 5]
# k = 12

# arr = [-1,0,1,2,-1,-4]
arr = [-2,0,1,1,2]

obj = Solution()
print(obj.threeSum(arr))
