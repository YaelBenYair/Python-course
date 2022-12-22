

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

def matrixReshape(mat: list[list[int]], r: int, c: int) -> list[list[int]]:
    new_mat = []
    row = []
    count = 0
    if len(mat) * len(mat[0]) != r * c:
        return mat

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            row.append(mat[i][j])
            count += 1
            if count == c:
                new_mat.append(row)
                row = []
                count = 0

    return new_mat


mat = [[1, 2], [3, 4]]
print(matrixReshape(mat, 4, 1))
# mat2 = [mat[0]+mat[-1]]
# print(mat2)
# print(len(mat))
# print(len(mat[0]))









