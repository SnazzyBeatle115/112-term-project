###########
# Game Mode
###########
# from Main import appStarted



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



from Bloons import *
from Towers import *
from Projectile import *

def gameMode_keyPressed(app, event):
    print(event.key)
    # if event.key == 'b':
    #     print("place monkey")
    if event.key=='Space' and not app.inRound:
        print("populating")
        # populateBloons(app)
        app.inRound=True
        app.round+=1
        app.bloons=app.round+10
    # if event.key=='p':
    #     app.objects.append()
    if event.key=="Escape":
        app.mode="pausedMode"
    if event.key=='r':
        restart(app)
        # restart round
        
        
    # ! debugging
    if event.key=='x':
        app.bloonsList.append(Bloons(app,(1,2),1))
    if event.key=='k':
        for i in app.objects:
            if isinstance(i,Towers):
                i.changeTargeting('closest')
    if event.key=='l':
        for i in app.objects:
            if isinstance(i,Towers):
                i.changeTargeting('first')

def restart(app):
    # * game info
    app.mode = 'splashScreenMode'
    app.time = 0
    app.timerDelay = 100
    
    # app.board=getBoard()
    app.rows=len(app.board)
    app.cols=len(app.board[0])
    app.margin=10   
    
    app.inRound=False
    app.round=0
    app.win=False
    app.health=0
    
    app.bloons=0
    
    app.objects=[]
    app.bloonsList=[]
    app.towersList=[]
    # app.projectilesList=[]
        
        

# * will if towers can/cant be placed at mouse location
def gameMode_mouseMoved(app, event):
    pass

# * click to place a tower
def gameMode_mousePressed(app, event):
    print(event.x,event.y)
    row,col = getCell(app, event.x, event.y)
    placeTower(app, row, col)

# * places tower in cell
def placeTower(app, row, col):
    tower = Towers(app,(row,col),1)
    isLegal = isTowerLegal(app,row,col)
    if isLegal==True: 
        app.objects.append(tower)
        print("placed")
    elif isLegal:
        app.objects.remove(isLegal)
        print("removed")
    
# * returns legality of tower
def isTowerLegal(app, row, col):
    board=app.board
    if board[row][col]!='g':
        return False
    
    for i in app.objects:
        if isinstance(i,Towers) and i.pos==(row,col):
            return i
    return True

def gameMode_timerFired(app):
    if app.round==10:
        app.win=True
    if app.win:
        return
    app.time+=app.timerDelay
    # app.objects=app.projectilesList+app.towersList+app.bloonsList
    # if app.bloonsList==[]:
    if app.bloons==0 and app.bloonsList==[]:
        app.inRound=False
        # print("not in round")
    # if not typeExists(app, Bloons):
    #     app.inRound=False
    
    # print(app.bloonsList)
    
    if app.inRound:
        
        if app.bloons>0:
            if app.time%1000==0:
                app.bloonsList.append(Bloons(app,(0,0),1))
                app.bloons-=1
                
        
        res=[]
        for bloon in app.bloonsList:
            if not bloon.update():
                # print("moved")
                res.append(bloon)
        app.bloonsList=res
        
    res=[]
    for obj in app.objects:
        # x=obj.update()
        # y=obj.pos
        # print(x,y)
        if not obj.update():
            res.append(obj)
            # print("adding")
            
    app.objects=res

def typeExists(app, type):
    for i in app.objects:
        if isinstance(i, type):
            return True
    return False
    
# * fills bloon list
# TODO stagger spawns
def populateBloons(app):
    # app.round=-9
    # for i in range(app.round+10):
    #     app.bloonsList.append(Bloons(app,(0,0),1))
        # app.objects.append(Bloons(app,(0,0),1))
    
    if app.time%10:
        app.bloonsList.append(Bloons(app,(0,0),1))
        






def drawBoard(app, canvas):
    board=app.board
    for i in range(app.rows):
        for j in range(app.cols):
            bounds=getCellBounds(app,i,j)
            cell=board[i][j]
            if cell=="g":
                fill='green'
            elif cell=='p':
                fill='brown'
            elif cell=='e':
                fill='yellow'
            elif cell=='s':
                fill='chartreuse'
            canvas.create_rectangle(bounds,fill=fill)
            
    
def drawObjects(app, canvas):
    objects=app.objects+app.bloonsList
    for obj in objects:
        obj.redraw(canvas)

def drawInfo(app, canvas):
    canvas.create_text(0,0,anchor='nw',text=f"Health: {app.health}", font="Comic\ Sans\ MS\ 30\ Bold")
    canvas.create_text(app.width,0,anchor='ne',text=f"Round: {app.round}", font="Comic\ Sans\ MS\ 30\ Bold")
    if not app.inRound:
        canvas.create_text(app.width/2,0,anchor='n',text="Press space to start round!", font="Comic\ Sans\ MS\ 40\ Bold")
    
def drawWin(app, canvas):
    if not app.win:
        return
    canvas.create_rectangle(0,0,app.width,app.height,fill="black")
    canvas.create_text(app.width/2,app.height/2,fill="yellow",text="You win!", font="Comic\ Sans\ MS\ 50\ Bold")
    

# * draw the board
def gameMode_redrawAll(app, canvas):
    drawBoard(app, canvas)
    drawObjects(app, canvas)
    drawInfo(app, canvas)
    drawWin(app, canvas)

