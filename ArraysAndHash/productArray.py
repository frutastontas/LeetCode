from typing import List
from collections import defaultdict

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, count_zeros =1,0 #important to count the existence of zeros and the product of the whole array
        for num in nums:
            if num:
                prod *= num
            else:
                count_zeros+=1
            
        res = [0]*len(nums) 
        if count_zeros > 1:
            return res
        for index,value in enumerate(nums):
            if count_zeros:
                if value:
                    res[index]=0
                else:
                    res[index] = prod   #it means my value is the zero here
            else:
                res[index]= prod//value #the product without considering my current value

        return res

