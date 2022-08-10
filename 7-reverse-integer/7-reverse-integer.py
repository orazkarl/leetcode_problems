class Solution:
    def reverse(self, x: int) -> int:
        num = int(str(x)[::-1].replace('-', '')) * (-1 if x < 0 else 1)
        return num if -2 ** 31 <= num <= 2 ** 31 else 0