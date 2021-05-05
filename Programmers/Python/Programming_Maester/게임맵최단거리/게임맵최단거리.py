from collections import deque

def bfs(start,maps):

    direct = [[-1,0],[0,-1],[1,0],[0,1]]
    queue = deque()
    queue.append(start)

    while queue:
        y, x , cnt= queue.popleft()
        maps[y][x] = 0

        for dy, dx in direct:
        
            next_x , next_y =  x + dx, y + dy
            
            if next_y == len(maps) -1  and next_x == len(maps[0]) -1 :
                return cnt + 1
            
            if 0 <= next_y < len(maps) and 0 <= next_x < len(maps[0]) and maps[next_y][next_x] == 1:
                maps[next_y][next_x] = 0
                queue.append([next_y,next_x,cnt+1])
    
    return -1
    
def solution(maps):
    answer = bfs([0,0,1],maps)
    return answer