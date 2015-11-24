from tkinter import *

def setup():
    gin = Tk()
    gin.geometry('200x200')
    lst1 = ['960x540','1920x1080','1600x900','1280x720']
    var1 = StringVar(gin)
    var1.set(lst1[0])
    drop = OptionMenu(gin,var1,*lst1)
    drop.config(width=20)
    drop.grid()
    drop.pack(padx=15,pady=15)
    def cont():
        global ww,hh
        ww = int((var1.get())[:((var1.get()).find('x'))])
        hh = int((var1.get())[((var1.get()).find('x'))+1:])
        gin.destroy()
    b = Button(gin, text='Continue',command=cont)
    b.pack(pady=15)
    gin.mainloop()
    print('yay')
    return ww,hh
