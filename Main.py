from cmu_112_graphics import *

def appStarted(app):
    # game info
    app.mode = 'splashScreenMode'
    app.time = 0
    app.timerDelay = 10

# * save data
def appStopped(app):
    pass
    

# * runs the app
def playGame():
    runApp(width=800, height=800)
