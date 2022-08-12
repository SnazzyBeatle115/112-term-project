from cmu_112_graphics import *
import random
import math
import copy

def restart(app):
    # * game info
    app.mode = 'splashScreenMode'
    app.time = 0
    app.timerDelay = 100
    
    
    
    # app.board=getBoard()
    # app.startPos=0,0
    # app.endPos=4,0
    
    app.board=getMaze(app,10,10)
    app.rows=len(app.board)
    app.cols=len(app.board[0])

    x=findPath(app)
    while x == None:
        app.board=getMaze(app,10,10)
        x=findPath(app)
        
    app.path=x
    
    app.margin=10   
    
    app.inRound=False
    app.round=0
    app.win=False
    app.lose=False
    app.debug=False
    app.health=20
    
    app.bloons=0
    app.towers=app.round
    app.nextTower='first'
    
    app.bloonsPopped=0
    app.towersPlaced=0
    
    app.objects=[]
    app.bloonsList=[]
    app.towersList=[]
    # app.projectilesList=[]

# * maze gen: https://en.wikipedia.org/wiki/Maze_generation_algorithm#Randomized_depth-first_search
def getMaze(app,rows,cols):
    startPos=endPos=0,0
    while startPos==endPos:
        startPos=random.randint(0,1)*(rows-1),random.randint(0,1)*(cols-1)
        endPos=random.randint(0,1)*(rows-1),random.randint(0,1)*(cols-1)
    
    # print(startPos,endPos)
    app.startPos=startPos
    app.endPos=endPos
    
    app.maze=[['g']*cols for _ in range(rows)]
    genMaze(app, startPos, set())
    x=app.maze
    row,col=startPos
    x[row][col]='s'
    row,col=endPos
    x[row][col]='e'
    if x != None:
        return x
    
    return getBoard()
 
def genMaze(app, cell, visited):
    visited.add(cell)
    row,col=cell
    app.maze[row][col]='p'
    rows,cols=len(app.maze),len(app.maze[0])
    dirs=[(2,0),(0,2),(-2,0),(0,-2)]
    random.shuffle(dirs)
    for drow,dcol in dirs:
            nrow,ncol=row+drow,col+dcol
            if not (0<=nrow<rows and 0<=ncol<cols):
                continue
            if (nrow,ncol) in visited:
                continue
            mr,mc=(row+nrow)//2,(col+ncol)//2
            # print(cell,(nrow,ncol))
            # print(mr,mc)
            app.maze[mr][mc]='p'
            genMaze(app, (nrow, ncol), visited)


    
    
    
def getNodes(app):
    board=app.board
    nodes=[app.startPos]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]=="p":
                nodes.append((i,j))
    return nodes
    

# * BFS: https://www.cs.cmu.edu/~112/notes/student-tp-guides/Pathfinding.pdf
def findPath(app):
    queue=[app.startPos]
    visited={app.startPos}
    map={}
    # print(app.startPos)
    # for _ in app.board: print(_)
    # print()
    while queue != []:
        node=queue.pop(0)


        # i,j=node
        # print(app.board[i][j])
        # if app.board[i][j]=="e" or (i,j)==(4,0) or i==4 and j==0:
        #     print(node,app.endPos)
        #     print("awawwaawwawaaw")
            
            
            
        if node == app.endPos: # * if node is target
            print("found end")
            path=[node]
            cur=node
            # print(f"visited:\n{visited}")
            # print(f"map:\n{map}")
            i=0
            while True:
                # print(cur)
                cur=map[cur]
                path.append(cur)
                if cur==app.startPos:
                    break
                i+=1
                if i>app.rows*app.cols:
                    print("broke")
                    return None
            print("DONE")
            path.reverse()
            return path
        
        # * for each neighbor
        for drow,dcol in [(1,0),(0,1),(-1,0),(0,-1)]:
            row,col=node
            nrow,ncol=row+drow,col+dcol
            if not (0<=nrow<app.rows and 0<=ncol<app.cols):
                continue
            if (nrow,ncol) in visited:
                continue
            if app.board[nrow][ncol]!="p" and app.board[nrow][ncol]!='e':
                continue
            visited.add((nrow,ncol))
            queue.append((nrow,ncol))
            map[(nrow,ncol)]=node
    # print(visited)
    # print(map)
    # return "no path"



            

# ! not used
# def round(num, limit):
#     return int((num+limit//2)>=limit)*limit


# * returns a board (for now hardcoded)
def getBoard():
    x= [['s','g','g','g','g'],
        ['p','p','p','p','g'],
        ['g','g','g','p','g'],
        ['g','p','p','p','g'],
        ['e','p','g','g','g']]
    return x

"""
start at start, pick random direction, keep going until hit end (base case)
can add weighting for how much to go toward end
"""

# * inspired by knights tour
def genBoardPath(rows, cols, start, end, path, depth=0):
    # * base case
    if start==end:
        return path
    
    
    L=[(1,0),(0,1),(-1,0),(0,-1)]
    for _ in range(depth+int(math.sqrt(rows*cols)/2)):
        L.append(findPathToEnd(start,end))
    random.shuffle(L)
    # print(L)
    for drow,dcol in L:
        row,col=start
        nrow,ncol=row+drow,col+dcol
        
        # * out of bounds
        if not (0<=nrow<rows and 0<=ncol<cols):
            continue
        # * already visited
        if path[nrow][ncol]=='p':
            continue
        # print(nrow,ncol)
        path[nrow][ncol]='p'
        res=genBoardPath(rows, cols, (nrow, ncol), end, path, depth+1)
        if res != None:
            return res
        path[nrow][ncol]='g'

    return 


# * returns sign of n
def sign(n):
    if n>0:
        return 1
    if n<0:
        return -1
    return 0

# * returns closest direction to end
def findPathToEnd(pos,end):
    row,col=pos
    erow,ecol=end
    
    rDist,cDist=abs(row-erow),abs(col-ecol)
    
    closer=0,0
    if min(rDist,cDist)==rDist and rDist!=0:
        closer= (1 * sign(erow-row),0)
    else:
        closer=(0,1*sign(ecol-col))
    return closer
    
# print(findPathToEnd((3,2),(3,0)))
    

def genBoard(app,rows,cols):
    startPos=endPos=0,0
    while startPos==endPos:
        startPos=random.randint(0,1)*(rows-1),random.randint(0,1)*(cols-1)
        endPos=random.randint(0,1)*(rows-1),random.randint(0,1)*(cols-1)
    
    # print(startPos,endPos)
    app.startPos=startPos
    app.endPos=endPos
    
    x=genBoardPath(rows, cols, startPos, endPos,
                 [['g']*cols for _ in range(rows)])
    row,col=startPos
    x[row][col]='s'
    row,col=endPos
    x[row][col]='e'
    if x != None:
        return x
    return getBoard()
    
# x=(genBoard(4,4))
# print(x)
# for _ in x:
#     print(_)

# * returns a dictionary of the data using first row as the keys
def parseDataString(data,idx):
    d={}
    splitData=data[idx].split(',')
    for i in range(len(splitData)):
        stat=splitData[i]
        if stat[0].isdigit():
            stat=eval(stat)
        d[data[0].split(',')[i]]=stat
    return d

# * loads the sprite
def loadImage(self,path,scale):
    app=self.app
    # * images: https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#imageMethods
    # * transparency and rotation: https://pillow.readthedocs.io/en/stable/reference/Image.html

    self.image=app.loadImage(path)
    self.image.apply_transparency()
    self.image=app.scaleImage(self.image,scale)


# * from https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
def pointInGrid(app, x, y):
    # return True if (x, y) is inside the grid defined by app.
    return ((app.margin <= x <= app.width-app.margin) and
            (app.margin <= y <= app.height-app.margin))
    
def getCell(app, x, y):
    # aka "viewToModel"
    # return (row, col) in which (x, y) occurred or (-1, -1) if outside grid.
    if (not pointInGrid(app, x, y)):
        return (-1, -1)
    gridWidth  = app.width - 2*app.margin
    gridHeight = app.height - 2*app.margin
    cellWidth  = gridWidth / app.cols
    cellHeight = gridHeight / app.rows

    # Note: we have to use int() here and not just // because
    # row and col cannot be floats and if any of x, y, app.margin,
    # cellWidth or cellHeight are floats, // would still produce floats.
    row = int((y - app.margin) / cellHeight)
    col = int((x - app.margin) / cellWidth)

    return (row, col)

def getCellBounds(app, row, col):
    # aka "modelToView"
    # returns (x0, y0, x1, y1) corners/bounding box of given cell in grid
    gridWidth  = app.width - 2*app.margin
    gridHeight = app.height - 2*app.margin
    cellWidth = gridWidth / app.cols
    cellHeight = gridHeight / app.rows
    x0 = app.margin + col * cellWidth
    x1 = app.margin + (col+1) * cellWidth
    y0 = app.margin + row * cellHeight
    y1 = app.margin + (row+1) * cellHeight
    return (x0, y0, x1, y1)

# * gets the coords of center of cell
def getCenter(app,row,col):
        x0,y0,x1,y1=getCellBounds(app, row, col)
        x=(x0+x1)/2
        y=(y0+y1)/2
        return x,y