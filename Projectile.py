class Projectile:
    
    def __init__(self, dmg, start, end, speed, size):
        self.damage=dmg
        self.start=start
        self.end=end
        self.speed=speed
        self.size=size
        self.pos=start
        self.path=findMidpoints(start, end, speed)
    
        
    def move(self):
        if len(self.path)==0:
            return
        self.pos=self.path[0]
        self.path.pop(0)

        
def findMidpoints(start,end,midpoints):
    res=[]
    for i in range(1,midpoints+2):
        sx,sy=start
        ex,ey=end
        x=sx-(sx-ex)/(midpoints+1)*i
        y=sy-(sy-ey)/(midpoints+1)*i
        res.append((x,y))
    return res
   
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
