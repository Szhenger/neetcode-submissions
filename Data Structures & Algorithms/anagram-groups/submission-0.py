class Solution:
    def groupAnagrams(self, strings: List[str]) -> List[List[str]]:
        # Get an default hashmap of empty lists
        groups = defaultdict(list) # frequency -> anagrams
        # Iterate over the strings array
        for string in strings:
            # Compute the anagram property
            frequency = [0] * 26 
            # Iterate over the string
            for letter in string:
                frequency[ord(letter) - ord('a')] += 1
            # Insert the string into the hashmap
            groups[tuple(frequency)].append(string)
        # Return the groups
        return list(groups.values()) 

