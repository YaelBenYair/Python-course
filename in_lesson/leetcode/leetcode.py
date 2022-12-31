

# https://leetcode.com/problems/robot-return-to-origin/

# def moove(moves: str):
#     sum_u = moves.count("U")
#     sum_d = moves.count("D")
#     sum_r = moves.count("R")
#     sum_l = moves.count("L")
#
#     if sum_u == sum_d and sum_l == sum_r:
#         return True
#     return False
#
# m = "ULL"
# print(moove(m))


# ------------------------------------------------------------------------------------

# https://leetcode.com/problems/longest-common-prefix/

# def longestCommonPrefix(strs) -> str:
#     comb_l = ""
#     word_short = min(strs, key=len)
#     for i in range(len(word_short)):
#         comb = set(map(lambda s: s[:i+1], strs))
#         if len(comb) == 1:
#             comb_l = "".join(comb)
#     return comb_l

# def longestCommonPrefix(strs) -> str:
#     comb_l = ""
#     count = 0
#     word_short = min(strs, key=len)
#     for i in range(len(word_short)):
#         comb = word_short[:i+1]
#         for j in strs:
#             if comb == j[:i+1]:
#                 count +=1
#         if len(strs) == count:
#             comb_l = comb
#         count = 0
#
#     return comb_l
#
#
# strs = ["flower","flow","flight"]
# print(longestCommonPrefix(strs))

# s = "flower"
# print(s[:0])


# ----------------------------------------------------------------------------------------------------------------------
# https://leetcode.com/problems/can-place-flowers/

# def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
#     count = 0
#     len_flo = len(flowerbed)
#     if n > len_flo:
#         return False
#     if len_flo == 1:
#         if flowerbed[0] == 0:
#             return True
#         elif n == 0:
#             return True
#         else:
#             return False
#
#     for inx, num in enumerate(flowerbed):
#         if inx == 0 and num == 0 and flowerbed[inx + 1] == 0:
#             flowerbed[inx] = 1
#             count += 1
#         elif inx == len_flo-1 and num == 0 and flowerbed[inx - 1] == 0:
#             flowerbed[inx] = 1
#             count += 1
#         elif num == 0 and flowerbed[inx - 1] == 0 and flowerbed[inx + 1] == 0:
#             flowerbed[inx] = 1
#             count += 1
#     if n <= count:
#         return True
#     return False

# def canPlaceFlowers(A, N):
#     for i, x in enumerate(A):
#         if (not x and (i == 0 or A[i-1] == 0)
#                 and (i == len(A)-1 or A[i+1] == 0)):
#             N -= 1
#             A[i] = 1
#     return N <= 0


# 2-1 end and start

# 3-2=1 3%2 = 1
# 4-3=1 4%3 = 1
# 5-3=2
# 6-4=2
# 7-4=3
# 8-5=3
# 1010101


# flowerbed = [1,0,0,0,0,1]
# flowerbed = [0, 0, 1, 0, 0, 0, 1, 0, 1]
# flowerbed = [1, 0, 0, 0, 1, 0, 0]
# flowerbed = [1]
# n = 0
# print(canPlaceFlowers(flowerbed, n))


# ----------------------------------------------------------------------------------------------------------------------
# https://leetcode.com/problems/reshape-the-matrix/

# def matrixReshape(mat: list[list[int]], r: int, c: int) -> list[list[int]]:
#     new_mat = []
#     row = []
#     count = 0
#     if len(mat) * len(mat[0]) != r * c:
#         return mat
#
#     for i in range(len(mat)):
#         for j in range(len(mat[0])):
#             row.append(mat[i][j])
#             count += 1
#             if count == c:
#                 new_mat.append(row)
#                 row = []
#                 count = 0
#
#     return new_mat
#
#
# mat = [[1, 2], [3, 4]]
# print(matrixReshape(mat, 4, 1))
# mat2 = [mat[0]+mat[-1]]
# print(mat2)
# print(len(mat))
# print(len(mat[0]))



# ----------------------------------------------------------------------------------------------------

# https://leetcode.com/problems/count-binary-substrings/description/

# def nu(s: str):
#     count_1 = 0
#     count_0 = 0
#     char = s[0]
#     substrings = 0
#     if len(s) < 2 or s == (s[0] * len(s)):
#         return 0
#     for inx, i in enumerate(s):
#         if char == i:
#             count_0 += 1
#         else:
#             count_1 += 1
#         if inx != 0 and count_1 > 0 and char == i and char != s[inx - 1]:
#             count_0 -= 1
#             substrings += min(count_1, count_0)
#             count_0 = count_1
#             count_1 = 1
#             char = s[inx - 1]
#
#     substrings += min(count_1, count_0)
#
#     return substrings




# s = "00110011" # 6
# s = "10101" # 4
# s = "111001" # 3
# s = "010010100100"
# p = nu(s)
# print(p)


# ----------------------------------------------------------------------------------------------------------------------

# https://leetcode.com/problems/set-mismatch/


# def nn(nums):
#     dup = sum(nums) - sum(set(nums))
#     miss = sum(range(1, len(nums)+1)) - sum(set(nums))
    # if dup == len(nums):
    #     return [dup, dup - 1]
    # elif dup - 1 not in nums and dup != 1:
    #     return [dup, dup -1]
    # else:
    #     return [dup, dup + 1]

    # for i in range(1, len(nums)+1):
    #     if i not in nums:
    #         return [sum(nums)-sum(set(nums)), i]
    # return [dup, miss]





# nums = [1, 2, 2, 4]
# nums = [1, 1, 3, 4]
# nums = [1, 1]
# nums = [1, 2, 3, 3]
# nums = [4, 4, 2, 1]
# nums = [3,2,2]
# print(nn(nums))


# ----------------------------------------------------------------------------------------------------------------------

# https://leetcode.com/problems/student-attendance-record-i/submissions/868724365/

# def checkRecord(s: str) -> bool:
#     char = s[0]
#     count = 0
#     if s.count('A') >= 2:
#         return False
#     for l in s:
#         if char == l:
#             count += 1
#         else:
#             if char == 'L' and count >= 3:
#                 return False
#             else:
#                 char = l
#                 count = 1
#     if char == 'L' and count >= 3:
#         return False
#     return True

# def checkRecord(s: str) -> bool:
#     count = 0
#     start = s.find('L')
#     char = s[start]
#
#     if s.count('A') >= 2:
#         return False
#     if start == -1:
#         return True
#     else:
#         for i in range(start, len(s)):
#             if char == s[i]:
#                 count += 1
#             else:
#                 if char == 'L' and count >= 3:
#                     return False
#                 else:
#                     char = s[i]
#                     count = 1
#         if char == 'L' and count >= 3:
#             return False
#         return True

# def checkRecord(s: str) -> bool:
#     if s.count('A') >= 2 or 'LLL' in s:
#         return False
#     return True


# s = "PPALLP"
# s = "PPALLL"
# print(checkRecord(s))


# ----------------------------------------------------------------------------------------------------------------------

# https://leetcode.com/problems/detect-capital/

import re
def detectCapitalUse(word: str) -> bool:
    if word.islower():
        return True
    elif word.isupper():
        return True
    elif re.match("[A-Z][a-z]+$", word) is not None:
        return True
    else:
        return False



w = 'GooglE'
print(detectCapitalUse(w))


















