from tkinter import *
import time
from tkinter import ttk
from time import sleep
from PIL import ImageTk, Image
from tkinter import messagebox


class app:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1280x800")
        #self.master['bg']='green'
        self.fourth_page()
    
    def click_5(self):
        self.fifth_page()

    def click_1(self):
        print("click")

    def play_animation(self):
        for i in range(2):
            k=300
            for j in range(4):
                Label(self.frame5, bg="#79E8FF",width=5,height=3).place(x=(k+100), y=400)
                sleep(0.3)
                self.frame5.update_idletasks()
                sleep(0.3) 
                k+=100
            Label(self.frame5, bg="white",width=60,height=3).place(x=500, y=400)
            self.frame5.update_idletasks()

        else:
            self.sixth_page()

    def fourth_page(self):
        self.frame4 = Frame(self.master, background="white", highlightthickness=1,width=1000, height=600, bd= 0)
        self.frame4.place(relx=0.5,rely=0.5, anchor=CENTER)
        self.label1 = Label(self.frame4, text="Have you put your clothes?", font=("Courier New", 50, "bold"),background="white")
        self.label1.place(relx=0.5, rely=0.2, anchor=CENTER)
        self.button1=Button(self.frame4, text = "Done", font=("Courier New", 20),height = 3, width = 10, command=self.click_5)
        self.button1.place(relx=0.8,rely=0.8, anchor=CENTER)

            
    def fifth_page(self):
        self.frame5 = Frame(self.master, background="white", highlightthickness=1,width=1000, height=600, bd= 0)
        self.frame5.place(relx=0.5,rely=0.5, anchor=CENTER)
        self.label1 = Label(self.frame5, text="Loading", font=("Courier New", 140, "bold"),background="white")
        self.label1.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.play_animation()

    def countdown(self,t):
    
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            Label(self.frame6, text=timer, bg="white", font=("Courier New", 310)).place(relx=0.5,rely=0.5, anchor=CENTER)
            self.frame6.update()
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
        
        self.seventh_page()


    def sixth_page(self):
        self.frame6 = Frame(self.master, background="white", highlightthickness=1,width=1000, height=600, bd= 0)
        self.frame6.place(relx=0.5,rely=0.5, anchor=CENTER)
        self.countdown(10)

    def seventh_page(self):
        self.frame7 = Frame(self.master, background="white", highlightthickness=1,width=1000, height=600, bd= 0)
        self.frame7.place(relx=0.5,rely=0.5, anchor=CENTER)
        self.label1 = Label(self.frame7, text="Finished!", font=("Courier New", 140, "bold"),background="white")
        self.label1.place(relx=0.5, rely=0.27, anchor=CENTER)
        self.pic = Image.open("/Users/Onlyjune/Desktop/Yor/image/laundry.png")
        self.resize = self.pic.resize((300,300), Image.ANTIALIAS)
        self.new_pic = ImageTk.PhotoImage(self.resize)
        self.label2 = Label(self.frame7, image=self.new_pic, background="white")
        self.label2.place(relx=0.5,rely=0.6, anchor=CENTER)
        self.label2.bind("<Button-1>", self.click)
        self.frame7.bind("<Button-1>", self.click)
        
        
        

root = Tk()
app(root)
root.mainloop()