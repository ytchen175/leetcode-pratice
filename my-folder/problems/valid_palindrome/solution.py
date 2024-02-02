class Solution:
    def isPalindrome(self, s: str) -> bool:
        preprocessed_string = ""

        s = s.lower()
        for i in s:
            if i.isalnum(): # Changed to isalnum to include alpha & numbers
                preprocessed_string += i

        if len(preprocessed_string) <= 1:
            return True
        else:
            left, right = 0, len(preprocessed_string) - 1

            while left < right:
                if preprocessed_string[left] != preprocessed_string[right]:
                    return False
                else:
                    left += 1
                    right -= 1

            return True
