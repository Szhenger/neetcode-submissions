class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Edge case
        if len(s) != len(t):
            return False
        # Iterate over the lowercase alphabet
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for letter in alphabet:
            # Count matching instances of letters
            if s.count(letter) != t.count(letter):
                return False
        # Instances of all letters match
        return True