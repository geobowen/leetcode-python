class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1 = len(word1)
        n2 = len(word2)
        n = min(n1, n2)
        res = ""
        for i in range(n):
            res = res + word1[i] + word2[i]

        ex1 = word1[n:]
        ex2 = word2[n:]

        res = res + ex1 + ex2
        return res
