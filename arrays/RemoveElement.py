#Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
# The relative order of the elements may be changed.

def removeElement(nums, val):
    # function to remove all occurrences of val in nums
    while val in nums:
        nums.remove(val)
    return nums

def main():
    nums = [3, 2, 2, 3, 4, 3, 5, 3, 7]
    val = 3
    print(removeElement(nums, val))
    print(len(nums))

main()