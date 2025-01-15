def count(n):
    res=0

    while n>0:
        res+=1&n

        n=n>>1

    return res

print(count(3))