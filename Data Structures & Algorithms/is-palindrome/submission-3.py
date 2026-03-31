class Solution:
    def isPalindrome(self, s: str) -> bool:
        i,j = 0,len(s)-1
        answer = True
        while(i<j):
            i_alpha = s[i].isalnum()
            j_alpha = s[j].isalnum()
            if i_alpha and j_alpha:
                answer = s[i].lower() == s[j].lower()
                i+=1
                j-=1
            elif not i_alpha:
                i+=1
            elif not j_alpha:
                j-=1
        return answer
