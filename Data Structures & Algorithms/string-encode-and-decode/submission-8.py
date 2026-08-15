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
        # Get an empty Python list of strings
        decoded = []
        # Decode the input Python string
        i = 0
        while i < len(s):
            j = i
            # Search for hash delimiter
            while s[j] != '#': j += 1
            # Extract the prepended length
            length = int(s[i : j])
            # Extract the appended string
            decoded.append(s[j + 1 : j + 1 + length])
            # Update the pointer
            i = j + 1 + length
        # Return the decoded strings
        return decoded


