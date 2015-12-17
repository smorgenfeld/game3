#buttons!

from graphics import *
from time import *

def button(p1x,p1y,p2x,p2y,text,win,undraw):
    rekt = Rectangle(Point(p1x,p1y),Point(p2x,p2y))
    rekt.draw(win)
    lab = Text(Point(((p1x+p2x)/2),((p1y+p2y)/2)),text);lab.draw(win)
    i = False
    while i == False:
        x=win.getMouse()
        if x.getX() >= p1x and x.getX() <= p2x:
            if x.getY() >= p1y and x.getY() <= p2y:
                rekt.setFill('grey')
                sleep(.2)
                rekt.setFill('white')
                if undraw == True:
                    sleep(.2)
                    rekt.undraw()
                    lab.undraw()
                return

def buttonChoice(p1x,p1y,p2x,p2y,text1,text2,win,undraw):
    rekt1 = Rectangle(Point(p1x,p1y),Point((p1x+p2x)/2-((p1x+p2x)/40),p2y))
    rekt2 = Rectangle(Point((p1x+p2x)/2+((p1x+p2x)/40),p1y),Point(p2x,p2y))
    rekt1.draw(win),rekt2.draw(win)
    lab1 = Text(Point((rekt1.getCenter()).getX(),(rekt1.getCenter()).getY()),text1);lab1.draw(win)
    lab2 = Text(Point((rekt2.getCenter()).getX(),(rekt2.getCenter()).getY()),text2);lab2.draw(win)
    i = False
    while i == False:
        x=win.getMouse()
        if x.getX() >= p1x and x.getX() <= (p1x+p2x)/2-((p1x+p2x)/40):
            if x.getY() >= p1y and x.getY() <= p2y:
                rekt1.setFill('grey')
                sleep(.2)
                rekt1.setFill('white')
                if undraw == True:
                    rekt1.undraw();rekt2.undraw();lab1.undraw();lab2.undraw()
                return 1
        elif x.getX() >= (p1x+p2x)/2+((p1x+p2x)/40) and x.getX() <= p2x:
            if x.getY() >= p1y and x.getY() <= p2y:
                rekt2.setFill('grey')
                sleep(.2)
                rekt2.setFill('white')
                if undraw == True:
                    rekt1.undraw();rekt2.undraw();lab1.undraw();lab2.undraw()
                return 2
def buttonChoice3(p1x,p1y,p2x,p2y,text1,text2,text3,win,undraw,b1e=True,b2e=True,b3e=True):
    rekt1 = Rectangle(Point(p1x,(p1y+p2y)/2+20),Point((p1x+p2x)/2-((p1x+p2x)/40),p2y))
    rekt2 = Rectangle(Point((p1x+p2x)/2+((p1x+p2x)/40),(p1y+p2y)/2+20),Point(p2x,p2y))
    rekt3 = Rectangle(Point(p1x+((p2x-p1x)/4),p1y),Point(p1x+(3*(p2x-p1x)/4),(p2y+p1y)/2-20))
    rekt1.draw(win),rekt2.draw(win),rekt3.draw(win)
    lab1 = Text(Point((rekt1.getCenter()).getX(),(rekt1.getCenter()).getY()),text1);lab1.draw(win)
    lab2 = Text(Point((rekt2.getCenter()).getX(),(rekt2.getCenter()).getY()),text2);lab2.draw(win)
    lab3 = Text(Point((rekt3.getCenter()).getX(),(rekt3.getCenter()).getY()),text3);lab3.draw(win)
    if not b1e:
        rekt1.setFill('grey')
    if not b2e:
        rekt2.setFill('grey')
    if not b3e:
        rekt3.setFill('grey')
    i = False
    while i == False:
        x=win.getMouse()
        if b1e and x.getX() >= p1x and x.getX() <= (p1x+p2x)/2-((p1x+p2x)/40):
            if x.getY() >= (p1y+p2y)/2+20 and x.getY() <= p2y:
                rekt1.setFill('grey')
                sleep(.2)
                rekt1.setFill('white')
                if undraw == True:
                    rekt1.undraw();rekt2.undraw();rekt3.undraw();lab1.undraw();lab2.undraw(),lab3.undraw()
                return 1
        elif b2e and x.getX() >= (p1x+p2x)/2+((p1x+p2x)/40) and x.getX() <= p2x:
            if x.getY() >= (p1y+p2y)/2+20 and x.getY() <= p2y:
                rekt2.setFill('grey')
                sleep(.2)
                rekt2.setFill('white')
                if undraw == True:
                    rekt1.undraw();rekt2.undraw();rekt3.undraw();lab1.undraw();lab2.undraw(),lab3.undraw()
                return 2
        elif b3e and x.getX() >= p1x+((p2x-p1x)/4) and x.getX() <= p1x+(3*(p2x-p1x)/4):
            if x.getY() >= p1y and x.getY() <= (p2y+p1y)/2-20:
                rekt3.setFill('grey')
                sleep(.2)
                rekt3.setFill('white')
                if undraw == True:
                    rekt1.undraw();rekt2.undraw();rekt3.undraw();lab1.undraw();lab2.undraw();lab3.undraw()
                return 3
