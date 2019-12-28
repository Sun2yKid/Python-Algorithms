"""
Merge Sort
time complexity: O(nlogn)
"""


def merge_sort(seq):
    if len(seq) <= 1:
        return seq
    mid = len(seq) // 2
    left = merge_sort(seq[:mid])
    right = merge_sort(seq[mid:])
    return merge_sorted_list(left, right)


def merge_sorted_list(left, right):
    """
    合并两个排好序的(升序)列表
    """
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    return result + left[i:] + right[j:]


seq = [34, 12, 324534, 24, 5, -1, 1, 99, 354]
print(merge_sort(seq))
