# program to count the numbers with even number of digit in an array

def evenNumberDigit(nums):
    # function to count the numbers with even number of digit in an array
    count = 0
    for i in range(len(nums)):
        if len(str(nums[i])) % 2 == 0:
            count += 1
    return count

def main():
    nums = [12, 345, 2, 6, 7896, 20, 3345, 1, 43244]
    print(evenNumberDigit(nums))

main()