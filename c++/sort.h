#pragma once

#include <vector>
#include <algorithm>

/*
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
*/


template<class T>
int partition(std::vector<T>& arr, int i, int j)
{
    T pivot_elem = arr[j];
    int curr_idx = i;
    int divider_idx = i;
    while(curr_idx < j)
    {
        if(arr[curr_idx] < pivot_elem)
        {
            std::swap(arr[curr_idx], arr[divider_idx]);
            divider_idx++;
        }
        curr_idx++;
    }
    std::swap(arr[j], arr[divider_idx]);
    return divider_idx;
}


template<class T>
void _quick_sort(std::vector<T>& arr, int i, int j)
{
    if(i >= j)
        return;
    int p = partition(arr, i, j);
    _quick_sort(arr, i, p-1);
    _quick_sort(arr, p+1, j);
}

template<class T>
void quick_sort(std::vector<T>& arr)
{
    _quick_sort(arr, 0, arr.size());
}
