class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            pref = strs[0][i]
            for words in strs[1:]:
                if i == len(words) or words[i] != pref:
                    return strs[0][:i]
        return strs[0]



