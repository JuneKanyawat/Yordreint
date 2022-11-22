from tkinter import *
from time import sleep

root = Tk()
root.title("Yordreint")
root.geometry("1280x800")

# Add image file
bg = PhotoImage(file = "/Users/Onlyjune/Desktop/Yor/image/bg image.png")

# Show image using label
label1 = Label(root, image = bg)
label1.place(x = 0, y = 0)

# Create Frame
frame1 = Frame(root, background="white", highlightthickness=1,width=1000, height=600, bd= 0)
frame1.place(relx=0.5,rely=0.5, anchor=CENTER)

for j in range(5):
    Label(root, bg="#D9F6FF",width=4,height=3,highlightbackground="blue", highlightthickness=2).place(x=(j + 29) * 29, y=500)

def play_animation():
        for i in range(4):
            for j in range(5):
                Label(root, bg="#79E8FF",width=4,height=3,highlightbackground="blue", highlightthickness=2).place(x=(j + 29) * 29, y=500)
                sleep(0.2)
                root.update_idletasks()

                Label(root, bg="#D9F6FF",width=4,height=3,highlightbackground="blue", highlightthickness=2).place(x=(j + 29) *29, y=500)
 
        else:
            root.destroy()

play_animation()
root.mainloop()