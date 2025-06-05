from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Developer:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_label=Label(self.root,text="DEVELOPER ",font=("times new roman",35,"bold"),bg="gray",fg="black")
        title_label.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"images\hero.jpg")
        img_top=img_top.resize((1530,850),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        first_label=Label(self.root,image=self.photoimg_top)
        first_label.place(x=0,y=55,width=1530,height=850)

        main_frame=Frame(first_label,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=500,height=687)

        img_diya=Image.open(r"images\dia.jpg")
        img_diya=img_diya.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg_diya=ImageTk.PhotoImage(img_diya)

        diya_label=Label(main_frame,image=self.photoimg_diya)
        diya_label.place(x=340,y=0,width=200,height=200)

        #developer
        dev_label=Label(main_frame,text="Hey! I Diya Rawat ",font=("times new roman",18,"bold"),bg="white")
        dev_label.place(x=0,y=5)

        #developer
        dev_label=Label(main_frame,text="I am an AI and ML Developer. ",font=("times new roman",18,"bold"),bg="white")
        dev_label.place(x=0,y=40)

        #third image
        img2=Image.open(r"images\stu.jpg")
        img2=img2.resize((500,480),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        
        first_label=Label(main_frame,image=self.photoimg2)
        first_label.place(x=0,y=210,width=500,height=480)



if __name__ == "__main__":    
    root=Tk()
    obj=Developer(root) 
    root.mainloop()  
