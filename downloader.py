import instaloader
from tkinter import *

ig = instaloader.Instaloader()
  
root = Tk()
root.geometry("300x80")
root.title("Instagram Profile Photo Downloader")
  
def Take_input():
    INPUT = inputtxt.get("1.0", "end-1c")
    print(INPUT)
    ig.download_profile(INPUT,profile_pic_only=True)
      
l = Label(text = "Enter Insta Username")
inputtxt = Text(root, height = 1,
                width = 30,
                bg = "light yellow",
                font=("Verdana",14))
  
Display = Button(root, height = 2,
                 width = 20, 
                 text ="Download",
                 command = lambda:Take_input())
  
l.pack()
inputtxt.pack()
Display.pack()
root.mainloop()