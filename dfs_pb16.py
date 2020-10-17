"""
0꽁간/1벽/2바이러스

"""

#n = 세로 x m 가로 
n , m = map(int, input().split())
data = []
#맵정보 리스트 초기화
temp = [ [0] * (m) for _ in range(n) ]

for _ in range(n):
  data.append( list(map(int, input().split())))
  
# 4가지 이동방향
#상 하 좌 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

result = 0


def virus(x, y):
  

def get_score():
  return score 

# 울타리를 설치하면서 매번 안전 영역의 크기 계산
def dfs(count):
  # 울타리가 3 개인 경우
  
  # 빈 공간에 울타리 설치
  if 
  return