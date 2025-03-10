class Solution(object):
    def twoSum(self, nums, k):
        possivel_combinação = {}
        for indice, x in enumerate(nums):
            if x in possivel_combinação:
                return [possivel_combinação[x], indice]
            
            if k - x > 0:
                possivel_combinação[k - x] = indice                
            
a = Solution()

print(a.twoSum([2,7,11,15], 9))

        