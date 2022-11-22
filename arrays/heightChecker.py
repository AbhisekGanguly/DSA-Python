def heightChecker(nums):
    # sort the array
    sorted_nums = sorted(nums)
    # count the number of elements that are not in the same position
    count = 0
    for i in range(len(nums)):
        if nums[i] != sorted_nums[i]:
            count += 1
    return count

def main():
    nums = [1,1,4,2,1,3]
    print(heightChecker(nums))

main()