from typing import List
from collections import defaultdict
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        for index,num in enumerate(numbers):
            hashmap[num] = index

        for number in numbers:
            key = target - number
            if key in hashmap.keys():
                if hashmap[number] < hashmap[key]:
                    return [hashmap[number]+1,hashmap[key]+1]
                
        return []
            

