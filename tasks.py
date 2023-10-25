# Write a function that takes two lists and adds the first element in the first list 
# with the first element in the second list, the second element in the first list with 
# the second element in the second list, etc, etc. Return True if all element combinations 
# add up to the same number. Otherwise, return False. 
# Example:

# puzzle_pieces([1, 2, 3, 4], [4, 3, 2, 1]) ➞ True
# # 1 + 4 = 5;  2 + 3 = 5;  3 + 2 = 5;  4 + 1 = 5
# # Both lists sum to [5, 5, 5, 5]
# puzzle_pieces([1, 8, 5, 0, -1, 7], [0, -7, -4, 1, 2, -6]) ➞ True
# puzzle_pieces([1, 2], [-1, -1]) ➞ False
# puzzle_pieces([9, 8, 7], [7, 8, 9, 10]) ➞ False

# def puzzle_pieces([1, 2, 3], [4, 5, 6]) -> bool: # negerai
#     sums = []
#     for x, y in zip([1, 2, 3], [4, 5, 6]):
#         sums.append(x + y)
#     return sums
#     print(sums)
# # list1 = [1, 2, 3]
# # list2 = [4, 5, 6]
# result = puzzle_pieces([1, 2, 3], [4, 5, 6])
# print(result)

# Alberto  Python
# from typing import Listdef can_find(bi_list: List[str], words_list: List[str]) -> bool:    check_list: list = [bi for bi in bi_list if any(bi in word for word in words_list)]    if check_list == bi_list:        return True    return False    # 4.3# can_find = lambda bi_list, words_list: True if bi_list == [x for x in bi_list if any(x in bi for bi in words_list)] else Falseprint(can_find(["at", "be", "th", "au"], ["beautiful", "the", "hat"]))print(can_find(["ay", "be", "ta", "cu"], ["maybe", "beta", "abet", "course"]))print(can_find(["th", "fo", "ma", "or"], ["the", "many", "for", "forest"]))print(can_find(["oo", "mi", "ki", "la"], ["milk", "chocolate", "cooks"]))