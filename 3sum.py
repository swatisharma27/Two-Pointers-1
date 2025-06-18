class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        TC: O(N log N) + O(N^2) = O(N^2)
        AS: O(1)
        """

        # sort the list 
        nums.sort() # O(1) search > in-place
        
        N = len(nums)
        result = []

        # to ensure there are low and high pointer at the end
        for i in range(0, N-2):

            if i != 0 and nums[i] == nums[i-1]:
                continue

            low = i + 1
            high = N - 1
                
            while low < high:

                three_sum = nums[i] + nums[low] + nums[high]

                if three_sum == 0:
                    result.append([nums[i], nums[low], nums[high]])
                    low += 1
                    high -= 1
                    while (low < high and nums[low] == nums[low-1]):
                        low +=1
                    while (low < high and nums[high] == nums[high +1]):
                        high -= 1

                elif three_sum > 0:
                    high -= 1
                else:
                    low += 1

        return result