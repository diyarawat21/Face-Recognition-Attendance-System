from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from time import strftime
from datetime import datetime
import mysql.connector
import cv2
import os
import numpy as np
import time




class Face_Recognition:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        title_label=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_label.place(x=0,y=0,width=1530,height=45)

        #1st image
        img_top=Image.open(r"images\all1.jpg")
        img_top=img_top.resize((650,800),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        first_label=Label(self.root,image=self.photoimg_top)
        first_label.place(x=0,y=55,width=650,height=800)


        #2nd image
        img_bottom=Image.open(r"images\all2.jpg")
        img_bottom=img_bottom.resize((950,800),Image.Resampling.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        second_label=Label(self.root,image=self.photoimg_bottom)
        second_label.place(x=650,y=55,width=950 ,height=800)

        # button====

        b1_1= Button(second_label,text="FACE RECOGNITION",command=self.face_recog,cursor="hand2",font=("times new roman",18,"bold"),bg="sky blue",fg="black")
        b1_1.place(x=350,y=690,width=300,height=40)

     #-----------attendance----------
    def mark_attendance(self,i,r,n,d):
        entry_key = f"{i},{r},{n},{d}"
        file_path = "face_attendance.csv"

        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
              f.write("ID,Roll,Name,Department,Time,Date,Status\n")

        
        with open("face_attendance.csv","r+",newline="\n") as f: #r+=read+
            myDataList = f.readlines()
            data_list = [line.strip().split(",")[0:4] for line in myDataList]
            data_list = [",".join(item) for item in data_list]

            
        if entry_key not in data_list:
            now = datetime.now()
            d1 = now.strftime("%d/%m/%Y")
            dtString = now.strftime("%H:%M:%S")
            f.writelines(f"\n{entry_key},{dtString},{d1},Present")

            with open(file_path, "a", newline="\n") as f:  # 'a' for append mode
              f.write(f"{entry_key},{dtString},{d1},Present\n")

            



        #============face recognition==========

    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                   
            
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
                my_cursor=conn.cursor() 

                my_cursor.execute("Select name from Student where Student_ID="+str(id))
                #lets take variable = n
                n=my_cursor.fetchone()
                n="+".join(n) if n else "Unknown"

                my_cursor.execute("Select Roll from Student where Student_ID="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r) if r else "Unknown"


                my_cursor.execute("Select Dep from Student where Student_ID="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)if d else "Unknown"

                my_cursor.execute("Select Student_ID from Student where Student_ID="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)if i else "Unknown"


                if confidence > 77:
                
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                    coord=[x,y,w,h]
                
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                    cv2.putText(img,"ID: Unknown",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    coord=[x,y,w,h]
                return False

            return coord
        
        #define function again
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            if coord:
                return True,img
            else:              
                return False,img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

        #now set the local binary pattern histogram LBPH algorithm
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        #video_cap=cv2.VideoCapture(0)
        video_cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        video_cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        video_cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        time.sleep(1)
        if not video_cap.isOpened():
           print("Error: Could not open video device")
           return


          
        start_time = time.time()
        while True:
            ret,img=video_cap.read()
            #img=recognize(img,clf,faceCascade)
            found ,img = recognize(img,clf,faceCascade)
            #if found:
            #   break

            cv2.imshow("Welcome To Face Recognition",img)
            if found is True and (time.time() - start_time) >= 15:
               break
            
            if  cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
       


if __name__ == "__main__":    
    root=Tk()
    obj=Face_Recognition(root) 
    root.mainloop()