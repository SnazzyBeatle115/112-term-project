
# * user can go back to splash or game modes
def pausedMode_mousePressed(app, event):
    if (app.width/5<event.x<app.width/5*2 and app.height/5<event.y<app.height/5*2):
        app.mode="splashScreenMode"
    elif (app.width/5*3<event.x<app.width/5*4 and app.height/5<event.y<app.height/5*2):
        app.mode="gameMode"
        
        

def pausedMode_redrawAll(app, canvas):
    canvas.create_rectangle(app.width/5,app.height/5,app.width/5*2,app.height/5*2,fill="orange")
    canvas.create_text(app.width/5*1.5,app.height/5*1.5,fill="blue",text="Home")
    canvas.create_rectangle(app.width/5*3,app.height/5,app.width/5*4,app.height/5*2,fill="green")
    canvas.create_text(app.width/5*1.5*3,app.height/5*1.5,fill="purple",text="Return")
    
    canvas.create_text(app.width/2,app.height/2, font="Comic\ Sans\ MS\ 30\ Bold",
                       text="Click to return to game\nClick on green cells to place towers.\nPress c to target closest and f to target first.\nProtect the end from incoming bloons!")