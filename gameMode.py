###########
# Game Mode
###########


from functions import *
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
        app.towers=app.round//2+1
        
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
        
    if event.key=='c':
        app.nextTower='closest'
    if event.key=='f':
        app.nextTower='first'
        
        
    if event.key=='`':
        app.debug= not app.debug
    # ! debugging
    if event.key=='w':
        app.timerDelay*=10
    if event.key=='s':
        app.timerDelay//=10
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

        

# * will if towers can/cant be placed at mouse location
def gameMode_mouseMoved(app, event):
    pass

# * click to place a tower
def gameMode_mousePressed(app, event):
    # print(event.x,event.y)
    row,col = getCell(app, event.x, event.y)
    placeTower(app, row, col)

# * places tower in cell
def placeTower(app, row, col):
    tower = Towers(app,(row,col),1)
    isLegal = isTowerLegal(app,row,col)
    if isLegal==True: 
        if app.towers==0:
            return
        app.towers-=1
        app.towersPlaced+=1
        app.objects.append(tower)
        print("placed")
    elif isLegal:
        app.towers+=1
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
    if app.health<=0:
        app.lose=True
    if app.win or app.lose:
        app.mode='gameOverMode'
    app.time+=app.timerDelay
    # app.objects=app.projectilesList+app.towersList+app.bloonsList
    # if app.bloonsList==[]:
    if app.bloons==0 and app.bloonsList==[]:
        app.inRound=False
        if app.round==10:
            app.win=True
        # print("not in round")
    # if not typeExists(app, Bloons):
    #     app.inRound=False
    
    # print(app.bloonsList)
    
    if app.inRound:

        # * place bloons
        if app.bloons>0:
            if app.time%1000==0:
                if app.round>4:
                    if app.time%2000==0:
                        app.bloonsList.append(Bloons(app,app.startPos,2))
                        app.bloons-=1
                    else:
                        app.bloonsList.append(Bloons(app,app.startPos,1))
                        app.bloons-=1
                else:
                    app.bloonsList.append(Bloons(app,app.startPos,1))
                    app.bloons-=1
                        
                
  
        
        # * remove bloons if popped or reach end
        res=[]
        for bloon in app.bloonsList:
            if not bloon.update():
                # print("moved")
                res.append(bloon)
            else:
                print("removing")
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

# ! not used
def populateBloons(app):
    # app.round=-9
    # for i in range(app.round+10):
    #     app.bloonsList.append(Bloons(app,(0,0),1))
        # app.objects.append(Bloons(app,(0,0),1))
    print("meow")
    if app.time%10:
        print(app.startPos)
        app.bloonsList.append(Bloons(app,app.startPos,1))
        if app.round>5 and app.time%15:
            app.bloonsList.append(Bloons(app,app.startPos,2))

        






def drawBoard(app, canvas):
    board=app.board
    for i in range(app.rows):
        for j in range(app.cols):
            bounds=getCellBounds(app,i,j)
            cell=board[i][j]
            if cell=="g":
                fill='green'
            elif cell=='p':
                fill='LightGoldenrod4'
            elif cell=='e':
                if app.debug:
                    fill='yellow'
                else:
                    fill='LightGoldenrod4'
            elif cell=='s':
                if app.debug:
                    fill='chartreuse'
                else:
                    fill='LightGoldenrod4'
            canvas.create_rectangle(bounds,fill=fill)
            
    
def drawObjects(app, canvas):
    objects=app.objects+app.bloonsList
    for obj in objects:
        obj.redraw(canvas)

def drawInfo(app, canvas):
    canvas.create_text(0,0,anchor='nw',text=f"Health: {app.health}", font="Comic\ Sans\ MS\ 30\ Bold")
    canvas.create_text(app.width,0,anchor='ne',text=f"Round: {app.round}", font="Comic\ Sans\ MS\ 30\ Bold")
    canvas.create_text(app.width,app.height,anchor='se',text=f"Towers Left: {app.towers}", font="Comic\ Sans\ MS\ 30\ Bold")
    canvas.create_text(0,app.height,anchor='sw',text=f"Bloons Left: {len(app.bloonsList)+app.bloons}", font="Comic\ Sans\ MS\ 30\ Bold")
    canvas.create_text(app.width/2,app.height,fill="yellow",anchor='s',text=f"Target {app.nextTower}", font="Comic\ Sans\ MS\ 30\ Bold")
    
    if not app.inRound:
        canvas.create_text(app.width/2,0,anchor='n',text="Press space to start round!", font="Comic\ Sans\ MS\ 40\ Bold")
    


# * draw the board
def gameMode_redrawAll(app, canvas):
    drawBoard(app, canvas)
    drawObjects(app, canvas)
    drawInfo(app, canvas)
   

