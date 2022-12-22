








# ---- Runtime: 50 ms   Beats: 78.11%   Memory: 13.9 MB --------------------------------

def merge(nums1: list[int], m: int, nums2: list[int], n: int):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    inx = 0
    if n == 0:
        return nums1
    else:
        for i, num in enumerate(nums2):

            for j in range(m):
                if num > nums1[j]:
                    inx = j+1
                elif num <= nums1[j] and j == 0:
                    inx = j
                elif num <= nums1[j] and num > nums1[j - 1]:
                    inx = j
            nums1.insert(inx, num)
            m += 1
            nums1.pop(-1)
    return nums1


# ---- Runtime: 48 ms   Beats: 80.11%   Memory: 13.9 MB --------------------------------

# def merge(nums1: list[int], m: int, nums2: list[int], n: int):
#     """
#     Do not return anything, modify nums1 in-place instead.
#     """
#     inx = 0
#     if n == 0:
#         return nums1
#     else:
#         for i, num in enumerate(nums2):
#             for j in range(m):
#                 if num > nums1[j]:
#                     inx = j+1
#                 elif num <= nums1[j] and num > nums1[j - 1]:
#                     inx = j
#             if num <= nums1[i] and i == 0:
#                 nums1.insert(i, num)
#             else:
#                 nums1.insert(inx, num)
#             m += 1
#             nums1.pop(-1)
#     return nums1



# nums1 = [1, 2, 3, 0, 0, 0]
# m = 3
# nums2 = [2, 5, 6]
# n = 3

nums1 = [2, 0]
m = 1
nums2 = [1]
n = 1

# nums1 = [1]
# m = 1
# nums2 = []
# n = 0

# nums1 = [0]
# m = 0
# nums2 = [1]
# n = 1

# nums1 = [4, 5, 6, 0, 0, 0]
# m = 3
# nums2 = [1, 2, 3]
# n = 3

# nums1 = [-1,0,0,3,3,3,0,0,0]
# m = 6
# nums2 = [1,2,2]
# n = 3

print(merge(nums1, m, nums2, n))
