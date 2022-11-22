from typing import List


def maxConsecuiveOnes(nums: List[int]) -> int:
    # function to count maximum number of ones in a binary array
    count = 0 # initialize count
    result = 0 # initialize max
    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
        else:
            count = 0
        result = max(result, count)
    return result

def main():
    nums = [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1]
    print(maxConsecuiveOnes(nums))


main()