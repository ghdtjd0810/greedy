m,n = map(int, input().split())

renewal = 0

#여기서 내가 헷갈린 핵심은, 컴퓨터가 표현하때 데이터 이거 읽고 버려도 된다는 것.
# 즉 데이터 입력받고 소팅때리고 갱신시켰으면 다음걸로 그냥 넘어가도 된다는거지
# 내가 알고싶은 답은 과정 전체를 알고싶은게 아니니까.

for i in range(m):
    data = list(map(int,input().split()))
    data.sort()
    renewal = max(renewal, data[0])
    

print(data)
print(renewal)
