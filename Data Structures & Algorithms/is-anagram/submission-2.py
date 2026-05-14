class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Short-circuit if the length of s and t are unequal
        if len(s) != len(t):
            return False
        # Get the string of lowercase English letters
        alphabet = "abcdefghijklnmopqrstuvwxyz"
        # Iterate over the alphabet string
        for letter in alphabet:
            # Short-circuit if count of letters are unequal
            if s.count(letter) != t.count(letter):
                return False
        return True