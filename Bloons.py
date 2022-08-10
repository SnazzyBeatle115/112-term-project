from gameMode import getCellBounds,parseDataString
from Projectile import *

class Bloons:
    # * direction priority
    # directions=['e','s','n','w']
    directions=[(1,0),(0,1),(0,-1),(-1,0)]
    
    # * spd, color
    bloonsData=["spd,color","1,red","1.4,blue"]
    
    def __init__(self,app,pos,type=1,dir=(1,0)):
        self.app=app
        self.pos=pos
        self.type=type
        self.setType(type)
        # self.dir=Bloons.directions[dir]
        self.dir=dir
        self.r=25
        
        self.setAbsPos()


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
        (x0, y0, x1, y1)=getCellBounds(self.app,row,col)
        x,y=other.pos
        if x0<x<x1 and y0<y<y1:
            self.pop(other.damage)

            
    
    # * go forward, if no path, try another direction, returns True if at 'e'
    def move(self):
        board=self.app.board
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
    
    # * gets next pos of bloon
    def getNextPos(self):
        board=self.app.board
        row,col=self.pos
        dRow,dCol=self.dir
        nRow,nCol=row+dRow,col+dCol
        if not isLegal((nRow,nCol),board):
            for dRow,dCol in Bloons.directions:
                nRow,nCol=row+dRow,col+dCol
                if isLegal((nRow,nCol),board):
                    # self.dir=(dRow,dCol)
                    break
        return nRow,nCol
    
    # * sets the absPos of bloon
    def setAbsPos(self):
        app=self.app
        row,col=self.pos
        x0,y0,x1,y1=getCellBounds(app, row, col)
        x=(x0+x1)/2
        y=(y0+y1)/2
        self.absPos=x,y
    
    # * draws the bloon
    def redraw(self, canvas):
        self.setAbsPos()
        x,y=self.absPos
        # print(f"bloons pos {self.absPos}")
        canvas.create_oval(x-self.r,y-self.r,x+self.r,y+self.r,fill=self.data['color'])
            
    def update(self):
        # print(self.app.time,(self.data["spd"]*1000))
        if self.app.time%(self.data["spd"]*500)==0:
            return self.move()
        # TODO implement projectile collision
        # return self.checkCollision()
        
        
        
def isLegal(pos,board):
    row,col=pos
    return 0<=row<len(board) and 0<=col<len(board[0]) and (board[row][col]=="p" or board[row][col]=="e")

    
        

            
            
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