class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            '2' : "abc", '3' : "def", '4' : "ghi",
            '5' : "jkl", '6' : "mno", '7' : "pqrs",
            '8' : "tuv", '9' : "wxyz"
        }
        combos = []
        def backtrack(index: int, combo: List[str]) -> None:
            if index >= len(digits):
                if combo:
                    combos.append("".join(combo))
            else:
                for letter in letters[digits[index]]:
                    combo.append(letter)
                    backtrack(index + 1, combo)
                    combo.pop()
        backtrack(0, [])
        return combos