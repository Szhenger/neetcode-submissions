class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Base case: s1.length > s2.length
        if len(s1) > len(s2): return False
        # Get the characterization of all permutations of s1
        perm = Counter(s1)
        # Maintain the frequency of a sliding window in s2
        freq = Counter("")
        # Sliding window technique
        left = 0
        for right in range(len(s2)):
            # Case 1: s2[right] in Counter(s1)
            if s2[right] in perm:
                freq[s2[right]] += 1
                while left <= right and perm[s2[right]] < freq[s2[right]]:
                    freq[s2[left]] -= 1
                    left += 1
            # Case 2: s2[right] not in Counter(s1)
            else:
                while left <= right:
                    if s2[left] in freq:
                        freq[s2[left]] -= 1
                    left += 1
            # Verify Counter(s1) equals Counter(s2[left : right + 1])
            if perm == freq:
                return True
        return False 
