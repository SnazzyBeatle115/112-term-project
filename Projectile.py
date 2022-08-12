class Projectile:
    
    def __init__(self, app, dmg, pierce, start, end, speed, size):
        self.app=app
        self.damage=dmg
        self.hp=pierce
        self.start=start
        self.end=end
        self.speed=speed
        self.size=size
        self.pos=start
        self.path=findMidpoints(start, end, 5)
    
        
    def move(self):
        x,y=self.pos
        tx,ty=self.end
        if (x,y)==(tx,ty):
            return True
        
        xDist,yDist=tx-x,ty-y
        
        x+=xDist/self.speed
        y+=yDist/self.speed

        self.pos=x,y
        
        # if len(self.path)==0:
        #     return
        # self.pos=self.path[0]
        # self.path.pop(0)

    def update(self):
        # if self.app.time%(self.speed)==0: 
            # self.move()
            # print("projectile moving")
            # print(self.pos)
        self.move()
        x,y=self.pos
        # print(self.pos)
        if 0>x>self.app.width or 0>y>self.app.height or self.app.inRound==False:
            return True
            # TODO or collided

    def redraw(self, canvas):
        x,y=self.pos
        canvas.create_rectangle(x-self.size,y-self.size,x+self.size,y+self.size,fill="black")
    
def findMidpoints(start,end,midpoints):
    res=[]
    for i in range(1,midpoints+2):
        sx,sy=start
        ex,ey=end
        x=sx-(sx-ex)/(midpoints+1)*i
        y=sy-(sy-ey)/(midpoints+1)*i
        res.append((x,y))
    return res
   
   
   
# x=(Projectile(1,1,(1,2),
#                           (1,2),3,25))
# print(x.speed)

# print(findMidpoints((0,0),(10,10),2))

# x=Projectile(1,(0,0),(10,10),3,1)
# print(x.path)
# print(x.pos)
# for i in range(4):
#     x.move()
#     print(x.pos)




# def abc(a):
#     yield a
#     yield a*2

# x=abc(1)
# print(next(x))
# print(next(x))

# if not None:
#     print(x)