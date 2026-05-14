class Solution:

    def encode(self, strs: List[str]) -> str:
        # Get an empty list of strings
        encoded = []
        # Encode the input list of strings
        for s in strs:
            encoded.append(f"{len(s)}#{s}")
        # Return the encoded string
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        # Get an empty list of strings
        decoded = []
        # Decode the input string
        i = 0
        while i < len(s):
            j = i
            # Find the hash delimiter
            while s[j] != '#':
                j += 1
            # Compute the prepended length
            length = int(s[i:j])
            # Compute the appended string
            decoded.append(s[j + 1:j + length + 1])
            # Update to find next word
            i = j + 1 + length
        return decoded

        