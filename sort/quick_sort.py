"""
Quick Sort
average time  complexity: O(nlogn)
average space complexity: O(logn)
"""
from timer import timer


@timer
def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


print('*'*10, 'start', '*'*10)
l = [234, 123412, 1324123, 12341, 351234, 235234, 26523452, 623462, 1]
print(quick_sort(l))


