def romanToInt(s: str) -> int:
    roman_let = {'i': 1, 'v': 5, 'x': 10, 'l': 50, 'c': 100, 'd': 500, 'm': 1000}
    s = s[::-1].lower()
    sahac = 0
    for inx, i in enumerate(s):
        if inx > 0 and roman_let[i] < roman_let[s[inx-1]]:
            sahac -= roman_let[i]
        else:
            sahac += roman_let[i]

    return sahac


s = "MMCCCXCIX"
print(romanToInt(s))







def climbStairs(n: int) -> int:
    a, b = 1, 2
    for i in range(1, n):
        a, b = b, a + b
    return a



print(climbStairs(n))