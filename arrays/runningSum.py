# Program to find out the running sum of an 1D array.

def sumArray(nums):
    for i in range(len(nums) - 1):
        nums[i+1] += nums[i]
    return nums

def main():
    nums = [1,2,3,4]
    print(sumArray(nums))

main()