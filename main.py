from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox


class app:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1280x800")
        #self.master['bg']='green'
        self.bg = PhotoImage(file = "/Users/Onlyjune/Desktop/Yor/image/bg image.png")
        self.label1 = Label(self.master, image = self.bg)
        self.label1.place(x = 0, y = 0)
        self.first_page()

    def click(self,event):
        self.second_page()

    def choose_power(self):
        self.confirm = messagebox.askquestion("Power wash mode", "Are you sure?")
        if self.confirm == 'yes':
            print("Power wash")
            self.third_page("Power wash")

    def choose_quick(self):
        self.confirm = messagebox.askquestion("Quick wash mode", "Are you sure?")
        if self.confirm == 'yes':
            print("Quick wash")
            self.third_page("Quick wash")  
    
    def choose_deli(self):
        self.confirm = messagebox.askquestion("Delicates wash mode", "Are you sure?")
        if self.confirm == 'yes':
            print("Delicates")
            self.third_page("Delicates") 
    
    def first_page(self):
        self.frame1 = Frame(self.master, background="white", highlightthickness=1,width=1000, height=600, bd= 0)
        self.frame1.place(relx=0.5,rely=0.5, anchor=CENTER)
        self.label1  = Label(self.frame1, text="Yordreint", font=("Courier New", 140, "bold"),background="white")
        self.label1.place(relx=0.5, rely=0.27, anchor=CENTER)
        self.pic = Image.open("/Users/Onlyjune/Desktop/Yor/image/washing-machine.png")
        self.resize = self.pic.resize((300,300), Image.ANTIALIAS)
        self.new_pic = ImageTk.PhotoImage(self.resize)
        self.label2 = Label(self.frame1, image=self.new_pic, background="white")
        self.label2.place(relx=0.5,rely=0.6, anchor=CENTER)
        self.label2.bind("<Button-1>", self.click)
        self.frame1.bind("<Button-1>", self.click)
    
    def second_page(self):
        self.frame2 = Frame(self.master, background="white", highlightthickness=1,width=1000, height=600, bd= 0)
        self.frame2.place(relx=0.5,rely=0.5, anchor=CENTER)
        self.label1 = Label(self.frame2, text="Choose mode",font=("Courier New", 90, "bold"),background="white")
        self.label1.place(relx=0.5,rely=0.25, anchor=CENTER)
        self.button1=Button(self.frame2, text = "Power wash", font=("Courier New", 14),height = 15, width = 20, command=self.choose_power)
        self.button1.place(relx=0.25,rely=0.57, anchor=CENTER)
        self.button2=Button(self.frame2, text = "Quick wash", font=("Courier New", 14), height = 15, width = 20, command=self.choose_quick)
        self.button2.place(relx=0.5,rely=0.57, anchor=CENTER)
        self.button3=Button(self.frame2, text = "Delicates wash", font=("Courier New", 14), height = 15, width = 20, command=self.choose_deli)
        self.button3.place(relx=0.75,rely=0.57, anchor=CENTER)

    def third_page(self,mode_c):
        self.frame3 = Frame(self.master, background="white", highlightthickness=1,width=1000, height=600, bd= 0)
        self.frame3.place(relx=0.5,rely=0.5, anchor=CENTER)
        self.label1 = Label(self.frame3, text="Payment",font=("Courier New", 60, "bold"),background="white")
        self.label1.place(relx=0.5,rely=0.15, anchor=CENTER)
        self.label1 = Label(self.frame3, text="Cycle\noptions",font=("Courier New", 25),background="white",justify=LEFT)
        self.label1.place(relx=0.18,rely=0.34, anchor=CENTER)
        self.frame1 = Frame(self.frame3, background="#D9D9D9", highlightthickness=1,width=200, height=55, bd= 0)
        self.frame1.place(relx=0.35,rely=0.33, anchor=CENTER)
        self.label1 = Label(self.frame3, text="Total\nprice",font=("Courier New", 25),background="white",justify=LEFT)
        self.label1.place(relx=0.174,rely=0.5, anchor=CENTER)
        self.frame1 = Frame(self.frame3, background="#D9D9D9", highlightthickness=1,width=200, height=55, bd= 0)
        self.frame1.place(relx=0.35,rely=0.50, anchor=CENTER)    
        self.label1 = Label(self.frame3, text=mode_c,font=("Courier New", 25),background="#D9D9D9",justify=LEFT)
        self.label1.place(relx=0.345,rely=0.33, anchor=CENTER)
        self.price = 20
        if mode_c == "Power wash":
            self.price = 30
        self.label1 = Label(self.frame3, text=self.price,font=("Courier New", 25),background="#D9D9D9",justify=LEFT)
        self.label1.place(relx=0.345,rely=0.5, anchor=CENTER)

        self.my_pic = Image.open("/Users/Onlyjune/Desktop/Yor/image/"+mode_c+".png")
        self.resize = self.my_pic.resize((300,300),Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.resize)
        self.label1 = Label(self.frame3, image=self.img, width=300, height=300)
        self.label1.place(relx=0.78,rely=0.6, anchor=CENTER)


root = Tk()
app(root)
root.mainloop()