
def to_re(l_list):

    return money_amount_re(l_list, 0, 0)

def money_amount_re(l_list, level, amounts) -> int:
    count = 0
    if level > 1:
        return amounts

    for i in range(2, 4):
        for l in range(level, len(l_list), i):
            count += l_list[l]
        if count > amounts:
            amounts = count
        count = 0
    return money_amount_re(l_list, level+1, amounts)

# -------------------------------------------------------------------

def money_amount(l_list) -> int:
    count = 0
    amounts = 0

    if len(l_list) == 1:
        return l_list[0]
    elif len(l_list) == 2:
        return max(l_list)

    for inx in range(0, 2):
        v = 2
        while v < 4:
            for numin in range(inx, len(l_list), v):
                count += l_list[numin]
            if count > amounts:
                amounts = count
            count = 0
            v += 1
    # print(amounts)
    return amounts

if __name__ == '__main__':
    nums = [7, 1, 1, 6, 1, 7]
    nums1 = [7, 2, 9, 30, 1]
    nums3 = [1, 8]
    nums4 = [1, 20, 8, 6, 8, 4]
    nums5 = [5, 1, 1, 5]
    nums6 = [2, 7, 9, 3, 1]
    print('nums', money_amount(nums))
    print('nums1', money_amount(nums1))
    print('nums3', money_amount(nums3))
    print('nums4', money_amount(nums4))
    print('nums5', money_amount(nums5))
    print('nums6', money_amount(nums6))

    print('nums', to_re(nums))
    print('nums1', to_re(nums1))
    print('nums3', to_re(nums3))
    print('nums4', to_re(nums4))
    print('nums5', to_re(nums5))
    print('nums6', to_re(nums6))


