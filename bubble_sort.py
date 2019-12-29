"""
Bubble Sort
time complexity: O(n2)
"""


def bubble_sort(seq):
    if len(seq) <= 1:
        return seq
    for iter_num in range(len(seq)-1, 0, -1):
        for i in range(iter_num):
            if seq[i] > seq[i+1]:
                seq[i+1], seq[i] = seq[i], seq[i+1]


l = [234, 123412, 1324123, 12341, 351234, 235234, 26523452, 623462, 1]
bubble_sort(l)
print(l)
