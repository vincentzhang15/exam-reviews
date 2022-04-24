"""
Demonstrate the binary search algorithm for the final exam review of the introduction to comp sci course.
@author Vincent Zhang
@since 8 December 2021
"""

def bin_search(data, val):
    s = 0
    e = len(data) - 1

    while s <= e:
        m = s + (e - s) // 2
        if data[m] == val:
            return m
        if data[m] < val:
            s = m + 1
        else:
            e = m - 1
    return None
if __name__ == '__main__':
    print(bin_search(sorted([10, 2, 2, 7, 8, 1]), 9))
# [1, 2, 2, 7, 8, 10], 2
# Output: 2
# [1, 2, 2, 7, 8, 10], 9
# Output: None
