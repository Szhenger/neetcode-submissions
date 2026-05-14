class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for letter in alphabet:
            if s.count(letter) != t.count(letter):
                return False
        return True