from collections import deque
class Solution:
	def orangesRot(self, mat):
		# code here
		
		matrix = mat.copy()
	    
		q = deque()
		for i in range(len(matrix)):
		    for j in range(len(matrix[0])):
		        if matrix[i][j] == 2:
		            q.append((i, j))
        
        n, m = len(matrix), len(matrix[0])
        min_time = -1
        while q:
            min_time += 1
            for _ in range(len(q)):
                r, c  = q.popleft()
                
                for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    new_i, new_j = r + dx, c + dy
                    
                    if new_i < 0 or new_i >= n or new_j < 0 or new_j >= m:
                        continue
                    
                    if matrix[new_i][new_j] == 1:
                        q.append((new_i, new_j))
                        matrix[new_i][new_j] = 2
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1:
                    return -1
                    
        return min_time if min_time!=-1 else 0