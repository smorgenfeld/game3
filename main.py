#game3.py

from graphics import *
from time import *
import tkinter, random, math, setup
import math
import random

def overlap(r1,r2,x,y,cr8,slime,sh):
    global falling,curx1,curx2,phealth
    r1cent = r1.getCenter()
    r1x = r1cent.getX()-15 + x
    r1y = r1cent.getY()+15 + y
    r2p1 = r2.getP1();r2p2 = r2.getP2()
    r2p1x = r2p1.getX()
    r2p2x = r2p2.getX()
    r2p1y = r2p1.getY()
    r2p2y = r2p2.getY()
    if r1x <= r2p2x and r1x+30 >= r2p1x and r1y >= r2p1y and r1y-30 <= r2p2y:
        if cr8:
            return True
        elif slime:
            phealth -= sh//15
            updatehealth(phealth)
        else:
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

def updatehealth(ph):
    global phbar
    phbar.undraw()
    del phbar
    phbar = Rectangle(Point(960-ph*3,990),Point(960+ph*3,1020))
    phbar.setWidth(0);phbar.setFill('green');phbar.draw(win)

def gameover():
    over = Text(Point(960,540),'Game Over');over.setFill('red');over.setFace('helvetica');over.setSize(35);over.draw(win)
    click = Text(Point(960,450),'Click Anywhere to Continue:');click.setFace('helvetica');click.setSize(20);click.draw(win)
    win.getMouse()
    quit()

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
        self.bul = Image(Point(self.x-10,self.y-10),('resources/' + str(win_height) + '/bul.gif'))
        self.bul.draw(win)
        top = (y2 - y1)
        bottom = (x2 - x1)
        try:
            m = top/bottom*ac
        except:
            m = top/(bottom*ac+0.001)
        self.mx = math.cos(math.atan(m))*v
        self.my = math.tan(math.atan(m)) * self.mx
        if bottom < 0:
            self.my *= -1
            self.mx *= -1
        x += self.mx/reco
        if falling:
            y += self.my/reco
        else:
            y = 0
        self.h = bhealth
            
    def mve(self):
        if self.bar == None:
            self.reckt.move(self.mx,self.my)
            self.bul.move(self.mx,self.my)
            self.x += self.mx;self.y += self.my

    def getReckt(self):
        return self.reckt

    def getHealth(self):
        return self.h

    def changeHealth(self,h):
        self.h -= h
            
    def close(self):
        if self.bar == None:
            self.reckt.undraw()
            self.bul.undraw()
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

    def __init__(self,win,initx,inity,health,t):
        if t == 'blue':
            self.health = health * 2
            self.wh = health//4 + 20
        else:
            self.health = health
            self.wh = health//2+20
        self.rekt = Rectangle(Point(initx,inity),Point(initx+self.wh,inity-self.wh))
        self.rekt.setWidth(0);self.rekt.setFill(t);self.rekt.draw(win)
        self.falling = True
        self.cur = ''
        self.x = initx;self.y = inity
        self.mx = 0;self.my=0
        self.surge = 0
        self.bar = None
        self.type = t

    def getHealth(self):
        if self.bar == None:
            return self.health
        else:
            return 0
    def getrect(self):
        return self.rekt

    def mvee(self,px,py,blocks,bult):
        global score
        if self.bar == None:
            if self.type == 'green':
                ms = 15
            elif self.type == 'red':
                ms = 25
            elif self.type == 'blue':
                ms = 7
            if not falling and self.surge >= 50:
                if py+10 > self.y:
                    if px > self.x:
                        self.mx = ms - 5
                    else:
                        self.mx = -ms + 5
                    self.my = random.randint(10,ms + 5)
                    self.falling = True
                else:
                    if px > self.x:
                        self.mx = ms
                    else:
                        self.mx = -ms
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
                    if self.health > bult[i].getHealth():
                        self.health -= bult[i].getHealth()
                        self.rekt.undraw()
                        if self.type == 'blue':
                            self.wh = self.health//4 + 20
                        else:
                            self.wh = self.health//2 + 20
                        del self.rekt
                        self.rekt = Rectangle(Point(self.x,self.y),Point(self.x+self.wh,self.y-self.wh))
                        self.rekt.setFill(self.type);self.rekt.setWidth(0);self.rekt.draw(win)
                        bult[i].close()
                    else:
                        bult[i].changeHealth(self.health)
                        self.close()
                        score += 1
                        if random.randint(0,5) == 5:
                            drop.append(gun(self.x,self.y))
                i += 1
                if self.y < -20:
                    self.close()
                
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
                if self.x+xx <= r2p2x and self.x+self.wh+xx >= r2p1x and self.y+yy >= r2p1y and self.y-self.wh+yy <= r2p2y:
                    if not bull:
                        if self.x >= r2p2x:
                            xx = self.x-r2p2x
                        if self.x+self.wh <= r2p1x:
                            xx = (self.x+self.wh) - r2p1x
                        if self.y <= r2p1y:
                            yy = r2p1y-self.y
                        if self.y-self.wh >= r2p2y:
                            yy = (r2p2y)-(self.y-self.wh)
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
        global types, gd,bd,gv,bv,gbr,bbr,grr,brr,gc,bc,ga,ba,gr,br,gl,bl,gm
        types = ['Minigun','Pistol','Assault Rifle','Sniper Rifle','Shotgun']
        gd = ['Shiny','Powerful','Destructive','Legendary']
        gv = ['Inflammed','Furious','Speedy']
        gbr = ['Automatic','Fast','Greasy']
        grr = ['Intuitive','User-Friendly']
        gc = ['Overstuffed','Long-Lasting','High-Capacity']
        ga = ['Suppressed','Accurate','Pin-Point','Scoped','Laser-Scoped']
        gr = ['Stable','Springy']
        gm = ['Double Barreled','Dual Barreled']
        bd = ['Cracked','Weak']
        bv = ['Sluggish','Lethargic','Soporific']
        bbr = ['Restrictive','Manual']
        brr = ['Corroded','Ackward']
        bc = ['Short','Low-Capacity']
        ba = ['Inaccurate',"Spray'n Pray",'Sawed-Off']
        br = ['Retroactive','Rocket-Like']
        gl = [gd,gv,gbr,grr,gc,ga,gr,gm]
        bl = [bd,bv,bbr,brr,bc,ba,br]
        self.type = types[random.randint(0,len(types)-1)]
        self.bar = None
        self.lz = False
        if random.randint(0,1) == 1:
            a1 = gl[random.randint(0,len(gl)-1)]
        else:
            a1 = bl[random.randint(0,len(bl)-1)]
        if random.randint(0,1) == 1:
            if random.randint(0,1) == 1:
                a2 = gl[random.randint(0,len(gl)-1)]
            else:
                a2 = bl[random.randint(0,len(bl)-1)]
            if random.randint(0,1) == 1:
                if random.randint(0,1) == 1:
                    a3 = gl[random.randint(0,len(gl)-1)]
                else:
                    a3 = bl[random.randint(0,len(bl)-1)]
            else:
                a3 = 0
        else:
            a2 = 0
        if self.type == 'Minigun':
            self.v = 40
            self.rc = -50
            self.br = 2
            self.ac = 100
            self.c = 40
            self.rr = 80
            self.h = 5
            self.m = 1
        elif self.type == 'Pistol':
            self.v = 40
            self.rc = -50
            self.br = 10
            self.ac = 20
            self.c = 10
            self.rr = 20
            self.h = 40
            self.m = 1
        elif self.type == 'Assault Rifle':
            self.v = 50
            self.rc = -50
            self.br = 4
            self.ac = 80
            self.c = 25
            self.rr = 40
            self.h = 10
            self.m = 1
        elif self.type == 'Sniper Rifle':
            self.v = 60
            self.rc = -200
            self.br = 20
            self.ac = 5
            self.c = 5
            self.rr = 60
            self.h = 300
            self.m = 1
        elif self.type == 'Shotgun':
            self.v = 40
            self.rc = -200
            self.br = 20
            self.ac = 90
            self.c = 20
            self.rr = 50
            self.h = 50
            self.m = 5
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
        self.crate = Image(Point(x+30,y),('resources/' + str(win_height) + '/crate.gif'))
        self.crate.draw(win)
        
    def trans(self):
        global magmax,rltg,rltb,velo,acc,recoil,name,bhealth,mult,lazer
        if self.bar == None:
            name = self.name
            rltg = self.rr
            rltb = self.br
            velo = self.v
            acc = self.ac
            bhealth = self.h
            magmax = self.c
            recoil = self.rc
            mult = self.m
            lazer = self.lz
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
                self.h = int(1.5 * self.h)
                return gd[random.randint(0,len(gd)-1)]
            elif a == gv:
                self.v = int(1.5 * self.v)
                return gv[random.randint(0,len(gv)-1)]
            elif a == gbr:
                self.br = int(.75 * self.br)
                return gbr[random.randint(0,len(gbr)-1)]
            elif a == grr:
                self.rr = int(.75 * self.rr)
                return grr[random.randint(0,len(grr)-1)]
            elif a == gc:
                self.c = int(1.5 * self.c)
                return gc[random.randint(0,len(gc)-1)]
            elif a == ga:
                kk = ga[random.randint(0,len(ga)-1)]
                if kk == 'Laser-Scoped':
                    self.lz = True
                    self.ac = int(.25 * self.ac)
                else:
                    self.ac = int(.75 * self.ac)
                return kk
            elif a == gr:
                self.rc = int(.75 * self.rc)
                return gr[random.randint(0,len(gr)-1)]
            elif a == gm:
                self.m = int(2 * self.m)
                return gm[random.randint(0,len(gm)-1)]
            elif a == bd:
                self.h = int(.75 * self.h)
                return bd[random.randint(0,len(bd)-1)]
            elif a == bv:
                self.v = int(.75 * self.v)
                return bv[random.randint(0,len(bv)-1)]
            elif a == bbr:
                self.br = int(1.5 * self.br)
                return bbr[random.randint(0,len(bbr)-1)]
            elif a == brr:
                self.rr = int(1.5 * self.rr)
                return brr[random.randint(0,len(brr)-1)]
            elif a == bc:
                self.c = int(.75 * self.c)
                return bc[random.randint(0,len(bc)-1)]
            elif a == ba:
                self.ac = int(1.5 * self.ac)
                return ba[random.randint(0,len(ba)-1)]
            elif a == br:
                self.rc = int(1.5 * self.rc)
                return br[random.randint(0,len(br)-1)]
            else:
                print('lolololol')
        

    
    
def main(ww,hh):
    global up, key, falling,curx1,curx2,but,tb,nxt,x,y,falling,score,win,drop
    global magmax,rltg,rltb,velo,acc,recoil,win_height,name,bhealth,mult
    global lazer,phealth,phbar
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
    gunname_text = Text(Point(800,970),'Starter Gun');gunname_text.draw(win);gunname_text.setSize(20);gunname_text.setFace('helvetica')
    round_text = Text(Point(100,980),'Round 1');round_text.setSize(15);round_text.setFace('helvetica');round_text.draw(win)
    bigrnd_text = Text(Point(960,540),'');bigrnd_text.setSize(35);bigrnd_text.setFace('helvetica');bigrnd_text.draw(win)
    player = Rectangle(Point(985,120),Point(1015,150));player.setWidth(0);player.setFill('Blue');player.draw(win)
    blocks = [Rectangle(Point(-10,-10),Point(20,1080)),Rectangle(Point(1910,-10),Point(1930,1090)),
              Rectangle(Point(-10,1060),Point(1940,1100)),Rectangle(Point(-10,-10),Point(1940,10)),
              Rectangle(Point(70,190),Point(570,230)),Rectangle(Point(1350,190),Point(1850,230))
              ,Rectangle(Point(660,10),Point(1260,20)),Rectangle(Point(670,400),Point(1250,440))
              ,Rectangle(Point(150,600),Point(650,640)),Rectangle(Point(1280,600),Point(1770,640))
              ,Rectangle(Point(10,10),Point(110,110)),Rectangle(Point(1810,10),Point(1910,110))
              ,Rectangle(Point(10,400),Point(210,440)),Rectangle(Point(1710,400),Point(1910,440)),
              Rectangle(Point(880,840),Point(1040,880))]
    phbarr = Rectangle(Point(660,990),Point(1260,1020));phbarr.setFill('red');phbarr.setWidth(0);phbarr.draw(win)
    phbar = Rectangle(Point(660,990),Point(1260,1020));phbar.setFill('green');phbar.setWidth(0);phbar.draw(win)
    for i in range(len(blocks)):
        blocks[i].setFill('black')
        blocks[i].setWidth(0)
        blocks[i].draw(win)
    ti = time()
    right = False;moving = False;up = True;falling = True;vert = False;but = False;yay=False;reload = False
    g = 0.5;f = 0.95;a=2;ts=10;x = 0;y=0;mx=0;my=0;bult = [];tb = 0;nxt = 0;xx=0;yy=0
    mobtime = 10;mob = [];score = 0;drop = []
    rnd = 1;spawning = True;toth = 0;bigrndcont = 0;bigrnd = False;phealth = 100
    #starter gun
    magmax = 10
    mag = magmax
    rltg = 20
    velo = 5
    rltb = 5
    acc = 100
    recoil = -70
    bhealth = 10
    mult = 1
    name = 'Starter gun'
    lazer = True
    while True:
        win.update()
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
            y = 17
        elif not vert and falling:
            y -= g
        if not moving:
            x *= f
        #barriers
        for j in range(len(blocks)):
            over = overlap(player,blocks[j],x,y,False,False,0)
            if over != False:
                x,y = over
        #move
        player.move(x,y)
        px = player.getCenter().getX();py = player.getCenter().getY()
        #shooting
        if tb >= nxt:
            reload = False
            if but and mag > 0:
                for i in range(mult):
                    if mag > 0:
                        bult.append(bullet(px,py,mx,my,velo,rltb,acc,recoil))
                        mag -= 1
                tb = 0
            elif mag == 0:
                tb = -1 * rltg
                reload = True
                mag = magmax
        tb += 1
        #lazer
        if lazer:
            try:
                Lll.undraw()
                del Lll
            except:
                l=0
            Lll = Line(Point(px,py),Point((mx-px)*20,(my-py)*20))
            Lll.setFill('red');Lll.draw(win)
            
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
        if mag < magmax//5:
            ammo.setTextColor('red')
        elif mag < magmax//2:
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
        if spawning and mobtime >= 10:
            mobtime = 0
            if score < 10:
                hhh = 10
            else:
                hhh = random.randint(10,score*3)
            if random.randint(0,5) == 5:
                ttt = 'red'
            elif random.randint(0,5) == 5:
                ttt = 'blue'
            else:
                ttt = 'green'
            toth += hhh
            mob.append(slime(win,960,1000,hhh,ttt))
        else:
            mobtime += 1
        mobclosed = True
        for i in range(len(mob)):
            mob[i].mvee(px,py,blocks,bult)
            if mob[i].getClosed():
                mobclosed = False
            overlap(player,mob[i].getrect(),0,0,False,True,mob[i].getHealth())
        if mobclosed:
            mob = []
        #drops
        for i in range(len(drop)):
            if drop[i].getClosed() == None and overlap(player,drop[i].getrect(),x,y,True,False,0):
                drop[i].trans()
                try:
                    Lll.undraw()
                    del Lll
                except:
                    l=0
                mag = magmax
                gunname_text.setText(name)
        #rounds!
        if spawning and toth > rnd * 100:
            toth = 0
            spawning = False
        rndcont = False
        for ii in range(len(mob)):
            if not spawning and mob[ii].getClosed():
                rndcont = True
        if rndcont == False and not spawning:
            mob = []
            rnd += 1
            round_text.setText('Round '+str(rnd))
            spawning = True
            bigrnd = True
            bigrndcont = 0
        if bigrnd:
            if bigrndcont == 0:
                bigrnd_text.setText('Round '+str(rnd))
            bigrndcont += 1
            if bigrndcont > 200:
                bigrnd_text.setText('')
                bigrnd = False
                bigrndcont = 0
        #gameover
        if phealth <= 0:
            gameover()
        #fudging it
        if py < 10:
            player.move(0,10)
            falling = False
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


