n , k = map(int, input().split())

'''
count = 0

# n이 True일려면 1보다 커야지. 그니까 1이되버리면 False되면서 밖으로 나옴
while n>1:
    if n%k != 0:
        n -= 1
        count += 1 
    else:
        n = n//k
        count += 1
'''
result = 0
while n >= k :
    while n&k !=0:
        n-=1
        result +=1
    n //= k
    result += 1

while n>1:
    n -= 1
    result += 1
    


print(count)
