class Solution:
    def Is_Palindrome(self,s,left,right):
        while left<right:
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True
    def validPalindrome(self, s: str) -> bool:
        l,r = 0,len(s)-1
        while(l<r):
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                return(
                    self.Is_Palindrome(s,l+1,r)
                    or
                    self.Is_Palindrome(s,l,r-1)
                )
        return True