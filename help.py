from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Help:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_label=Label(self.root,text="HELP DESK ",font=("times new roman",35,"bold"),bg="gray",fg="black")
        title_label.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"images\bck.png")
        img_top=img_top.resize((1530,850),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        first_label=Label(self.root,image=self.photoimg_top)
        first_label.place(x=0,y=55,width=1530,height=850)

        #developer
        dev_label=Label(first_label,text=" Email: diyarawat2102@gmail.com ",font=("times new roman",18,"bold"),bg="grey")
        dev_label.place(x=580,y=500)


if __name__ == "__main__":    
    root=Tk()
    obj=Help(root) 
    root.mainloop()