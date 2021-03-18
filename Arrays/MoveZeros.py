class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero = 0
        for i in range(0,len(nums)):
            if nums[i] == 0:
                zero +=1
            else:
                nums[i-zero], nums[i] = nums[i], nums[i-zero]
        return nums
