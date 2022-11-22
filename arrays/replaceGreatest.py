# Given an array arr, replace every element in that array with the greatest element among the 
# elements to its right, and replace the last element with -1

def replaceGreatest(arr):
    # function to replace every element in an array with the greatest element among the 
    # elements to its right, and replace the last element with -1
    for i in range(len(arr)-1):
        arr[i] = max(arr[i+1:])
    arr[-1] = -1
    return arr

def main():
    arr = [17, 18, 5, 4, 6, 1]
    print(replaceGreatest(arr))

main()