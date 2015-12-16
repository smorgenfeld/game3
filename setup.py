from tkinter import *

def setup():
    gin = Tk()
    gin.geometry('200x200')
    gin.title('')
    lst1 = ['960x540','Fullscreen (Native)','1920x1080','1600x900','1280x720']
    var1 = StringVar(gin)
    var1.set(lst1[0])
    drop = OptionMenu(gin,var1,*lst1)
    drop.config(width=20)
    drop.grid()
    drop.pack(padx=15,pady=15)
    def cont():
        global ww,hh,full
        if var1.get() != 'Fullscreen (Native)':
            ww = int((var1.get())[:((var1.get()).find('x'))])
            hh = int((var1.get())[((var1.get()).find('x'))+1:])
            full = False
        else:
            ww = gin.winfo_screenwidth()
            hh = gin.winfo_screenheight()
            full = True
        gin.destroy()
    b = Button(gin, text='Continue',command=cont)
    b.pack(pady=15)
    gin.wait_window()
    return ww,hh,full
