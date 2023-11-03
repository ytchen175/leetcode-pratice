class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        longest_word = ''

        for word in d:
            i , j = 0, 0
            while i < len(word) and j < len(s):
                if word[i] == s[j]:
                    i+=1
                    j+=1
                else:
                    j+=1
            if i == len(word):
                if len(longest_word) < len(word):
                    longest_word = word
                elif len(word) == len(longest_word):
                    longest_word = min(longest_word , word)
        return longest_word