# Given an array nums of n integers where nums[i] is in the range [1, n], 
# return an array of all the integers in the range [1, n] that do not appear in nums.

def disapprearedArray(nums):
    min_num = min(nums)
    max_num = max(nums)
    arr_new=[]
    for i in range(min_num, max_num + 1):
        if i not in nums:
            arr_new.append(i)
    return arr_new

def main():
    nums = [4,3,2,7,8,2,3,1]
    print(disapprearedArray(nums))

main()
