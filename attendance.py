from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]
class Attendance:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #============variables========
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

        #first image
        img=Image.open(r"images\att1.jpg")
        img=img.resize((800,200),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        first_label=Label(self.root,image=self.photoimg)
        first_label.place(x=0,y=0,width=800,height=200)

        #second image
        img1=Image.open(r"images\group.jpg")
        img1=img1.resize((800,200),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        first_label=Label(self.root,image=self.photoimg1)
        first_label.place(x=800,y=0,width=800,height=200)

        #background image
        img3=Image.open(r"images\bg1.jpg")
        img3=img3.resize((1530,810),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1530,height=810)

        title_label=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM ",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_label.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1500,height=687)

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=610)

        img_left=Image.open(r"images\face2.jpg")
        img_left=img_left.resize((715,170),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        first_label=Label(Left_frame,image=self.photoimg_left)
        first_label.place(x=5,y=0,width=715,height=170)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=2,y=150,width=720,height=430)

        #labels and entries
        #attendance id
        attendanceId_label=Label(left_inside_frame,text="Attendance-ID:",font=("times new roman",13,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        attendanceID_entry=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_id,font=("comicsansns 11 bold"))
        attendanceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #roll no
        roll_label=Label(left_inside_frame,text="Roll: ",font=("comicsansns 11 bold"),bg="white")
        roll_label.grid(row=0,column=2,padx=4,pady=8)
        
        atten_roll=ttk.Entry(left_inside_frame,textvariable=self.var_atten_roll,width=22,font=("comicsansns 11 bold"))
        atten_roll.grid(row=0,column=3,pady=8)

        #student name 
        name_label=Label(left_inside_frame,text="Name: ",font=("comicsansns 11 bold"),bg="white")
        name_label.grid(row=1,column=0)
        
        atten_name=ttk.Entry(left_inside_frame,textvariable=self.var_atten_name,width=22,font=("comicsansns 11 bold"))
        atten_name.grid(row=1,column=1,pady=8)

        #department
        dep_label=Label(left_inside_frame,text="Department: ",font=("comicsansns 11 bold"),bg="white")
        dep_label.grid(row=1,column=2)
        
        atten_dep=ttk.Entry(left_inside_frame,textvariable=self.var_atten_dep,width=22,font=("comicsansns 11 bold"))
        atten_dep.grid(row=1,column=3,pady=8)

        #time
        time_label=Label(left_inside_frame,text="Time: ",font=("comicsansns 11 bold"),bg="white")
        time_label.grid(row=2,column=0)
        
        atten_time=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_time,font=("comicsansns 11 bold"))
        atten_time.grid(row=2,column=1,pady=8)

        #date
        date_label=Label(left_inside_frame,text="Date: ",font=("comicsansns 11 bold"),bg="white")
        date_label.grid(row=2,column=2)
        
        atten_date=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_date,font=("comicsansns 11 bold"))
        atten_date.grid(row=2,column=3,pady=8)

        #attendance
        attendance_label=Label(left_inside_frame,text="Attendance Status: ",font=("comicsansns 11 bold"),bg="white")
        attendance_label.grid(row=3,column=0)
        
        self.atten_status=ttk.Combobox(left_inside_frame,width=22,textvariable=self.var_atten_attendance,font=("comicsansns 11 bold"))
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

        #button frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=740,height=35)

        save_btn=Button(btn_frame,text="Import CSV",command=self.importCsv,width=17,font=("times new roman",13,"bold"),bg="green",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export CSV",command=self.exportCsv,width=17,font=("times new roman",13,"bold"),bg="green",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman",13,"bold"),bg="green",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="green",fg="white")
        reset_btn.grid(row=0,column=3)





        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=750,y=10,width=740,height=610)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=730,height=445)

        #=========scroll bar========
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","date","time","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview) 

       
        self.AttendanceReportTable.heading("id",text="Attendance-ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)


        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

        #===========fetch data============

    def fetchData(self,rows):
            self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
            for i in rows:
                self.AttendanceReportTable.insert("",END,values=i)

    def importCsv(self):
            global mydata
            mydata.clear() # it clears all the previous data
            fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File", ".csv"),("ALL File","*.*")),parent=self.root)
            if fln:
                with open(fln) as myfile:
                    csvread=csv.reader(myfile,delimiter=",")
                    for i in csvread:
                        mydata.append(i)
                    self.fetchData(mydata)

    # export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
               messagebox.showerror("No Data","No Data found to export",parent=self.root)
               return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File", ".csv"),("ALL File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                 exp_write=csv.writer(myfile,delimiter=",")
                 for i in mydata:
                      exp_write.writerow(i)
                      messagebox.showinfo("Data Export","your data exported to "+os.path.basename(fln)+" Successfully") #from +os. there is file path name which is optional 
        except Exception as es:
            messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root) 

    def get_cursor(self, event=""):
         self.root.update_idletasks() #for smoother use of cursor
         cursor_row=self.AttendanceReportTable.focus()
         content=self.AttendanceReportTable.item(cursor_row)
         rows=content['values']
         self.var_atten_id.set(rows[0])
         self.var_atten_roll.set(rows[1])                                        
         self.var_atten_name.set(rows[2])
         self.var_atten_dep.set(rows[3])
         self.var_atten_time.set(rows[4])
         self.var_atten_date.set(rows[5])
         self.var_atten_attendance.set(rows[6])

    def reset_data(self):
         self.var_atten_id.set("")
         self.var_atten_roll.set("")                                        
         self.var_atten_name.set("")
         self.var_atten_dep.set("")
         self.var_atten_time.set("")
         self.var_atten_date.set("")
         self.var_atten_attendance.set("")

    def update_data(self):
       attendance_id = self.var_atten_id.get()
    
       if attendance_id == "":
           messagebox.showerror("Error", "Please select an attendance record to update", parent=self.root)
           return
    
       updated = False
       for i, row in enumerate(mydata):
           if row[0] == attendance_id:  # Assuming Attendance-ID is index 0
            mydata[i] = [
                self.var_atten_id.get(),
                self.var_atten_roll.get(),
                self.var_atten_name.get(),
                self.var_atten_dep.get(),
                self.var_atten_time.get(),
                self.var_atten_date.get(),
                self.var_atten_attendance.get()
            ]
            updated = True
            break
    
       if updated:
        messagebox.showinfo("Success", "Attendance updated successfully", parent=self.root)
        self.fetchData(mydata)
       else:
        messagebox.showerror("Error", "Attendance ID not found", parent=self.root)


    
    
         
         




        









if __name__ == "__main__":    
    root=Tk()
    obj=Attendance(root) 
    root.mainloop()  