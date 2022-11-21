from tkinter import *
root = Tk()
root.title("Yordreint")
root.geometry("1280x800")
root['background']='#D9F6FF'

frame1 = Frame(root, background="white", highlightthickness=1,width=1000, height=600, bd= 0)
frame1.place(relx=0.5,rely=0.5, anchor=CENTER)

label1 = Label(root, text="Choose mode",font=('Arial', 36))
label1.place(relx=0.5,rely=0.2, anchor=CENTER)

button1=Button(root, text = "Power wash", height = 10, width = 15)
button1.place(relx=0.28,rely=0.54, anchor=CENTER)

button2=Button(root, text = "Quick wash", height = 10, width = 15)
button2.place(relx=0.5,rely=0.54, anchor=CENTER)

button3=Button(root, text = "DELICATES", height = 10, width = 15)
button3.place(relx=0.72,rely=0.54, anchor=CENTER)

root.mainloop()