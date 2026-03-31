class Solution:

    def encode(self, strs: List[str]) -> str:
        s  = ""
        def counter(string):
            return len(string)
        for i in strs:
            s+=str(counter(i))+"#"+i
        return s

    def decode(self, s: str) -> List[str]:
        l =[]
        i = 0
        while(i<len(s)):
            j = i
            while s[j]!="#":
                j+=1
            leng = int(s[i:j])
            l.append(s[j+1:j+1+leng])
            i=j+1+leng
        return l
