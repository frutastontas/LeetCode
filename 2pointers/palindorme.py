class Solution:
    def isPalindrome(self, s: str) -> bool:
        normalized_s = ""
        for l in s:
            if not l.isalnum():
                continue
            normalized_s += l.lower()

        start = 0
        end = len(normalized_s)-1

        while start < end:
            if normalized_s[start] != normalized_s[end]:
                return False
            start += 1
            end -= 1

        return True
