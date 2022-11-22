def thirdMaxNo(num):
    sorted_num = sorted(num)
    return sorted_num[-3]

def main():
    num = [3,2,1,7,5,6]
    print(thirdMaxNo(num))

main()