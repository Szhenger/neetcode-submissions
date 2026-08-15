class Solution:

    def encode(self, strs: List[str]) -> str:
        # Get an empty Python list of strs
        encoded = []
        # Encode the input Python list of strs
        for s in strs:
            encoded.append(f"{len(s)}#{s}")
        # Return the encoded string
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        # Get an empty Python list of strs
        decoded = []
        # Decode the input Python str
        i = 0
        while i < len(s):
            # Search for delimiter
            j = i
            while s[j] != '#':
                j += 1
            # Extract the length and string
            length = int(s[i:j])
            decoded.append(s[j+1:j+1+length])
            # Update the pointer
            i = j + 1 + length
        # Return the decoded strings
        return decoded


