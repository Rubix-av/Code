
arr = [1, 2, 3, 4, 5]
k = 5

class Solution:
  def pair_sum(self, nums: list[int], k: int):
    
    pairs = []
    
    for i in range(len(arr)):
      diff = k - nums[i]
      
      for j in range(i+1, len(arr)):
        
        if diff == nums[j]:
          pairs.append([nums[i], nums[j]])
          
    # pairs.sort(key = lambda x: x[0])
    return sorted(pairs, key = lambda x: x[0])
      
    

arr = [2, -3, 3, 3, -2]
k = 0

obj = Solution()

print(obj.pair_sum(arr, k))
