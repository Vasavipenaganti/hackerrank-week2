if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    newarr = list(set(arr))
newarr.sort()
print (newarr[-2:][0])
