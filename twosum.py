'''
Given an array of integers, return indices of the two number such that they add up to 
a specific target. You may assum that each input should have exactly one solution,
and you may not use the same element twice. example:
given nums = [2,7,11,15], target = 9
Because nums[0] + nums[1] = 2 +7 = 9
return [0,1]

'''
class Solution(object):
    def twoSum(self, nums, target):
        index_mapping = {}

        #go through the nums
        #acces to that number, find the second number
        #target - number, where can I store this information? in the dictionary
        #if complement is in dictionary
            #return the indicies
        #put number in the dictionary
        for i in range(len(nums)):
            curr = nums[i]
            complement = target - curr
            if complement in index_mapping:
                return [index_mapping[complement], i]
            else:
                index_mapping[curr] - 1
        