class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap_s = {}
        for l in s:
            if l in hashmap_s.keys():
                hashmap_s[l] = hashmap_s[l] + 1
            else:
                hashmap_s[l] = 1
        
        hashmap_t = {}
        for l in t:
            if l in hashmap_t.keys():
                hashmap_t[l] = hashmap_t[l] + 1
            else:
                hashmap_t[l] = 1

        return hashmap_s == hashmap_t
        
