from cmu_112_graphics import *
from Projectile import *
from gameMode import getCellBounds,parseDataString,getCenter
from Bloons import *
import math


class Towers:
    
    # type, damage, pierce, attack speed /s, range
    towerData = ["type,damage,pierce,attack speed,range",
               "dart,1,2,0.95,32",
               "wizard,1,3,1.1,"]
    
    def __init__(self,app,pos,type=1):
        self.app=app
        self.pos=pos
        self.setType(type)
        # * 0 = hovering, 1 = placed
        # self.state=0
        self.rotation=math.pi/2
        self.r=25
        self.range=300
        self.targeting='first'
    
   
        row,col=pos
        self.absPos=getCenter(self.app,row,col)

        self.loadImage()
        
    # * loads the sprite
    def loadImage(self):
        app=self.app
        # * images: https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#imageMethods
        # * transparency and rotation: https://pillow.readthedocs.io/en/stable/reference/Image.html

        self.image=app.loadImage('Assets/monkey.png')
        self.image.apply_transparency()
        self.image=app.scaleImage(self.image,1/5)
        
        
    # * sets the stats of towers in a dict
    def setType(self,type):
        data=parseDataString(Towers.towerData,type)
        self.data=data
        self.fill='brown'
        
    # TODO make some function to place towers (on mousePressed) and to hover towers, if holding a tower, make it transparent
    # TODO add hovering later

    def changeTargeting(self, targeting):
        self.targeting=targeting

    # * turn towards first bloon by rotating
    def turn(self,targetList):
        target=targetList[0]
        trow,tcol=target.pos
        row,col=self.pos
        
    # * target closest vs target first
    # * target closest uses best template and target first targets first in range
        
    # * fire projectile in a direction
    def fire(self):
        # print("fire")
        targets=self.bloonsInRange()
        if len(targets)>0:
            # print("found target")
            # print(self.absPos)
            if self.targeting=='closest':
                target=self.findClosest(targets)
                # print("closest:")
                # print(target.pos,target.absPos)
                # print(target)
            elif self.targeting=='first':
                target=targets[0]
            if target==None:
                return
            self.rotate(target)
            if self.app.time%(500)==0:
                # print("fired")
                self.app.objects.append(Projectile(self.app,self.data['damage'],self.absPos,
                          self.getDirectionTarget(),1,25))
    
    # * gets the coordinates of the target direction
    def getDirectionTarget(self):
        magnitude=self.app.width
        x=magnitude*math.cos(self.rotation)
        y=magnitude*math.sin(self.rotation)
        # print(f"target {x,y}")
        cx,cy=self.absPos
        # print(f'adjusted {x+cx,y+cy}')
        return (x+cx,y+cy)
        
    # * returns a list of bloons in range of tower
    def bloonsInRange(self):
        res=[]
        for i in self.app.bloonsList:
            if math.dist(i.absPos,self.absPos)<self.range:
                res.append(i)
        return res
    
    # * finds closest bloon
    def findClosest(self,L):
        bestBloon=None
        min=self.range
        for i in L:
            dist=math.dist(i.setAbsPos(),self.absPos)
            if dist<min:
                min=dist
                bestBloon=i
        return bestBloon
    
    # * atan2: https://docs.python.org/3/library/math.html#trigonometric-functions
    # * rotates to target direction
    def rotate(self, target):
        x,y=self.absPos
        tx,ty=target.setAbsPos()

        
        # temp=Bloons(self.app,target.getNextPos())
        
        # temp=Bloons(self.app,target.pos)
        # if self.targeting=="first":
        #     tx,ty=temp.absPos
        # tx,ty=temp.absPos
        # if self.targeting=="closest":
            # trow,tcol=temp.pos
            # print(f"nextpos{trow,tcol}")
            # tx,ty=getCenter(self.app,trow,tcol)
            # tx,ty=target.absPos 
        
        
        # print(f"target pos {target.pos,target.setAbsPos()}")
        # print(f"predicted pos {temp.pos,temp.absPos}")
        
        
        xDist,yDist=tx-x,ty-y
        theta=math.atan2(yDist,xDist)
        # if xDist==0:
        #     theta=math.pi/2 if yDist<0 else math.pi*3/2
        # elif yDist==0:
        #     theta=math.pi if xDist<0 else 0
        self.rotation=theta
        rotImg=-theta/math.pi*180-90
        # print(rotImg)
        self.loadImage()
        self.image=self.image.rotate(rotImg)
        
        # print(f"bloons pos {tx,ty}")
        # print(f"self pos {x,y}")
        # print(f"dist {xDist,yDist}")
        # print(f"rotation {theta}")

    
    def update(self):
        # if self.app.time%(self.data["attack speed"]*100)==0:
        # if self.app.time%(250)==0:
        #     self.fire()
        self.fire()
    
    def redraw(self, canvas):
        app=self.app
        x,y=self.absPos
        # canvas.create_oval(x-self.r,y-self.r,x+self.r,y+self.r,fill='saddle brown')
        canvas.create_oval(x-self.range,y-self.range,x+self.range,y+self.range,outline='gray',width=5,fill='')
        
        canvas.create_image(x, y, image=ImageTk.PhotoImage(self.image))
        
        canvas.create_text(x,y,text=self.targeting,font="Comic\ Sans\ MS\ 20\ Bold")
        # tx,ty=self.getDirectionTarget()
        # canvas.create_line(tx,ty,x,y,width=10)
  
 

# x=Towers(1,1,1)
# print(x.data)
# print("hi")

# print(type(eval("hi")))

# def f(a,b):
#     return a+b
# x=(1,2)
# print(f(x))