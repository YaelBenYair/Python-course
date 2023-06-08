

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

# import re
# def detectCapitalUse(word: str) -> bool:
#     if word.islower():
#         return True
#     elif word.isupper():
#         return True
#     elif re.match("[A-Z][a-z]+$", word) is not None:
#         return True
#     else:
#         return False
#
#
#
# w = 'GooglE'
# print(detectCapitalUse(w))


# class Solution:
#
#
#     # def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
#     #     reach_time = arrivalTime + delayedTime
#     #     if reach_time == 24:
#     #         return 0
#     #     return reach_time if reach_time <= 24 else reach_time % 24
#
#     def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
#         reach_time = arrivalTime + delayedTime
#         return reach_time if reach_time < 24 else reach_time % 24
#
# if __name__ == '__main__':
#     a_time = Solution()
#     print(a_time.findDelayedArrivalTime(15, 5))
#     print(a_time.findDelayedArrivalTime(13, 11))
#     print(a_time.findDelayedArrivalTime(15, 12))
#     print(a_time.findDelayedArrivalTime(1, 1))
#     print(a_time.findDelayedArrivalTime(20, 4))


class Solution:
    def isWinner(self, player1: list[int], player2: list[int]) -> int:
        count_10_p1 = 0
        count_10_p2 = 0
        p1 = 0
        p2 = 0
        for i in range(len(player1)):
            if 0 < count_10_p1:
                p1 += player1[i] * 2
                count_10_p1 -= 1
            else:
                p1 += player1[i]
            if 0 < count_10_p2:
                p2 += player2[i] * 2
                count_10_p2 -= 1
            else:
                p2 += player2[i]

            if player1[i] == 10:
                count_10_p1 = 2

            if player2[i] == 10:
                count_10_p2 = 2

        print(f'p1: {p1}')
        print(f'p2: {p2}')
        if p1 == p2:
            return 0
        return 1 if p1 > p2 else 2

    def isValid(self, s: str) -> bool:
        mark = {
            '{': 3,
            '}': -3,
            '(': 1,
            ')': -1,
            '[': 2,
            ']': -2,
        }
        count = 0
        for inx, i in enumerate(s):
            count += mark[i]
            if inx % 2 == 0 and count < 0:
                return False
            elif inx % 2 != 0 and count != 0:
                return False
        return True
        pass


if __name__ == '__main__':
    a_time = Solution()
    # print(a_time.isValid("()"))
    # print(a_time.isValid("()[]{}"))
    # print(a_time.isValid("(]"))
    # print(a_time.isValid("][]"))
    # print(a_time.isValid("{[]}"))
    # print(a_time.isWinner([4,10,7,9], [6,5,2,3]))
    # print(a_time.isWinner([3,5,7,6], [8,10,10,2]))
    # print(a_time.isWinner([2,3], [4,1]))
    # print(a_time.isWinner([0,2,6,0,6,1,1,6,4,2,8,4,2,6,3,3,3,4,6,2,6,0,5,4,4,5,7,8,6,6,1,5,7,10,3,6,2,0,2,1,4,10,8,8,8,6,7,8,7,6,9,7,4,6,6,10,9,9,2,7,7,7,4,2,0,1,4,5,1,5,3,6,6,0,7,7,8,7,5,5,6,7,5,4,7,9,5,1,9,8,4,7,7,0,4,1,0,3,2,3,8,2,6,0,1,9,7,2,2,4,8,7,1,2,2,7,3,4,9,4,10,5,9,3,5,3,9,1,6,0,3,5,4,6,8,9,10,4,3,8,4,3,6,8,2,4,3,1,4,3,9,0,9,0,10,1,10,4,5,2,0,9,1,2,10,8,0,9,9,3,4,2,10,6,2,7,6,5,5,6,3,1,0,9,8,7,3,9,5,9,1,2,2,8,5,3,2,4,6,9,7,8,9,4,6,8,7,1,1,7,6,0,5,4,8,1,3,8,8,10,7,5,1,5,9,7,7,6,5,10,5,0,3,8,4,6,6,1,5,3,10,0,8,4,8,10,6,2,4,10,3,10,6,1,9,10,7,5,1,8,1,6,0,6,10,10,3,10,9,5,10,7,7,3,7,5,0,5,7,4,8,1,6,5,2,0,7,9,3,0,0,9,3,5,4,8,0,10,0,3,2,1,3,8,9,7,1,3,2,2,5,5,9,9,3,5,5,3,1,10,7,8,6,5,3,2,2,4,3,7,1,7,7,4,8,2,4,2,9,9,0,9,1,5,9,3,4,8,8,5,2,7,10,0,0,6,2,9,9,5,0,3,5,2,2,4,9,5,0,8,1,2,7,4,5,9,1,10,4,5,0,5,1,5,5,2,2,9,1,8,6,1,1,3,6,1,8,3,1,3,10,6,1,9,0,10,5,3,3,3,10,2,4,5,5,0,2,4,8,9,1,10,3,4,4,7,10,4,6,9,4,3,10,10,6,5,2,4,7,1,0,10,4,10,1,7,6,3,8,8,7,10,1,8,8,5,5,8,1,3,7,9,5,0,10,0,7,8,6,5,1,6,4,5,10,2,4,8,9,2,5,5,1,2,7,8,6,10,7,1,7,8,10,10,9,8,0,2,10,3,0,8,0,5,2,0,3,10,7,1,1,7,10,3,0,8,0,2,7,5,4,1,9,7,5,5,3,7,1,4,1,6,3,4,8,3,2,2,0,6,1,0,4,5,9,5,3,10,3,3,0,8,7,4,5,4,3,1,3,3,4,0,8,5,1,4,4,7,1,4,10,8,3,5,9,1,0,6,6,10,7,9,4,1,0,9,10,2,6,9,4,6,5,8,7,6,1,1,2,7,3,5,8,2,10,9,2,0,3,6,1,3,7,4,2,9,6,9,1,6,3,3,6,4,10,0,4,10,10,4,1,10,0,5,3,1,5,8,1,5,7,1,7,8,1,10,3,10,0,7,4,9,2,6,4,10,6,10,3,2,2,0,10,7,8,10,6,6,8,2,1,2,0,3,6,4,8,10,5,7,8,5,7,7,5,5,0,9,5,7,4,5,5,1,3,10,0,0,1,10,9,9,9,9,0,1,2,4,2,3,2,2,10,0,4,4,6,4,0,0,4,7,4,1,1,2,0,1,10,10,3,7,7,8,9,5,7,9,5,9,5,1,7,3,7,9,0,5,9,5,7,10,2,1,2,3,2,1,6,10,0,5,7,1,10,6,10,5,10,3,9,9,9,7,1,1,1,10,0,6,7,7,5,3,0,6,0,8,3,7,2,9,7,3,2,10,8,1,8,0,2,8,7,7,0,7,7,3,10,8,2,9,3,8,3,8,6,8,7,3,3,2,5,1,9,1,1,4,8,5,1,10,2,1,2,1,3,10,7,4,10,7,4,10,3,8,7,10,7,2,9,10,5,4,8,4,6,0,10,8,1,9,5,4,2,5,9,9,6,0,2,1,6,1,2,3,7,8,2,4,10,2,2,1,0,3,7,9,8,1,9,4,8,3,1,8,7,7,4,4,7,8,5,5,6,5,9,9,8,9,0,7,1,0,3,0,7,2,2,8,5,6,0,7,9,2,8,8,4,1,6,0,10,6,5,5,0,7,8,1,10,1,7,6,4,5,10,6,9,8,9,6,1,3,1,7,6,0,9,4,10,6,5,9,1,7,10,8,6,6,8,9,6,7,5,10,4,3,8,0,2,9,10,7,3,0,5,2,9,0,9,1,10,7,10,2,0,2,0,3], [3,8,0,10,6,8,7,8,2,10,2,6,1,5,2,3,8,6,7,6,9,1,9,2,7,0,7,8,3,3,5,7,5,4,4,9,5,10,0,8,5,8,8,9,5,5,9,10,9,5,6,3,10,2,6,5,5,8,2,9,1,10,5,2,10,7,4,6,9,5,2,6,5,4,6,7,2,5,8,5,0,9,7,2,5,8,6,10,1,3,0,2,2,4,8,6,3,0,6,7,0,3,3,2,1,9,4,8,7,5,0,5,7,9,0,6,2,0,1,10,0,9,10,4,0,3,9,1,2,1,6,9,0,4,5,4,3,5,7,10,2,6,4,0,8,2,8,10,6,0,6,9,1,2,7,3,4,6,9,2,1,3,1,3,1,0,9,1,7,9,3,3,9,0,1,9,4,3,7,7,3,6,3,1,9,9,5,5,3,3,7,5,3,7,0,9,6,6,3,7,6,10,0,2,1,3,2,3,1,0,0,10,4,1,4,5,3,6,3,8,7,6,5,0,6,8,2,6,1,0,8,7,0,5,0,8,4,0,10,8,10,2,4,8,1,4,7,9,6,0,10,8,2,1,1,1,2,1,9,2,2,9,9,9,0,7,5,1,9,2,9,0,0,4,10,8,4,4,2,0,8,8,9,10,4,5,6,3,2,7,6,2,9,10,5,1,0,6,5,6,10,2,6,10,3,3,8,2,1,4,4,2,2,6,4,10,8,9,4,5,8,10,0,4,4,1,3,9,0,7,6,5,4,9,4,10,4,4,5,5,2,3,1,4,7,9,1,0,8,2,5,6,8,6,0,10,10,7,2,6,4,7,6,4,7,5,10,4,10,10,7,7,3,10,10,2,7,1,7,8,4,6,2,6,0,9,7,1,8,4,4,10,7,2,8,3,8,9,1,5,6,3,8,4,7,0,2,1,2,4,10,8,1,8,8,6,3,3,1,4,3,3,6,1,8,9,1,3,0,6,2,1,2,9,2,5,2,3,10,10,2,9,0,4,5,2,4,8,3,0,8,1,9,0,10,4,4,7,1,3,2,8,5,3,8,9,9,6,10,4,9,8,0,2,9,7,8,4,4,8,5,8,9,8,7,10,3,2,6,5,5,5,9,4,3,6,7,8,7,2,1,0,8,6,0,3,6,7,0,3,8,0,2,7,9,6,4,5,4,9,6,6,1,8,3,9,9,1,0,4,3,2,2,7,0,0,3,4,6,10,2,7,1,6,3,0,0,2,0,1,8,8,5,1,3,6,1,9,8,10,4,4,9,2,2,1,5,9,0,4,7,6,9,4,10,9,4,6,4,0,1,9,2,7,6,9,2,5,8,3,8,8,0,2,9,9,6,0,6,7,10,7,3,9,10,8,8,1,8,9,2,9,5,0,5,8,1,10,2,7,8,9,3,0,0,7,5,6,7,4,10,2,2,1,0,9,7,2,9,8,5,10,10,0,5,1,10,7,8,9,0,4,1,5,6,2,9,1,1,0,10,0,4,4,8,0,2,2,2,6,8,6,8,6,0,3,8,3,0,6,1,10,4,5,6,4,7,6,8,1,5,5,4,9,7,0,1,2,4,9,7,8,2,10,9,2,10,1,0,2,10,9,9,4,0,8,4,9,7,3,7,3,7,3,5,10,8,7,8,3,5,1,1,0,4,3,10,10,10,1,2,10,5,2,9,8,8,4,6,10,8,9,3,7,10,4,0,2,6,0,2,8,8,10,4,10,2,1,6,4,5,9,7,1,5,5,8,3,9,9,2,10,1,2,0,6,0,3,5,2,4,1,3,5,9,8,7,8,2,0,7,1,7,6,0,1,6,7,1,4,6,2,10,8,7,3,6,6,1,2,10,9,2,8,1,3,9,7,6,4,2,10,10,10,0,5,5,8,8,1,6,3,5,8,10,0,5,7,6,2,0,4,6,8,7,5,5,2,8,6,9,6,2,1,2,5,8,3,0,2,10,10,7,4,9,0,7,10,0,6,3,0,1,3,5,1,3,4,10,10,3,8,4,3,4,7,2,5,6,7,7,6,1,2,7,4,0,9,2,1,9,8,9,8,6,6,8,6,8,4,4,4,10,2,9,1,3,0,3,5,8,6,0,8,3,2,3,10,7,7,1,5,5,7,10,5,10,8,10,10,1,7,3,7,8,2,0,8,2,4,1,3,9,8,10,8,0,9,7,0,0,10,2,5,1,9,8,0,9,3,2,2,3,3,7,9,3,5,6,8,10,6,8,6,4,2,10,0,3,7]))

    # print('{' == '}')
    a = [1, 2, -2, -1, 3, -3]










