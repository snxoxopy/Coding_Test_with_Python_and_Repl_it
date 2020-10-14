"""
모든 도로의 거리는 1 이라는 조건 덕분에 너비 우선 탐색을 이용하여 간단히간해결 가능
review
BFS
1. queue에 시작 노드 삽입
2. 시작 노드 방문 처리
3. queue에서 노드를 빼내어 인접노드 확인
"""

from collections import deque

# 도시 개수, 도로개수, 거리정보, 출발 도시 번호
n, m, k, x = map(int, input().split())

# 각 행은 노드에 연결된 다른 노드를 표기함
# 리스트 초기화
# 오답노트: BFS 그래프는 연결된 노드 집합으로 사용 
graph = [ [] for _ in range(n + 1) ]


for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)

# 한번 방문한 곳은 중복 방문하지 않는 방법 --> deque를 이용하여 distance가 -1이 아닐 경우 popleft()
  
# 모든 도시에 대하여 거리 초기회
# 최단 거리 업데이트를 위한 리스트
distance = [-1] * (n+1)
distance[x] = 0 
  
# 처음 시작노드 큐에 삽입
q = deque([x])

while q:
  now = q.popleft()
  # 현제 도시에서 이동할 수 있는 모든 도시를 확인
  for next_node in graph[now]:
    # 오답노트: distance[now] --> 다음 드부터 확인해야함
    if distance[next_node] == -1:
    # 최단 거리 갱신
      distance[next_node] = distance[now] + 1
      q.append(next_node)

# 최단 거리가 k인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n+1):
  if distance[i] == k:
    print(i)
    check = True

if check == False:
  print(-1)