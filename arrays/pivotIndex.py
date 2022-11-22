# Program to find out the pivot index of an array
# return the leftmost pivot index. If no such index exists, return -1.

def pivotIndex(nums):
    sumL = 0
    sumR = sum(nums)
    for i in range(len(nums)):
        sumR -= nums[i]
        if sumL == sumR:
            return i
        sumL += nums[i]
    return -1

def main():
    nums = [1,7,3,6,5,6]
    print(pivotIndex(nums))

main()