# to find the square of a sorted array (assending order) and return the square of
# all the numbers in the array in assending order.

def squareArraySorted(nums):
    sortedArray = [] # initialize sorted array variable
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2 # square the numbers in the array
        sortedArray.append(nums[i]) # append the square of the number to the array at the last
        sortedArray.sort() # sort the array in assending order
    return sortedArray

def main():
    nums = [-4, -1, 0, 3, 10]
    print(squareArraySorted(nums))

main()