class Towers:
    
    # type, damage, pierce, attack speed /s, range
    towerData = ["type,damage,pierce,attack speed,range",
               "dart,1,2,.95,32",
               "wizard,1,3,1.1,"]
    
    def __init__(self,pos,type=1):
        self.setType(type)
        self.pos=pos
        # * 0 = hovering, 1 = placed
        # self.state=0
        
    # * sets the stats of towers in a dict
    def setType(self,type):
        data=parseDataString(Towers.towerData,type)
        self.data=data
        self.fill='brown'
        
    # TODO make some function to place towers (on mousePressed) and to hover towers, if holding a tower, make it transparent
    # TODO add hovering later
    
    def fire(self,target):
        return Projectile(self.data['damage'],self.pos,target,3,25)
        
        
    

# TODO can move this somewhere else so it can work with both classes
def parseDataString(data,idx):
    d={}
    splitData=data[idx].split(',')
    for i in range(len(splitData)):
        d[data[0].split(',')[i]]=splitData[i]
    return d        
 

x=Towers(1)

# print(type(eval("hi")))

# def f(a,b):
#     return a+b
# x=(1,2)
# print(f(x))