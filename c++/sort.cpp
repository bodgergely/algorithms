#include "sort.h"
#include <vector>
#include <cstdlib>
#include <ctime>
#include <chrono>
#include <cstdio>
using namespace std;

typedef void (*sorter)(vector<int>&);

double timed_sort(vector<int>& nums, sorter s)
{
    auto start = chrono::system_clock::now();
    s(nums);
    auto end = chrono::system_clock::now();
    return chrono::duration_cast<chrono::milliseconds>(end - start).count();
}

void builtin_sort(vector<int>& nums)
{
    std::sort(nums.begin(), nums.end());
}

vector<int> build_random_list(int len)
{
    vector<int> nums;
    for(int i=0;i<len;i++)
        nums.push_back(rand());
    return nums;
}

int main(int argc, char** argv)
{
   int iter_count = 5;
   double quicksort_sum = 0;
   double builtin_sum = 0;
   for(int i=0;i<iter_count;i++)
   {
       printf("Iter: %d\n", i);
       srand(time(NULL));
       vector<int> rand_list = build_random_list(2000000);
       vector<int> copy = rand_list;
       printf("quicksorting...\n");
       quicksort_sum += timed_sort(rand_list, quick_sort);
       printf("buildin sortin...\n");
       builtin_sum += timed_sort(rand_list, builtin_sort);
   }

   double qs_time = quicksort_sum / iter_count;
   double bs_time = builtin_sum / iter_count;
   printf("quicksort time: %f\n", qs_time);
   printf("builtin_sort time: %f\n", bs_time);
   printf("Ratio: %f\n", qs_time / bs_time);
   
   return 0;
}
