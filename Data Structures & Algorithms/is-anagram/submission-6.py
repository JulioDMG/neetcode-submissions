
from collections import Counter
class Solution:
    def isAnagram(self,s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)

sol = Solution()
print(sol.isAnagram("fish","shif")) #counter counts how many time a each item appears in a word and retruns a dictionary
#For a class you have to create an instance and from that instance you gotta call any function inside the class

#print(Solution.isAnagram(Solution,"fish","shief")) #self means the current object used (always first parameter of the calss)