class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Short-circuit 
        if len(s) != len(t):
            return False
        # Get the lowercase English alphabet
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        # Iterate over the English alphabet
        for letter in alphabet:
            # Short-circuit
            if s.count(letter) != t.count(letter):
                return False
        return True
        