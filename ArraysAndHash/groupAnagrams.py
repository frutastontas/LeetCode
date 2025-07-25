from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sortstring = sorted(s)
            sortstring = ''.join(sortstring)
            res[sortstring].append(s)
        return list(res.values())


