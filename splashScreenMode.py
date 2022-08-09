


# * if the player presses the play button, go to game mode
def splashScreenMode_mousePressed(app, event):
    print("clicked")
    if app.width*2/3>event.x>app.width/3 and app.height*2/3>event.y>app.height/3:
        app.mode="gameMode"
        print("go")

# * draw the splash screen
def splashScreenMode_redrawAll(app, canvas):
    canvas.create_rectangle(app.width/3,app.height/3,app.width*2/3,app.height*2/3,fill="green")
    canvas.create_text(app.width/2,app.height*2/5,text="Bloons Tower Defense")