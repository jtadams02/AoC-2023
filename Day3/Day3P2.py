#Looks like some form of BFS but not in depthly
# Now that i am thinking it through, we do not really need a dequeu
from collections import deque

infile = open("input.txt",'r')

# Build a 2D array of each character??
n = infile.readline()

grid = []
while n:
    row = [char for char in n]
    if row[-1] == '\n':
        row.pop()
    grid.append(row)
    n = infile.readline()

def bfs(q):
    while q:
        curr = q.popleft()
        row = curr[0]
        col = curr[1]
        
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0),(-1,1),(-1,-1),(1,1),(1,-1)]:
            nr = row + dx
            nc = col + dy
            if (nr >=0 and nr < len(grid)) and (nc >=0 and nc < len(grid[0])):
                if not grid[nr][nc].isnumeric() and grid[nr][nc] == '*':
                    return (nr,nc)
    return None


total = 0

m = {}
for i in range(len(grid)):
    num_found = 0
    curr_q = deque()
    curr_num = ''
    for j in range(len(grid[0])):
        if grid[i][j].isnumeric():
            # If it is numeric we start building a queue
            curr_q.append((i,j))
            curr_num += grid[i][j]
            num_found = 1
        else:
            if num_found:
                print(f"Trying {curr_num}")
                num_found = 0
                t = bfs(curr_q)
                if t:
                    if t in m:
                        m[t][0] *= int(curr_num)
                        m[t][1] += 1
                    else:
                        m[t] = [int(curr_num),1]
                    print(f"Got {curr_num}!")
                # print(curr_num)
                # Now reset our curr_q
                curr_q = deque()
                curr_num = ''
    if num_found:
        # print(f"Trying {curr_num}")
        num_found = 0
        t = bfs(curr_q)
        if t:
            if t in m:
                m[t][0] *= int(curr_num)
                m[t][1] += 1
            else:
                m[t] = [int(curr_num),1]

        # Now reset our curr_q
        curr_q = deque()
        curr_num = ''
        
for t in m:
    if m[t][1] == 2:
        total += m[t][0]
print("Output:", total)
                
                
            
    