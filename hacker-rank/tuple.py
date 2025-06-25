if __name__ == '__main__':
    n = int(input())
    integer_list =tuple(map(int,input().split()))
    if len(integer_list) == n:
        print(integer_list)
        t=integer_list
        print(hash(t))




