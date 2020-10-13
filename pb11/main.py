# =================== 입력받기
# 1) 정수형
n = int(input())
k = int(input())
# 2) 리스트형
# 2-1) 초기화
data = [ [0] * (n+1) for _ in range(n+1) ]
info = []
# 2-2) 입력받기
# 사과 좌표[행][열]
for _ in range(k):
  a , b = map(int, input().split())
  #사과 있는 곳의 값은 1
  data[a][b] = 1
# 이동 좌표[초][방향]
l = int(input())
for _ in range(l):
  x, c = input().split()
  info.append(int(x),c)

# =================== 함수생성
# 1) 리스트 초기화
# 초기 방향 "오른쪽"
# 회전 방향 L=좌회전/ D=우화전
# 좌회전시 동 --> 북 --> 서 --> 남
# 우회전시 동 --> 남 --> 서 --> 북
# 동남서북 순서로 이동 방향 좌표 생성
#오답노트: dx = [1동, 0남, -1서, 0북] 여기서의 x는 행을 의미.
#오답노트: dy = [0동, 1남, 0서, -1북]
#오답노트: 매번 헷갈리지 않기 위해 dx는 행이동 dy는 열이동이라고 정의하자
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 2) turn 함수
#오답노트: def turn(c) --> 조건:c, 입/출력:direction
def turn(direction, c):
  if(c == "L"):
    #오답노트: direction -= 1 --> 범위가 벗어날 수 있음 ex) -5
    direction = (direction - 1) % 4 # [0,3]
  else:
    direction = (direction + 1) % 4
  return direction

# 3) simulate 함수