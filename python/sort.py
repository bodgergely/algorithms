import unittest
import random
import time

def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

def partition(arr, i, j):
    pivot_elem = arr[j]
    curr_idx = i
    divider_idx = i
    while curr_idx < j:
        if arr[curr_idx] < pivot_elem:
            swap(arr, curr_idx, divider_idx)
            divider_idx += 1 
        curr_idx+=1 

    swap(arr, j, divider_idx)
    return divider_idx


def quicksort(arr):
    def _quicksort(arr, i, j):
        if i >= j:
            return
        p = partition(arr, i, j)
        _quicksort(arr, i, p-1)
        _quicksort(arr, p+1, j)
    _quicksort(arr, 0, len(arr)-1)


class QuickSortTest(unittest.TestCase):
    def test_quicksort(self):
        li = [4,3,8,1,9,4,12,4,4,2,3]
        copy = li
        quicksort(li)
        self.assertEqual(li, sorted(copy))
        li = [4,3,3,3]
        copy = li
        quicksort(li)
        self.assertEqual(li, sorted(copy))
    def test_random_lists(self):
        count = 100
        for i in range(count):
            li = [random.randrange(0,200) for j in range(2000)]
            copy = li
            quicksort(li)
            self.assertEqual(li, sorted(copy))
    def timed_sort(self, li, sorter):
        start = time.time()
        sorter(li)
        return time.time() - start
    def test_speed(self):
        count = 100
        quick_time_sum = 0
        builtin_time_sum = 0
        for i in range(count):
            li = [random.randrange(0,20000) for j in range(20000)]
            cp = li
            quick_time_sum += self.timed_sort(li, quicksort)
            builtin_time_sum += self.timed_sort(cp, sorted)

        quick_sort_time = quick_time_sum/float(count) *   1000000
        built_sort_time = builtin_time_sum/float(count) * 1000000
        print("quicksort avg time:", quick_sort_time)
        print("builtin_sort avg time:", built_sort_time)
        print("Ratio:", quick_sort_time/built_sort_time)


if __name__ == "__main__":
    unittest.main()

