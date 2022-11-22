# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place 
# such that each unique element appears only once. The relative order of the elements should be kept the same.

def removeDuplicates(nums):
    # function to remove duplicates in-place
    i = 0
    while i < len(nums):
        if nums[i] in nums[i+1:]:
            nums.remove(nums[i])
        else:
            i += 1
    return nums

def main():
    nums = [1, 1, 2, 2, 3, 2, 3, 4, 4, 5, 5]
    print(removeDuplicates(nums))
    print(len(nums))

main()