# Given a fixed-length integer array arr, duplicate each occurrence of zero, 
# shifting the remaining elements to the right.

def duplicateZeros(arr):
    # function to duplicate zeros in an array
    i = 0
    while i < len(arr):
        if arr[i] == 0:
            arr.insert(i+1, 0)
            arr.pop() # remove last element
            i += 1
        i += 1
    return arr

def main():
    arr = [1, 0, 2, 3, 0, 4, 5, 0]
    print(duplicateZeros(arr))

main()

# As the pop() method is used in this problem to solve the question, this no longer
# qualifies as an "Array" problem. It is now a "Stack" problem. The difference is that
# the pop() method is not available in arrays in Python. Arrays are fixed-length and
# immutable. Stacks are dynamic and mutable. The pop() method is used to remove and
# return the last element of a stack. 