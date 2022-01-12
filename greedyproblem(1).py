n , m, k = map(int, input().split())

data = list(map(int, input().split()))
data.sort(reverse = True)

answer = 0

data1 = 0
count = 0

mook = m//k
narme = m%k

if data[0] == data[1]:
    answer = data[0] * m
else:
    answer = data[0]*k*mook + data[1]*narme
print(answer)
