#You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
#and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

def mergeSortedArray(nums1, m, nums2, n):
    # function to merge two sorted arrays
    nums1[m:] = nums2[:n]
    nums1.sort()
    return nums1

def main():
    nums1 = [1, 2, 3, 11, 0, 0, 0, 0, 0, 0, 0]
    m = 4
    nums2 = [2, 5, 6, 8, 10, 12]
    n = 6
    print(mergeSortedArray(nums1, m, nums2, n))

main()