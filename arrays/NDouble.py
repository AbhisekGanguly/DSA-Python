# Check If N and Its Double Exist

def nDouble(arr):
    for i in range(len(arr)):
        if 2*arr[i] in arr:
            return True
    return False

def main():
    arr = [10, 2, 5, 3]
    print(nDouble(arr))

main()