from cmu_112_graphics import *
from splashScreenMode import * 
from gameMode import *
from pausedMode import *
from Bloons import *
from Towers import *
from Projectile import *


def appStarted(app):
    restart(app)

def restart(app):
    # * game info
    app.mode = 'splashScreenMode'
    app.time = 0
    app.timerDelay = 100
    
    app.board=getBoard()
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
    
    

# * returns a board (for now hardcoded)
def getBoard():
    x= [['s','g','g','g','g'],
        ['p','p','p','p','g'],
        ['g','g','g','p','g'],
        ['g','p','p','p','g'],
        ['e','p','g','g','g']]
    return x



# * save data
def appStopped(app):
    pass
    

# * runs the app
def playGame():
    runApp(width=600, height=600)

playGame()
