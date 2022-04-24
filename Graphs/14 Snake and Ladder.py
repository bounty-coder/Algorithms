# Given a 10*10 snake and ladder board, find the minimum no of dice 
# to be rolled to end the game.
 
#approach-
# Clearly, See the board as a graph/matrix. Each block can be represented as
# a vertex. Each possible move from a dice roll is an edge. We have choices from 
# 1 to 6 for traversing and start vertex is 1 and end vertex is 100.
# for 99 it has only 1 edge, for block 98- 2 edges...
# Next modifying this graph on the based input ladders and snakes
# For ex. if we reach 32 it will move to 62(by ladder). So, better to replace
# all vertex pointing to 32 to 62. and so for the all ladders and snakes.
# As it is the unweighted graph, We have to find the shortest distance/path from
# source node to the destination node which can be processed by bfs traversal.
# Dfs can also be used for traversal, but it doesn't make any sense here to use it.
# as we first have to see all the dice moves 1 to 6 then move on which is possible 
# by bfs only.

# approach 1 ( if board not already given, make your own board)
# A- ladders , B- Snakes
# A = [  [32, 62], [42, 68], [12, 98] ]  
#  B = [  [95, 13] [97, 25] [93, 37] [79, 27] [75, 19]
#         [49, 47] [67, 17] ]
# output: 3
from collections import deque
def snakeLadder(A, B):
    # we will start from 1, it'll be easy to implement
    board=[-1]*101
    # changing all given nodes values
    for i in range(len(A)):
        board[A[i][0]]=A[i][1]
    for i in range(len(B)):
        board[B[i][0]]=B[i][1]
    
    q=deque()
    q.append([1,0])  # [square(1-100), move]
    visit=set()
    while q:
        square,moves=q.popleft()
        for i in range(1,7):   # 1 to 6
            nextSquare= square + i

            # if nodes value is not -1, its on ladder or snake
            # change nextsquare to that place
            if board[nextSquare]!=-1:
                nextSquare=board[nextSquare]

            # if node has reached to end
            if nextSquare==100:
                return moves+1
            
            if nextSquare not in visit:
                visit.add(nextSquare)
                q.append([nextSquare,moves+1])
    return -1

# solution approach 2
# if board already given(although code is same😅)
# [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],
# [-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]

def snakesAndLadders(board):
    length=len(board)
    # board was given in reverse order(ie 100th row first)
    board.reverse()

    # converting square into position( do it last) 
    def intToPos(square):
        r=(square-1)//length
        c=(square-1)%length
        if r%2:
            c=length-1-c
        return [r,c]
    
    q=deque([])
    q.append([1,0])
    visit=set()
    while q:
        square, moves = q.popleft()
        for i in range(1,7):
            nextSquare = square + i
            r,c=intToPos(nextSquare)
            if board[r][c]!=-1:
                nextSquare = board[r][c]
            if nextSquare == length*length:
                return moves+1
            if nextSquare not in visit:
                visit.add(nextSquare)
                q.append([nextSquare,moves+1])
    return -1