from typing import List
from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        current = 0

        numset = set(nums)
        
        for n in nums:
            if n-1 not in numset:   #this marks the start of the sequence
                current = 1
                while n+current in numset:
                    current += 1

                longest = max(longest,current)
        return longest
                
            
        