class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(0,len(nums)):
            res=0
            while(nums[i]>0):
                res+=int(nums[i]%10)
                nums[i]=int(nums[i]/10)
            nums[i]=res
        nums=sorted(nums)
        return nums[0]

        