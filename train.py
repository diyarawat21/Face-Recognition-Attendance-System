from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np



class Train:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        title_label=Label(self.root,text="TRAIN DATA SET ",font=("times new roman",35,"bold"),bg="white",fg="brown")
        title_label.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"images\top1.jpg")
        img_top=img_top.resize((1530,365),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        first_label=Label(self.root,image=self.photoimg_top)
        first_label.place(x=0,y=55,width=1530,height=365)

        #button
        b1_1= Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="green",fg="white")
        b1_1.place(x=0,y=420,width=1530,height=60)


        img_bottom=Image.open(r"images\bottom.jpg")
        img_bottom=img_bottom.resize((1530,365),Image.Resampling.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        first_label=Label(self.root,image=self.photoimg_bottom)
        first_label.place(x=0,y=480,width=1530,height=365)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file)for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #Gray scale image
            imageNp=np.array(img,'uint8') # uint8 is a datatype
            id=int(os.path.split(image)[1].split('.')[1])


            faces.append(imageNp)
            ids.append(id)
              
            cv2.imshow("Training",imageNp)
            cv2.waitKey(100)
        
        ids=np.array(ids)

        #===========train thr classifier and save============
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()

        messagebox.showinfo("Result","Training datasets completed!!") 








if __name__ == "__main__":    
    root=Tk()
    obj=Train(root) 
    root.mainloop()