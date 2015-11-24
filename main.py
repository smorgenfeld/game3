#game3.py

from graphics import *
from time import *
import tkinter, random, math, setup
import math
import random

def overlap(r1,r2,x,y):
    global falling,curx1,curx2
    r1cent = r1.getCenter()
    r1x = r1cent.getX()-15 + x
    r1y = r1cent.getY()+15 + y
    r2p1 = r2.getP1();r2p2 = r2.getP2()
    r2p1x = r2p1.getX()
    r2p2x = r2p2.getX()
    r2p1y = r2p1.getY()
    r2p2y = r2p2.getY()
    if r1x <= r2p2x and r1x+30 >= r2p1x and r1y >= r2p1y and r1y-30 <= r2p2y:
        if r1x-x >= r2p2x:
            x = (r1x-x)-r2p2x
        if r1x+30-x <= r2p1x:
            x = (r1x+30-x) - r2p1x
        if r1y-y <= r2p1y:
            y = r2p1y-(r1y-y)
        if r1y-30-y >= r2p2y:
            y = (r2p2y)-(r1y-30-y)
            falling = False
            curx1 = r2p1x
            curx2 = r2p2x
        return x,y
    else:
        return False

def keyup(e):
    global up,key
    up = True
    key = e.char
    
def keydown(e):
    global up,key
    up = False
    key = e.char

def butdown(event):
    global but
    but = True

def butup(event):
    global but
    but = False

class bullet:

    def __init__(self,x1,y1,x2,y2,v,rel,acur,reco):
        global nxt,tb,x,y,falling
        nxt = rel
        tb = 0
        ac = 1+ random.randint(-acur,acur)/100
        self.bar = None
        self.x = x1+10;self.y = y1+10
        self.reckt = Rectangle(Point(self.x-20,self.y-20),Point(self.x,self.y))
        self.reckt.setWidth(0);self.reckt.setFill('grey');self.reckt.draw(win)
        top = (y2 - y1)
        bottom = (x2 - x1)
        m = top/bottom*ac
        self.mx = math.cos(math.atan(m))*v
        self.my = math.tan(math.atan(m)) * self.mx
        if bottom < 0:
            self.my *= -1
            self.mx *= -1
        x += self.mx/reco
        if falling and self.my < y1:
            y += self.my/reco
            
    def mve(self):
        if self.bar == None:
            (self.reckt).move(self.mx,self.my)
            self.x += self.mx;self.y += self.my

    def getReckt(self):
        return self.reckt
            
    def close(self):
        if self.bar == None:
            self.reckt.undraw()
            self.bar = 'lol'
            
    def isclosed(self):
        if self.bar == None:
            return False
        else:
            return True
    def col(self,r2):
        if self.bar == None:
            r2p1 = r2.getP1();r2p2 = r2.getP2();r2cent = r2.getCenter()
            r2w = abs(r2p1.getX()-r2p2.getX())
            r2h = abs(r2p1.getY()-r2p2.getY())
            r2x = r2cent.getX() - r2w/2
            r2y = r2cent.getY() - r2h/2
            if (self.x <= r2x + r2w and self.x+20 >= r2x and self.y >= r2y and self.y-20 <= r2y+ r2h) or (self.x < -20 or self.x > 1940 or self.y < -10 or self.y > 1100):
                self.close()

def quickcol(x1,x2,y1,y2):
    if abs(x2-x1) > 100 and abs(y2-y1) > 100:
        return False
    else:
        return True

class slime:

    def __init__(self,win,initx,inity):
        self.rekt = Rectangle(Point(initx,inity),Point(initx+30,inity-30))
        self.rekt.setWidth(0);self.rekt.setFill('green');self.rekt.draw(win)
        self.falling = True
        self.cur = ''
        self.x = initx;self.y = inity
        self.mx = 0;self.my=0
        self.surge = 0
        self.bar = None

    def mvee(self,px,py,blocks,bult):
        global score
        if self.bar == None:
            if not falling and self.surge >= 50:
                if py+10 > self.y:
                    if px > self.x:
                        self.mx = 10
                    else:
                        self.mx = -10
                    self.my = random.randint(10,20)
                    self.falling = True
                else:
                    if px > self.x:
                        self.mx = 15
                    else:
                        self.mx = -15
                    self.my = 0
                self.surge = random.randint(-20,20)
            else:
                self.mx *= 0.95
                self.my -= 0.5
                self.surge += 1
            for i in range(len(blocks)):
                e = self.coll(blocks[i],self.mx,self.my,False)
                if e != False:
                    self.mx,self.my = e
            self.rekt.move(self.mx,self.my)
            self.x += self.mx;self.y += self.my
            c = len(bult)
            i=0
            while i < c and self.bar == None:
                if self.coll(bult[i].getReckt(),0,0,True):
                    bult[i].close()
                    self.close()
                    score += 1
                    if random.randint(0,00) == 0:
                        drop.append(gun(self.x,self.y))
                i += 1
                
    def getClosed(self):
        if self.bar == None:
            return True
        else:
            return False

    def coll(self,r2,xx,yy,bull):
        global score
        if self.bar == None:
            r2p1 = r2.getP1()
            r2p1x = r2p1.getX();r2p1y = r2p1.getY()
            if bull and quickcol(self.x,self.y,r2p1x,r2p1y):
                return False
            else:
                r2p2 = r2.getP2()
                r2p2x = r2p2.getX()
                r2p2y = r2p2.getY()
                if self.x+xx <= r2p2x and self.x+30+xx >= r2p1x and self.y+yy >= r2p1y and self.y-30+yy <= r2p2y:
                    if not bull:
                        if self.x >= r2p2x:
                            xx = self.x-r2p2x
                        if self.x+30 <= r2p1x:
                            xx = (self.x+30) - r2p1x
                        if self.y <= r2p1y:
                            yy = r2p1y-self.y
                        if self.y-30 >= r2p2y:
                            yy = (r2p2y)-(self.y-30)
                            self.falling = False
                            curx1 = r2p1x
                            curx2 = r2p2x
                        return xx,yy
                    else:
                        return True
                else:
                    return False
            return True
        return True
                
    def close(self):
        if self.bar != 'closed':
            self.rekt.undraw()
            self.bar = 'closed'

class gun:
    
    def __init__(self,x,y):
        global types, gd,bd,gv,bv,gbr,bbr,grr,brr,gc,bc,ga,ba,gr,br,gl,bl
        types = ['Minigun','Pistol','Assault Rifle','Sniper Rifle']
        gd = ['Shiny','Powerful']
        gv = ['Inflammed','Furious']
        gbr = ['Automatic','Fast','Greasy']
        grr = ['Intuitive','User-Friendly']
        gc = ['Overstuffed','Long-Lasting']
        ga = ['Suppressed','Accurate']
        gr = ['Stable']
        bd = ['Cracked']
        bv = ['Sluggish','Lethargic']
        bbr = ['Restrictive','Manual']
        brr = ['Corroded','Ackward']
        bc = ['Short','Low-Capacity']
        ba = ['Inaccurate',"Spray'n Pray"]
        br = ['Retroactive']
        gl = [gd,gv,gbr,grr,gc,ga,gr]
        bl = [bd,bv,bbr,brr,bc,ba,br]
        self.type = types[random.randint(0,len(types)-1)]
        self.bar = None
        if random.randint(0,1) == 1:
            a1 = gl[random.randint(0,len(gl)-1)]
        else:
            a1 = bl[random.randint(0,len(gl)-1)]
        if random.randint(0,1) == 1:
            if random.randint(0,1) == 1:
                a2 = gl[random.randint(0,len(gl)-1)]
            else:
                a2 = bl[random.randint(0,len(gl)-1)]
            if random.randint(0,1) == 1:
                if random.randint(0,1) == 1:
                    a3 = gl[random.randint(0,len(gl)-1)]
                else:
                    a3 = bl[random.randint(0,len(gl)-1)]
            else:
                a3 = 0
        else:
            a2 = 0
        if self.type == 'Minigun':
            self.d = 1
            self.v = 40
            self.rc = -50
            self.br = 2
            self.ac = 50
            self.c = 40
            self.rr = 80
        elif self.type == 'Pistol':
            self.d = 5
            self.v = 40
            self.rc = -20
            self.br = 10
            self.ac = 100
            self.c = 10
            self.rr = 20
        elif self.type == 'Assault Rifle':
            self.d = 2
            self.v = 50
            self.rc = -30
            self.br = 4
            self.ac = 80
            self.c = 25
            self.rr = 40
        elif self.type == 'Sniper Rifle':
            self.d = 20
            self.v = 100
            self.rc = -200
            self.br = 20
            self.ac = 200
            self.c = 5
            self.rr = 80
        a1 = self.getatts(a1)
        if a2 != 0:
            a2 = self.getatts(a2)
            if a3 != 0:
                a3 = self.getatts(a3)
                self.name = a1 + ' ' + a2 + ' ' + a3 + ' ' + self.type
            else:
                self.name = a1 + ' ' + a2 + ' ' + self.type
        else:
            self.name = a1 + ' ' + self.type
        self.rect = Rectangle(Point(x,y-30),Point(x+60,y+30))
        self.rect.draw(win)
        self.crate = Image(Point(x+30,y),('resources/' + str(win_height) + '/crate.gif'))
        self.crate.draw(win)
        #print(self.name,self.d,self.v,self.rc,self.br,self.ac,self.c,self.rr)
    def trans(self):
        global magmax,rltg,rltb,velo,acc,recoil,name
        if self.bar == None:
            name = self.name
            rltg = self.rr
            rltb = self.br
            velo = self.v
            acc = self.ac
            magmax = self.c
            recoil = self.rc
            self.bar = 'closed'
            self.rect.undraw()
            self.crate.undraw()
        
    def getrect(self):
        return self.rect

    def getClosed(self):
        return self.bar
    
    def getatts(self,a):
        if self.bar == None:
            if a == gd:
                self.d = int(1.5 * self.d)
                return gd[random.randint(0,len(gd)-1)]
            elif a == gv:
                self.v = int(1.5 * self.v)
                return gv[random.randint(0,len(gv)-1)]
            elif a == gbr:
                self.br = int(.5 * self.v)
                return gbr[random.randint(0,len(gbr)-1)]
            elif a == grr:
                self.rr = int(.5 * self.rr)
                return grr[random.randint(0,len(grr)-1)]
            elif a == gc:
                self.c = int(1.5 * self.c)
                return gc[random.randint(0,len(gc)-1)]
            elif a == ga:
                self.ac = int(1.5 * self.ac)
                return ga[random.randint(0,len(ga)-1)]
            elif a == gr:
                self.rc = int(.5 * self.rc)
                return gr[random.randint(0,len(gr)-1)]
            elif a == bd:
                self.d = int(.5 * self.d)
                return bd[random.randint(0,len(bd)-1)]
            elif a == bv:
                self.v = int(.5 * self.v)
                return bv[random.randint(0,len(bv)-1)]
            elif a == bbr:
                self.br = int(1.5 * self.v)
                return bbr[random.randint(0,len(bbr)-1)]
            elif a == brr:
                self.rr = int(1.5 * self.rr)
                return brr[random.randint(0,len(brr)-1)]
            elif a == bc:
                self.c = int(.5 * self.c)
                return bc[random.randint(0,len(bc)-1)]
            elif a == ba:
                self.ac = int(.5 * self.ac)
                return ba[random.randint(0,len(ba)-1)]
            elif a == br:
                self.rc = int(1.5 * self.rc)
                return br[random.randint(0,len(br)-1)]
            else:
                print('lolololol')
        

    
    
def main(ww,hh):
    global up, key, falling,curx1,curx2,but,tb,nxt,x,y,falling,score,win,drop
    global magmax,rltg,rltb,velo,acc,recoil,win_height,name
    win_height = hh
    win = GraphWin('hi',ww,hh)
    win.setCoords(0,0,1920,1080)
    win.bind("<KeyPress>",keydown)
    win.bind("<KeyRelease>",keyup)
    win.bind("<Button-1>",butdown)
    win.bind("<ButtonRelease-1>",butup)
    win.pack()
    win.focus_set()
    fps = Text(Point(1900,1040),'');fps.draw(win)
    ammo = Text(Point(1820,1020),'');ammo.draw(win);ammo.setSize(15);ammo.setFace('helvetica')
    score_text = Text(Point(100,1020),'');score_text.draw(win);score_text.setSize(20);score_text.setFace('helvetica')
    gunname_text = Text(Point(800,1020),'Starter Gun');gunname_text.draw(win);gunname_text.setSize(20);gunname_text.setFace('helvetica')
    player = Rectangle(Point(985,120),Point(1015,150));player.setWidth(0);player.setFill('Blue');player.draw(win)
    blocks = [Rectangle(Point(-10,-10),Point(20,1080)),Rectangle(Point(1910,-10),Point(1930,1090)),
              Rectangle(Point(-10,1060),Point(1940,1100)),Rectangle(Point(400,10),Point(450,60)),
              Rectangle(Point(1100,10),Point(1150,60)),Rectangle(Point(-10,-10),Point(1940,10)),
              Rectangle(Point(500,200),Point(700,220))]
    for i in range(len(blocks)):
        blocks[i].setFill('black')
        blocks[i].setWidth(0)
        blocks[i].draw(win)
    ti = time()
    right = False;moving = False;up = True;falling = True;vert = False;but = False;yay=False;reload = False
    g = 0.5;f = 0.95;a=2;ts=10;x = 0;y=0;mx=0;my=0;bult = [];tb = 0;nxt = 0;xx=0;yy=0
    mobtime = 0;mob = [];score = 0;drop = []
    #starter gun
    magmax = 10
    mag = magmax
    rltg = 20
    velo = 30
    rltb = 5
    acc = 100
    recoil = -70
    name = 'Starter gun'
    while True:
        win.update()
        px = player.getCenter().getX();py = player.getCenter().getY()
        #=====Start Code=====#
        #keys!
        if up == False:
            if key == 'a':
                right = False
                moving = True
            if key == 'd':
                right = True
                moving = True
            if key == ' ' or key == 'w':
                if not falling:
                    vert = True
                    falling = True
        else:
            moving = False
        mx =(win.winfo_pointerx()-win.winfo_rootx())*(1920/ww)
        my = win.winfo_screenheight()-((win.winfo_pointery()-win.winfo_rooty())*(1080/hh))
        #movement
        if moving and right:
            if x > ts:
                x = ts
            else:
                x += a
        elif moving and not right:
            if x < -1 * ts:
                x = -1 * ts
            else:
                x -= a
        if falling and vert:
            y = 15
        elif not vert and falling:
            y -= g
        if not moving:
            x *= f
        #barriers
        for j in range(len(blocks)):
            over = overlap(player,blocks[j],x,y)
            if over != False:
                x,y = over
        #move
        if py < 10:
            falling = False
        player.move(x,y)
        #shooting
        if tb >= nxt:
            reload = False
            if but and mag > 0:
                bult.append(bullet(px,py,mx,my,velo,rltb,acc,recoil))
                mag -= 1
                tb = 0
            elif mag == 0:
                tb = -1 * rltg
                reload = True
                mag = magmax
        tb += 1
        #move/destroy bullets
        yay = True
        for i in range(len(bult)):
            bult[i].mve()
            for j in range(len(blocks)):
                bult[i].col(blocks[j])
            if not(bult[i].isclosed()):
                yay = False
        if yay == True:
            bult = []
        ammo.setText(mag)
        score_text.setText(score)
        if mag < 5:
            ammo.setTextColor('red')
        elif mag < 10:
            ammo.setTextColor('orange')
        elif reload:
            ammo.setTextColor('blue')
        else:
            ammo.setTextColor('black')
        #off a platform?
        if vert and falling:
            vert = False
        if not falling and (px+30 < curx1 or px > curx2):
            falling = True
        #enemies
        if mobtime >= 50:
            mobtime = 0
            mob.append(slime(win,500,500))
        else:
            mobtime += 1
        mobclosed = True
        for i in range(len(mob)):
            mob[i].mvee(px,py,blocks,bult)
            if mob[i].getClosed():
                mobclosed = False
        if mobclosed:
            mob = []
        #drops
        for i in range(len(drop)):
            if drop[i].getClosed() == None and overlap(player,drop[i].getrect(),x,y):
                drop[i].trans()
                mag = magmax
                gunname_text.setText(name)
        #======End Code======#
        if time() - ti < 0.016:
            try:
                sleep(0.016-(time()-ti))
            except:
                print('lol')
        fps.setText(str(round(1/(time()-ti),3)))
        ti = time()
ww,hh=setup.setup()
main(ww,hh)


