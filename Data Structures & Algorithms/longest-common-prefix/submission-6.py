class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])): #first we use the first word as a guide | Note: range needs a number and len returns a number
            char = strs[0][i] #store the characters of the first word

            for word in strs[1:]: #we check for the rest of the words in the list
                if i == len(word) or word[i] != char: #check if the 1st word is over or if the rest of the word differs
                    return strs[0][:i] #return the first string up to a point before i

        return strs[0] #means that the first string is the most common prefix


