# given an array, sort it to send all the even integer to the front of the array,
# and all the odd integers to the back of the array

def paritySorting(nums):
    i = 0
    j = len(nums) - 1
    while i < j:
        if nums[i] % 2 == 0:
            i += 1
        else:
            nums[i], nums[j] = nums[j], nums[i]
            j -= 1
    return nums

def main():
    nums = [3,1,2,4]
    print(paritySorting(nums))

main()