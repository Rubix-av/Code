
class MountainArray:
  
  def get(self, index: int) -> int:
    return 

class Solution:

    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:

        n = mountainArr.length()

        # Find peak
        start = 0
        end = n - 1

        while start < end:

            mid = (start + end) // 2

            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                start = mid + 1
            else:
                end = mid

        peak = start

        # Binary search on ascending part
        start = 0
        end = peak

        while start <= end:

            mid = (start + end) // 2
            val = mountainArr.get(mid)

            if val == target:
                return mid

            elif val < target:
                start = mid + 1

            else:
                end = mid - 1

        # Binary search on descending part
        start = peak + 1
        end = n - 1

        while start <= end:

            mid = (start + end) // 2
            val = mountainArr.get(mid)

            if val == target:
                return mid

            elif val < target:
                end = mid - 1

            else:
                start = mid + 1

        return -1