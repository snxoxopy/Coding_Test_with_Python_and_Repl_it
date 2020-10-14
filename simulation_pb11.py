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
  info.append((int(x),c))

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
def simulate():
  #뱀 머리 위치
  x, y = 1, 1
  #뱀이 존재하는 위치의 값은 2
  data[x][y] = 2
  #초기 이동방향 동쪽
  direction = 0
  #시작한 뒤에 지난 '초' 시간, 결과 출력 변수
  time = 0
  #다음 회전 정보
  index = 0
  #뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)
  q = [(x, y)]

  while True: #종료 조건: 벽이나 뱀의 몸통과 부딪힌 경우
    nx = x + dx[direction]
    ny = y + dy[direction]

    #맵 범위 내 존재하고, 뱀이 없는 좌표일 경우
    if(1 <= nx and nx <= n and ny <= n and data[nx][ny] != 2):
      #사과 없는 경우
      if data[nx][ny] == 0:
        #**꼬리 제거
        data[nx][ny] = 2
        q.append((nx,ny))
        px, py = q.pop(0)
        data[px][py] = 0
      #사과 있는 경우
      if data[nx][ny] == 1:
        #꼬리 유지
        data[nx][ny] = 2
        q.append((nx,ny))

    #벽이나 뱀의 몸통과 부딪힌 경우
    else:
      time += 1
      break
    #다음 위치 좌표
    x, y = nx, ny
    time += 1
    #회전할 시간인 경우
    if(index < 1 and time == info[index][0]):
      direction = turn(direction, info[index][1])
      index += 1
  return time

print(simulate())