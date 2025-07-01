from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for number in nums:
            if(number in hashmap.keys()):
                hashmap[number] += 1
            else:
                hashmap[number] = 1
        
        array = []
        for num,count in hashmap.items():
            array.append([count,num])
        array.sort()    #dá sort pelo count de aparências 

        res = []
        while len(res) < k:
            res.append(array.pop()[1])  #retorna a combinação no topo
        return res

        
