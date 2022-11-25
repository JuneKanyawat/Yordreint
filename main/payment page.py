from tkinter import *
root = Tk()
root.title("Yordreint")
root.geometry("1280x800") # window size

# Add image file
bg = PhotoImage(file = "/Users/Onlyjune/Desktop/Yor/image/bg image.png")

# Show image using label
label1 = Label(root, image = bg)
label1.place(x = 0, y = 0)

# Create frame
frame1 = Frame(root, background="white", highlightthickness=1,width=1000, height=600, bd= 0)
frame1.place(relx=0.5,rely=0.5, anchor=CENTER)

# Payment Text
label1 = Label(root, text="Payment",font=("Courier New", 60, "bold"),background="white")
label1.place(relx=0.5,rely=0.2, anchor=CENTER)

# Cycle options
label1 = Label(root, text="Cycle\noptions",font=("Courier New", 25),background="white",justify=LEFT)
label1.place(relx=0.18,rely=0.34, anchor=CENTER)

# Pink box
frame1 = Frame(root, background="pink", highlightthickness=1,width=200, height=55, bd= 0)
frame1.place(relx=0.35,rely=0.33, anchor=CENTER)

# Total price 
label1 = Label(root, text="Total\nprice",font=("Courier New", 25),background="white",justify=LEFT)
label1.place(relx=0.174,rely=0.5, anchor=CENTER)

# Pink box
frame1 = Frame(root, background="pink", highlightthickness=1,width=200, height=55, bd= 0)
frame1.place(relx=0.35,rely=0.50, anchor=CENTER)

label1 = Label(root, text="DELICATES",font=("Arial", 25),background="pink",justify=LEFT)
label1.place(relx=0.345,rely=0.33, anchor=CENTER)

root.mainloop()