# Check if a given array is a valid mountain array

def MountainArray(arr):
    # function to check if a given array is a valid mountain array
    if len(arr) < 3:
        return False
    i = 0
    while i < len(arr)-1:
        if arr[i] < arr[i+1]:
            i += 1
        else:
            break
    if i == 0 or i == len(arr)-1:
        return False
    while i < len(arr)-1:
        if arr[i] > arr[i+1]:
            i += 1
        else:
            return False
    return True

def main():
    arr = [0, 3, 2, 1]
    print(MountainArray(arr))

main()