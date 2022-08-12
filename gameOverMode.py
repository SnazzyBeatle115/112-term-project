from functions import restart
def drawGameOver(app, canvas):
    canvas.create_rectangle(0,0,app.width,app.height,fill="black")
    text="Game Over!"
    if app.win:
        text="You won!"
    elif app.lose:
        text="You lost!"
    canvas.create_text(app.width/2,app.height/2,fill="yellow",text=text, font="Comic\ Sans\ MS\ 50\ Bold")
    canvas.create_text(app.width,0,fill="yellow",anchor='ne',text=f"Round: {app.round}", font="Comic\ Sans\ MS\ 30\ Bold")
    canvas.create_text(app.width,app.height,fill="yellow",anchor='se',text=f"Towers Placed: {app.towersPlaced}", font="Comic\ Sans\ MS\ 30\ Bold")
    canvas.create_text(0,app.height,fill="yellow",anchor='sw',text=f"Bloons Popped: {app.bloonsPopped}", font="Comic\ Sans\ MS\ 30\ Bold")

def gameOverMode_redrawAll(app,canvas):
    drawGameOver(app,canvas)
    
def gameOverMode_keyPressed(app, event):
    if event.key=='r':
        restart(app)