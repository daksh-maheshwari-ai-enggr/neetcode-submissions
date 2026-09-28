class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict={}
        for i in range(len(nums)):
            dict[nums[i]]=dict.get(nums[i],0)+1

        for val in dict.values():
            if val>1:
                return True
        return False

        