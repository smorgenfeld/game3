#shop.py

from graphics import *
import buttons,time

def shop(win):
    global back,forwards,op1,op2,op3,op4,op5,op6,op7,op8,op9,op10, unlocks, backback
    #get the save data
    savefiler = open('resources/save.txt','r')
    high_score = savefiler.readline()
    caish = eval(savefiler.readline())
    unlocks = savefiler.readline()
    selected_skin = savefiler.readline()
    savefiler.close()
    costs = [10,10,25,25,50,50,100,100,250,500]
    names = ['Red','Yellow','Rafi']
    l1 = Text(Point(960,1000),'Shop');l1.setFace('helvetica');l1.setSize(30);l1.draw(win)
    back = Rectangle(Point(100,200),Point(200,900));back.setFill('grey');back.draw(win)
    forwards = Rectangle(Point(1700,200),Point(1800,900));forwards.setFill('grey');forwards.draw(win)
    op1 = Rectangle(Point(200,550),Point(500,900));op1.draw(win)
    op2 = Rectangle(Point(500,550),Point(800,900));op2.draw(win)
    op3 = Rectangle(Point(800,550),Point(1100,900));op3.draw(win)
    op4 = Rectangle(Point(1100,550),Point(1400,900));op4.draw(win)
    op5 = Rectangle(Point(1400,550),Point(1700,900));op5.draw(win)
    op6 = Rectangle(Point(200,200),Point(500,550));op6.draw(win)
    op7 = Rectangle(Point(500,200),Point(800,550));op7.draw(win)
    op8 = Rectangle(Point(800,200),Point(1100,550));op8.draw(win)
    op9 = Rectangle(Point(1100,200),Point(1400,550));op9.draw(win)
    op10 = Rectangle(Point(1400,200),Point(1700,550));op10.draw(win)
    backback = Rectangle(Point(760,50),Point(1160,150));backback.draw(win)
    Text(Point(350,600),'Cost: '+str(costs[0])).draw(win)
    Text(Point(650,600),'Cost: '+str(costs[1])).draw(win)
    Text(Point(950,600),'Cost: '+str(costs[2])).draw(win)
    Text(Point(1250,600),'Cost: '+str(costs[3])).draw(win)
    Text(Point(1550,600),'Cost: '+str(costs[4])).draw(win)
    Text(Point(350,250),'Cost: '+str(costs[5])).draw(win)
    Text(Point(650,250),'Cost: '+str(costs[6])).draw(win)
    Text(Point(950,250),'Cost: '+str(costs[7])).draw(win)
    Text(Point(1250,250),'Cost: '+str(costs[8])).draw(win)
    Text(Point(1550,250),'Cost: '+str(costs[9])).draw(win)
    Text(Point(960,100),'Back').draw(win)
    clicks = [back,forwards,op1,op2,op3,op4,op5,op6,op7,op8,op9,op10,backback]
    yay = True
    while yay:
        click = win.getMouse()
        for i in range(len(clicks)):
            yay,sel = getClicked(clicks[i],click)
            if yay != True:
                overlay(sel,costs,caish,names,selected_skin,high_score,win)
    

def overlay(selection,costs,caish,names,selected_skin,high_score,win):
    if selection == op1:
        sel = 1
    elif selection == op2:
        sel =2
    elif selection == op3:
        sel =3
    elif selection == op4:
        sel =4
    elif selection == op5:
        sel =5
    elif selection == op6:
        sel =6
    elif selection == op7:
        sel =7
    elif selection == op8:
        sel =8
    elif selection == op9:
        sel = 9
    elif selection == op10:
        sel = 10
    elif selection == forwards:
        return
    elif selection == back:
        return
    elif selection == backback:
        backback.setFill('grey')
        time.sleep(.2)
        win.clear()
        savefilew = open('resources/save.txt','w')
        print(high_score,file=savefilew,end='')
        print(caish,file=savefilew)
        print(unlocks,file=savefilew,end='')
        print(selected_skin,file=savefilew)
        savefilew.close()
        return
    if selected_skin == sel or not unlocks[sel-1]:
        selectable = False
    else:
        selectable = True
    overekt = Rectangle(Point(310,250),Point(1610, 900));overekt.setFill('lightgrey');overekt.setWidth(2);overekt.draw(win)
    l2 = Text(Point(960,300),'Total Caish: '+str(caish));l2.setFace('helvetica');l2.setSize(20);l2.draw(win)
    l3 = Text(Point(960,800),names[sel-1]);l3.setFace('helvetica');l3.setSize(25);l3.draw(win)
    if not unlocks[sel-1] and caish >= cost[sel-1]:
        buyable = True
    else:
        buyable = False
    yay = buttons.buttonChoice3(350,350,1570,750,'Buy','Equip','Back',win,True,b1e = buyable,b2e=selectable)
    if yay == 1:
        caish -= cost[sel-1]
        unlocks[sel-1] = True
        selected_skin = sel
    elif yay == 2:
        selected_skin = sel
    l2.undraw();l3.undraw();overekt.undraw()
    savefilew = open('resources/save.txt','w')
    print(high_score,file=savefilew,end='')
    print(caish,file=savefilew)
    print(unlocks,file=savefilew,end='')
    print(selected_skin,file=savefilew)
    savefilew.close()

def getClicked(rekt,click):
    p1 = rekt.getP1()
    p2 = rekt.getP2()
    p1x = p1.getX();p1y = p1.getY()
    p2x = p2.getX();p2y=p2.getY()
    mx = click.getX();my = click.getY()
    if mx > p1x and mx < p2x and my > p1y and my < p2y:
        return False,rekt
    else:
        return True, None
