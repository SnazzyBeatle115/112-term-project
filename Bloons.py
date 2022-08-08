class Bloons:
    # * direction priority
    # directions=['e','s','n','w']
    directions=[(1,0),(0,1),(0,-1),(-1,0)]
    
    # * spd, color
    bloonsData=["spd,color","1,red","1.4,blue"]
    
    def __init__(self,pos,type=1,dir=(1,0)):
        self.type=type
        self.setType(type)
        
        # self.dir=Bloons.directions[dir]
        self.dir=dir
        self.pos=pos
        self.r=25

    # * sets the stats of bloons in a dict
    def setType(self,type):
        data=parseDataString(Bloons.bloonsData,type)
        self.data=data
        # * change sprite
    
    # * whenever a bloon is hit
    def pop(self,dmg):
        self.type-=dmg
        if self.type<=0:
            # * play pop noise
            return
        self.setType(self.type)
        
    # * takes in a projectile and checks collision (for now just check if in same box)
    def checkCollision(self,other):
        row,col=self.pos
        if not isinstance(other, Projectile):
            return
        (x0, y0, x1, y1)=getCellBounds(app,row,col)
        x,y=other.pos
        if x0<x<x1 and y0<y<y1:
            self.pop(other.damage)
            
    
    # * go forward, if no path, try another direction, returns True if at 'e'
    def move(self,board):
        row,col=self.pos
        dRow,dCol=self.dir
        nRow,nCol=row+dRow,col+dCol
        if not isLegal((nRow,nCol),board):
            for dRow,dCol in Bloons.directions:
                nRow,nCol=row+dRow,col+dCol
                if isLegal((nRow,nCol),board):
                    self.dir=(dRow,dCol)
                    break
        self.pos=nRow,nCol
        return board[nRow][nCol]=="e"
            
def isLegal(pos,board):
    row,col=pos
    return 0<=row<len(board) and 0<=col<len(board[0]) and (board[row][col]=="p" or board[row][col]=="e")

    
        

# TODO can move this somewhere else so it can work with both classes
def parseDataString(data,idx):
    d={}
    splitData=data[idx].split(',')
    for i in range(len(splitData)):
        stat=splitData[i]
        if stat[0].isdigit():
            stat=eval(stat)
        d[data[0].split(',')[i]]=stat
    return d
            
            
# b = Bloons((0,0),2)
# print(b.data)
# b.pop(1)
# print(b.data)
# print(b.pos)
# board=[['p','p','g'],
#        ['g','p','e']]
# for i in range(4):
#     print(b.move(board))
#     print(b.pos)
# print((1,2)+(3,4))