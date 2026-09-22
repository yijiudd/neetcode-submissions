class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directs=[[-1,0],[1,0],[0,1],[0,-1]]
        visited=[[False]*len(board[0]) for _ in range(len(board))]
        self.res=False
        def dfs(choices,cur_pos,target):
            if board[cur_pos[0]][cur_pos[1]]!=target[0]:
                            return
            if len(target)==1:
                self.res=True
                return 
     
            visited[cur_pos[0]][cur_pos[1]] = True
            for direct in choices:
                next_pos = [x + y for x, y in zip(cur_pos, direct)]
                if next_pos[0]>=0 and next_pos[0]<len(board) and next_pos[1]>=0 and next_pos[1]<len(board[0]):
                       if visited[next_pos[0]][next_pos[1]]==False:
                            dfs(choices,next_pos,target[1:])
            visited[cur_pos[0]][cur_pos[1]] = False
        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                dfs(directs,[i,j],word)
        return self.res
        