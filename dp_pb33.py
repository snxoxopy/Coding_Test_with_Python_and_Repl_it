"""
dp[i] = i번째 날부터 마지막 날까지 낼 수 있는 최대 
dp[i] = max(p[i]+dp[t[i]+i], max_value)
"""


n = int(input())
#뇨각 상담을 완료하는 데 걸리는 기간
t = []
#각 상담을 완료했을 때 받을 수 있는 금액
p = []
## 다이나믹 ㅍ르로그래밍을 위한 1차원 dp 테이블 초기화
dp = [0] * (n+1)
max_value = 0

for _ in range(n):
  a, b = map(int, input().split())
  t.append(a)
  p.append(b)
#리스트 뒤에서부터 거꾸로 확인
for i in range(n-1, -1, -1):
  time = t[i] + i
  if time <= n:
    dp[i] = max(p[i] + dp[time],max_value)
    max_value = dp[i]
  else:
    dp[i] = max_value
print(max_value)