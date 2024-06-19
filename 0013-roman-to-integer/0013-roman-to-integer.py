class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        total = 0
        prev = 0

        for i in s[::-1]:
            value = roman_to_int[i]

            if value < prev:
                total = total - value

            else:
                total = total + value

            prev = value

        return total
