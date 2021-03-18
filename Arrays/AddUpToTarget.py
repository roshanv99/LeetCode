#Find 2 numbers in the list whose sum is equal to the target value

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i, num in enumerate(nums):
            if (target-num) in nums[i+1:]:
                print(nums[i+1:])
                return [i, nums.index(target-num,i+1)]
        return []        
      
      
      #OR
      
      
      def twoSum(self, num, target):
        map = {}
        for i in range(len(num)):
            if num[i] not in map:
                map[target - num[i]] = i + 1
            else:
                return map[num[i]], i + 1

        return -1, -1
