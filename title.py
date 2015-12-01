#title screen

import buttons
from graphics import *

def title(ww,hh,full,start,gin):
    if start == True:
        win = GraphWin('hi',ww,hh,fullscreen=full)
        win.setCoords(0,0,1920,1080)
        l1 = Text(Point(960,600),'Game3')
        l1.setFace('helvetica');l1.setSize(35);l1.draw(win)
        c = buttons.buttonChoice(20,280,1900,400,'Play','Quit',win,True)
        if c == 1:
            l1.undraw()
            return win
        else:
            quit()
    else:
        gin.delete('all')
        l1 = Text(Point(960,600),'Game3')
        l1.setFace('helvetica');l1.setSize(35);l1.draw(win)
        c = buttons.buttonChoice(20,280,1900,400,'Play','Quit',win,True)
        if c == 1:
            l1.undraw()
            return win
        else:
            quit()
