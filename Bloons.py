# from gameMode import getCellBounds,parseDataString,getCenter
from functions import *
from Projectile import *

class Bloons:
    # * direction priority
    # directions=['e','s','n','w']
    # directions=[(1,0),(0,1),(0,-1),(-1,0)]
    
    
    # * spd, color
    bloonsData=["spd,color,img","1,red,Assets/redbloon.png",
                "1.4,blue,Assets/bluebloon.png"]
    
    def __init__(self,app,pos,type=1,dir=(1,0)):
        self.app=app
        self.pos=pos
        self.type=type
        self.setType(type)
        # self.dir=Bloons.directions[dir]
        self.dir=dir
        self.r=25
        
        self.setAbsPos()
        self.path=copy.copy(app.path)
        
        


    # * sets the stats of bloons in a dict
    def setType(self,type):
        data=parseDataString(Bloons.bloonsData,type)
        self.data=data
        
        self.img=data['img']
        loadImage(self,self.img,1/2)
        
        # * change sprite
    
    # * whenever a bloon is hit
    def pop(self,dmg):
        self.type-=dmg
        if self.type<=0:
            self.type=0
            # * play pop noise
            print("Pop!")
            self.app.bloonsPopped+=1
            return True
        self.setType(self.type)
        
    # * takes in a projectile and checks collision (for now just check if in same box)
    def checkCollision(self,other):
        # row,col=self.pos
        if not isinstance(other, Projectile):
            # print("not proj")
            return
        # (x0, y0, x1, y1)=getCellBounds(self.app,row,col)
        # x,y=other.pos
        # if x0<x<x1 and y0<y<y1:
        if math.dist(other.pos,self.absPos)<=self.r:
            print(f"{math.dist(other.pos,self.pos)<=self.r} dist:{math.dist(other.pos,self.pos)}")
            return self.pop(other.damage)
            
    def checkAllProjectiles(self):
        app=self.app
        for i in app.objects:
            if isinstance(i, Projectile):
                if self.checkCollision(i):
                    print("collided")
                    return True
        return False


    
    
    
      
    
    
    # # * go forward, if no path, try another direction, returns True if at 'e'
    # def move(self):
    #     board=self.app.board
    #     row,col=self.pos
    #     dRow,dCol=self.dir
    #     nRow,nCol=row+dRow,col+dCol
    #     if not isLegal((nRow,nCol),board): # * if hit a wall
    #         x=Bloons.directions
    #         random.shuffle(x) # * to avoid getting stuck
    #         for dRow,dCol in Bloons.directions:
    #             nRow,nCol=row+dRow,col+dCol
    #             if isLegal((nRow,nCol),board):
    #                 self.dir=(dRow,dCol)
    #                 break
    #     self.pos=nRow,nCol
    #     if board[nRow][nCol]=="e":
    #         self.app.health-=self.type
    #         return True
    #     return False
    
    # # * gets next pos of bloon
    # def getNextPos(self):
        # board=self.app.board
        # row,col=self.pos
        # dRow,dCol=self.dir
        # nRow,nCol=row+dRow,col+dCol
        # if not isLegal((nRow,nCol),board):
        #     for dRow,dCol in Bloons.directions:
        #         nRow,nCol=row+dRow,col+dCol
        #         if isLegal((nRow,nCol),board):
        #             # self.dir=(dRow,dCol)
        #             break
        # return nRow,nCol
    
    # * sets the absPos of bloon
    def setAbsPos(self):
        row,col=self.pos
        self.absPos=getCenter(self.app,row,col)
        return self.absPos
    
    # * draws the bloon
    def redraw(self, canvas):
        self.setAbsPos()
        x,y=self.absPos
        # print(f"bloons pos {self.absPos}")
        # canvas.create_oval(x-self.r,y-self.r,x+self.r,y+self.r,fill=self.data['color'])
        canvas.create_image(x, y, image=ImageTk.PhotoImage(self.image))
            
            
    def move(self):
        self.pos=self.path.pop(0)
        row,col=self.pos
        if self.app.board[row][col]=="e":
            self.app.health-=self.type
            return True
        return False
    
 
    
    def update(self):
        self.setAbsPos()
        x=self.checkAllProjectiles()
        # print(self.app.time,(self.data["spd"]*1000))
        if self.app.time%(self.data["spd"]*500)==0:
            return self.move()
        # TODO implement projectile collision
        return x
        
        
        
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