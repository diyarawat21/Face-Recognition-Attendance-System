from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from tkinter import StringVar



class Student:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
         
        #variablesss=============
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_stu_id=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_stu_name=StringVar()


        #first image
        img=Image.open(r"D:\Face_Recognition System\images\image.jpg")
        img=img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        first_label=Label(self.root,image=self.photoimg)
        first_label.place(x=0,y=0,width=510,height=130)

        #second image
        img1=Image.open(r"D:\Face_Recognition System\images\face2.jpg")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        first_label=Label(self.root,image=self.photoimg1)
        first_label.place(x=500,y=0,width=500,height=150)

        #third image
        img2=Image.open(r"D:\Face_Recognition System\images\face1.jpg")
        img2=img2.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        first_label=Label(self.root,image=self.photoimg2)
        first_label.place(x=1000,y=0,width=500,height=150)

        #background image
        img3=Image.open(r"D:\Face_Recognition System\images\back.jpg")
        img3=img3.resize((1530,810),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=810)

        title_label=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM ",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_label.place(x=0,y=0,width=1530,height=45)

        #bd=borderlength
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1500,height=687)

        #left label frame

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=780,height=660)
         

        #image
        img_left=Image.open(r"D:\Face_Recognition System\images\face2.jpg")
        img_left=img_left.resize((770,170),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        first_label=Label(Left_frame,image=self.photoimg_left)
        first_label.place(x=5,y=5,width=770,height=170)

        #current course
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course information",font=("times new roman",13,"bold"))
        current_course_frame.place(x=5,y=175,width=767,height=130)

        #department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",13,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",13,"bold"),state="read only")
        dep_combo["values"]=("Select Department","CSE","IT","Civil","Mechanical","Electronics ,BBa , MBA , B.sc")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

        #Course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",13,"bold"),state="read only",width=20)
        course_combo["values"]=("Select Course","AI","ML","IOT","SE","PYTHON, B.Pharma")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year
        Year_label=Label(current_course_frame,text="Year",font=("times new roman",13,"bold"),bg="white")
        Year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",13,"bold"),state="read only",width=20)
        year_combo["values"]=("Select Year","1st year","2nd year","3rd year","4th year","5th year")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",13,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",13,"bold"),state="read only",width=20)
        semester_combo["values"]=("Select Semester","semester-1","semester-2", "semester-3","semester-4","semester-5", "semester-6", "semester-7","semester-8","semester-9","semester-10")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #class student info
        class_Student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student information",font=("times new roman",13,"bold"))
        class_Student_frame.place(x=5,y=310,width=767,height=320)
        
        #studentID
        studentId_label=Label(class_Student_frame,text="StudentID",font=("times new roman",13,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,sticky=W)
        
        studentID_entry=ttk.Entry(class_Student_frame,textvariable=self.var_stu_id,width=20,font=("times new roman",13,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,sticky=W)

        #student name 
        studentName_label=Label(class_Student_frame,text="Student Name: ",font=("times new roman",13,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        studentName_entry=ttk.Entry(class_Student_frame,textvariable=self.var_stu_name,width=20,font=("times new roman",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #class division
        class_div_label=Label(class_Student_frame,text="Class Divison: ",font=("times new roman",13,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        #class_div_entry=ttk.Entry(class_Student_frame,textvariable=self.var_div,width=20,font=("times new roman",13,"bold"))
        #class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        div_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_div,font=("times new roman",13,"bold"),state="read only",width=18)
        div_combo["values"]=("A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #roll no.
        roll_no_label=Label(class_Student_frame,text="Roll No: ",font=("times new roman",13,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        roll_no_entry=ttk.Entry(class_Student_frame,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #dob
        dob_label=Label(class_Student_frame,text="DOB: ",font=("times new roman",13,"bold"),bg="white")
        dob_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        dob_entry=ttk.Entry(class_Student_frame,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #email
        email_label=Label(class_Student_frame,text="EMAIL: ",font=("times new roman",13,"bold"),bg="white")
        email_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        email_entry=ttk.Entry(class_Student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #phone no
        phone_label=Label(class_Student_frame,text="Phone No: ",font=("times new roman",13,"bold"),bg="white")
        phone_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        phone_entry=ttk.Entry(class_Student_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        phone_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #address
        address_label=Label(class_Student_frame,text="Address: ",font=("times new roman",13,"bold"),bg="white")
        address_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        
        address_entry=ttk.Entry(class_Student_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        address_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #gender
        gender_label=Label(class_Student_frame,text="Gender: ",font=("times new roman",13,"bold"),bg="white")
        gender_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        
        #gender_entry=ttk.Entry(class_Student_frame,textvariable=self.var_gender,width=20,font=("times new roman",13,"bold"))
        #gender_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,font=("times new roman",13,"bold"),state="read only",width=18)
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=4,column=1,padx=10,pady=5,sticky=W)


        #teacher name
        teacher_label=Label(class_Student_frame,text="Teacher Name: ",font=("times new roman",13,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        
        teacher_entry=ttk.Entry(class_Student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",13,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radio Buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=5,column=0)

        
        radiobtn2=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=5,column=1)

        #button frame
        btn_frame=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=210,width=750,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=18,font=("times new roman",13,"bold"),bg="green",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=18,font=("times new roman",13,"bold"),bg="green",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=18,font=("times new roman",13,"bold"),bg="green",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=18,font=("times new roman",13,"bold"),bg="green",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=5,y=245,width=750,height=35)

        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=37,font=("times new roman",13,"bold"),bg="green",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=37,font=("times new roman",13,"bold"),bg="green",fg="white")
        update_photo_btn.grid(row=0,column=1)


        #right label frame

        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=810,y=10,width=680,height=660)

        #image
        img_right=Image.open(r"D:\Face_Recognition System\images\studimg.jpg")
        img_right=img_right.resize((770,170),Image.Resampling.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        first_label=Label(Right_frame,image=self.photoimg_right)
        first_label.place(x=5,y=5,width=770,height=170)

        #------search system--------
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",13,"bold"))
        search_frame.place(x=5,y=175,width=665,height=80)

        search_frame_label=Label(search_frame,text="Search By: ",font=("times new roman",15,"bold"),bg="green",fg="white")
        search_frame_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)


        self.search_by = StringVar()
        self.search_entry = StringVar()

        search_combo=ttk.Combobox(search_frame,textvariable=self.search_by,font=("times new roman",12,"bold"),state="readonly",width=13)
        search_combo["values"]=("Select","Roll_No","Phone_No", "Name","StudentID","Email")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,textvariable=self.search_entry,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)


        search_btn=Button(search_frame,text="Search",command=self.search_data,width=12,font=("times new roman",12,"bold"),bg="green",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(search_frame,text="Show   All",command=self.fetch_data,width=14,font=("times new roman",12,"bold"),bg="green",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)

        #table frame----------- 
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE,)
        table_frame.place(x=5,y=260,width=665,height=370)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep", "course", "year", "sem", "id", "name", "div", "roll", "dob", "email", "phone", "address", "teacher", "photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="Student ID")
        self.student_table.heading("name", text="Student Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="Photo Sample Status")

        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=150)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=150)
        self.student_table.column("teacher", width=150)
        self.student_table.column("photo", width=180)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        

    #function declaration
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_stu_name.get()==""or self.var_stu_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",( 

                                                                           self.var_dep.get(),
                                                                           self.var_course.get(),
                                                                           self.var_year.get(),
                                                                           self.var_semester.get(),
                                                                           self.var_stu_id.get(),
                                                                           self.var_stu_name.get(),
                                                                           self.var_div.get(),
                                                                           self.var_roll.get(),
                                                                           self.var_gender.get(),
                                                                           self.var_dob.get(),
                                                                           self.var_email.get(),
                                                                           self.var_phone.get(),
                                                                           self.var_address.get(),
                                                                           self.var_teacher.get(),
                                                                           self.var_radio1.get()

                                                                         ))   
                conn.commit() 
                self.fetch_data()
                conn.close()   
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)                                                           
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)                                          

    #======fetch data========
    def fetch_data(self):   
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
        my_cursor=conn.cursor() 
        my_cursor.execute("Select * from student")  
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())

            for i in data:
                self.student_table.insert("", END, values=i)   
            conn.commit()

        conn.close() 

    # get cursor ------------------
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus) 
        data=content["values"] 

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]), 
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),                                         
        self.var_stu_id.set(data[4]),
        self.var_stu_name.set(data[5]),
        self.var_div.set(data[6]), 
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    #update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_stu_name.get()==""or self.var_stu_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
                    my_cursor=conn.cursor() 
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_ID=%s",(
                                              
                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                        self.var_stu_name.get(),
                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                        self.var_teacher.get(),              
                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                        self.var_stu_id.get()

                                                                                                                                                                    ))
                    
                else:
                    if not update:
                        return
                messagebox.showinfo("Success","Student details successfully update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

#delete function
    def delete_data(self):
        if self.var_stu_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)   
        else:
            try:    
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="root",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_ID=%s"
                    val=(self.var_stu_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)



        #search data===============

            

    def search_data(self):
        selected_column = self.search_by.get()
        search_text_value = self.search_entry.get()

        print(f"DEBUG: Dropdown selected = '{selected_column}'")  # debug
        print(f"DEBUG: Search text = '{search_text_value}'")      # debug

        if selected_column == "Select" or search_text_value.strip() == "":
            messagebox.showerror("Error", "Please select a search criteria and enter value")
            return

        column_map = {
            "Name": "Name",
            "Roll No": "Roll",
            "Phone_No": "Phone",
            "Email": "Email",
            "StudentID": "Student_ID",
            "Department": "department"
        }

        if selected_column not in column_map:
            messagebox.showerror("Error", "Invalid search criteria")
            return

        search_by_value = column_map[selected_column]

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="face_recognizer"
        )
        my_cursor = conn.cursor()

        query = f"SELECT * FROM student WHERE {search_by_value} LIKE %s"
        like_pattern = f"%{search_text_value}%"

        my_cursor.execute(query, (like_pattern,))
        rows = my_cursor.fetchall()
    
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("", END, values=row)
        else:
            messagebox.showinfo("Info", "No records found")

        conn.close()

        

    # reset =============
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_stu_id.set("")
        self.var_stu_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")


    #============Generate dataset Take Photo Sample================
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_stu_name.get()==""or self.var_stu_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
                my_cursor=conn.cursor() 
                my_cursor.execute("Select * from Student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_ID=%s",(
                                              
                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                        self.var_stu_name.get(),
                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                        self.var_teacher.get(),              
                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                        self.var_stu_id.get()

                                                                                                                                                                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
            

                #=============load predefined data on face frontals from opencv=============

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor =1.3
                    #minimum neighbour= 5

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        # if i uncomment this 547th line then there should be black nd white photographs and if we comment this then colorful photograph willl aprear on the camera
                        #face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path , face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==50:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)





                   


        

        


if __name__ == "__main__":    
    root=Tk()
    obj=Student(root) 
    root.mainloop()  
