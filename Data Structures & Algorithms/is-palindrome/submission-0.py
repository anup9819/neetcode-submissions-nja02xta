class Solution:
    def isPalindrome(self, s: str) -> bool:
        org = []
        for i in s:
            if i.isalnum():
                org.append(i.lower())
        return org[::1] == org[::-1]