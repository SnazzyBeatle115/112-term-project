# from cmu_112_graphics import *
from splashScreenMode import * 
from gameMode import *
from pausedMode import *
from gameOverMode import *
# from Bloons import *
# from Towers import *
# from Projectile import *
from functions import *


def appStarted(app):
    restart(app)
    
    




# * save data
def appStopped(app):
    pass
    

# * runs the app
def playGame():
    runApp(width=600, height=600)

playGame()
