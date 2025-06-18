class Solution:
    def sortColors(self, nums: list[int]) -> None:
        '''
        TC: O(3n) = 0(n)
        AS: O(1)

        '''
        count0 = nums.count(0)
        count1 = nums.count(1)
        count2 = nums.count(2)  

        for i in range(0, count0):
            nums[i] = 0

        end = count0+count1
        for i in range(count0, count0+count1):
            nums[i] = 1         

        for i in range(end, len(nums)):
            nums[i] = 2

        return nums
    

nums = [2,0,2,1,1,0]
s = Solution()
print(s.sortColors(nums))