class Solution:
    def isPalindrome(self, s: str) -> bool:
        y=0
        found=True
        for i in range(len(s)-1,-1,-1):
            if s[i].isalnum()==False:
                continue
            if s[y].isalnum()==False:
                continue
            if s[i].lower()==s[y].lower():
                y+=1
            else: 
                found=False
        return found
            