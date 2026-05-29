class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cnt=0
        nums=sorted(nums)
        while(sum(nums)%k!=0):
            nums[len(nums)-1]-=1
            cnt+=1
        return cnt

        