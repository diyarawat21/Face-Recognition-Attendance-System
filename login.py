from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk  #pip install pillow
from tkinter import messagebox
import random
import time
import datetime
import mysql.connector
import os

from main import Face_Recognition_System
from train import Train
from time import strftime
from datetime import datetime
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
import tkinter
from student import Student




def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()



class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.var_email = StringVar()
        self.var_pass = StringVar()

        self.bg=ImageTk.PhotoImage(file=r"images\login.jpg")
        label_bg=Label(self.root,image=self.bg)
        label_bg.place(x=0,y=0,relwidth=1,relheight=1)

        self.frame=Frame(self.root,bg="white")
        self.frame.place(x=610,y=170,width=340,height=450)

        img=Image.open(r"images\logo.jpg")
        img1=img.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img1)
        labelimg1=Label(image=self.photoimage,bg="white",borderwidth=0)
        labelimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(self.frame,text="Get Started",font=("times new roman",20,"bold"),fg="black",bg="white")
        get_str.place(x=95,y=100)

        #label
        username=Label(self.frame,text="Username",font=("times new roman",15,"bold"),fg="black",bg="white")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(self.frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=Label(self.frame,text="Password (0 to 9)",font=("times new roman",15,"bold"),fg="black",bg="white")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(self.frame,font=("times new roman",15,"bold"),show="*")
        self.txtpass.place(x=40,y=250,width=270)

        # Show/Hide button
        self.show_password = False
        self.btn_toggle = Button(self.frame, text="Show", command=self.toggle_password, font=("times new roman", 10), bg="white", bd=0)
        self.btn_toggle.place(x=300, y=210)

        #=======Icon Images==========
        img=Image.open(r"images\logo.jpg")
        img2=img.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        labelimg2=Label(image=self.photoimage2,bg="white",borderwidth=0)
        labelimg2.place(x=650,y=323,width=25,height=25)

        #=======Icon Images==========
        img=Image.open(r"images\lock1.jpg")
        img3=img.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        labelimg3=Label(image=self.photoimage3,bg="white",borderwidth=0)
        labelimg3.place(x=650,y=397,width=25,height=25)

        #loginbutton
        loginbtn=Button(self.frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="black",bg="lavender",activeforeground="black",activebackground="lavender")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #registerbutton
        registerbtn=Button(self.frame,command=self.register_window,text="New User Register",font=("times new roman",10,"bold"),borderwidth=0,fg="black",bg="white",activeforeground="black",activebackground="white")
        registerbtn.place(x=15,y=350,width=160)

        #forgetpasswordbutton
        forgetbtn=Button(self.frame,command=self.forgot_password_window,text="Forget Password",font=("times new roman",10,"bold"),borderwidth=0,fg="black",bg="white",activeforeground="black",activebackground="white")
        forgetbtn.place(x=10,y=370,width=160)

    def toggle_password(self):
        if self.show_password:
           self.txtpass.config(show="*")
           self.btn_toggle.config(text="Show")
           self.show_password = False
        else:
            self.txtpass.config(show="")
            self.btn_toggle.config(text="Hide")
            self.show_password = True

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):
       if self.txtuser.get() == "" or self.txtpass.get() == "":
        messagebox.showerror("Error", "All fields are required")

       elif self.txtuser.get() == "user" and self.txtpass.get() == "123":
        messagebox.showinfo("Success", "Login Successfully!")
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition_System(self.new_window)

       else:
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="face_recognizer"
            )
            my_cursor = conn.cursor()

            # Use local variables (no self.)
            username_or_email = self.txtuser.get().strip()
            password = self.txtpass.get().strip()

            # Correct SQL query with placeholders
            my_cursor.execute(
                "SELECT * FROM register WHERE (email=%s OR fname=%s) AND password=%s",
                (username_or_email, username_or_email, password)
            )

            row = my_cursor.fetchone()

            if row is None:
                messagebox.showerror("Error", "Invalid Username or Password")
            else:
                open_main = messagebox.askyesno("Access", "Access allowed only for Admin. Continue?")
                if open_main:
                    self.new_window = Toplevel(self.root)
                    self.app = Face_Recognition_System(self.new_window)
                else:
                    return

        except Exception as e:
            messagebox.showerror("Error", f"Database Error: {str(e)}")

        finally:
            conn.close()

 
            #reset password=====================
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Invalid Username & Password",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="root",database="face_recognizer")
                my_cursor=conn.cursor()
                query=("SELECT * FROM register WHERE email=%s AND securityQ=%s AND securityA=%s")
                value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get())
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                if row==None:
                        messagebox.showerror("Error","Please enter the correct Answer",parent=self.root2)
                else:
                    query=("UPDATE register SET password=%s WHERE email=%s")
                    value=(self.txt_newpass.get(),self.txtuser.get())
                    my_cursor.execute(query,value)


                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Info","Your password has been changed , please enter the new password",parent=self.root2)

                    self.root2.destroy()
            except Exception as e:
                    messagebox.showerror("Error", f"Database Error: {str(e)}", parent=self.root2)

                    



#forgot password window================================

    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error"," Please enter your email to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("SELECT * FROM register WHERE email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)
            conn.close()

            if row==None:
                messagebox.showerror("Error","Please enter the valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="brown",bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text='Select Security Questions',font=("times new roman",15,"bold"),bg="white",fg="black")
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your Partner Name","Your Pet Name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)

                security_A=Label(self.root2,text=' Security Answer',font=("times new roman",15,"bold"),bg="white",fg="black")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_security.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text='New Password',font=("times new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_newpass.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="lavender",bg="purple")
                btn.place(x=100,y=290)


                



class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        #variables==============
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityA=StringVar()
        self.var_securityQ=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        

        #-----background image-------
        self.bg=Image.open("images/register.jpg")
        self.bg=self.bg.resize((1600,900),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(self.bg)

        label_bg=Label(self.root,image=self.photoimg)
        label_bg.place(x=0,y=0,relwidth=1,relheight=1)

        #-----left image-------
        self.left=Image.open("images/pum.jpg")
        self.left=self.left.resize((1600,900),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(self.left)

        label_left=Label(self.root,image=self.photoimg1)
        label_left.place(x=50,y=100,width=470,height=550)
        
        #frame=======

        frame=Frame(self.root,bg='white')
        frame.place(x=520,y=100,width=800,height=550)

        register_label=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="red",bg='white')
        register_label.place(x=20,y=20)
     
        #labels and entry==========

        fname=Label(frame,text='First Name', font=("times new roman",15,"bold"),bg='white')
        fname.place(x=50,y=100)

        self.txt_fname=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.txt_fname.place(x=50,y=130,width=250)

        l_name=Label(frame,text='Last Name',font=("times new roman",15,"bold"),bg="white",fg="black")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

        #row2==================

        contact=Label(frame,text='Contact No',font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text='Email',font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)

        #=========row3

        security_Q=Label(frame,text='Select Security Questions',font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Partner Name","Your Pet Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text=' Security Answer',font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)

        #row4-===============

        pswd=Label(frame,text='Password',font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text='Confirm Password',font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

        #=======check button============

        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I agree to Terms & Conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

        #=========buttons=============

        img=Image.open("images/noww.jpg")
        img=img.resize((200,50),Image.Resampling.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)

        self.b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",bg="white",activebackground="white")
        self.b1.place(x=0,y=420,width=200)

        img1=Image.open("images/log1.png")
        img1=img1.resize((250,50),Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)

        self.b2=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2",bg="white",activebackground="white")
        self.b2.place(x=370,y=420,width=300)

        #==========function declaration===========

    def register_data(self):
       try:
           if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
                  messagebox.showerror("Error","All fields are required")
           elif self.var_pass.get()!=self.var_confpass.get():
               messagebox.showerror("Error","Password & Confirm Password must be same")
           elif self.var_check.get()==0:
                  messagebox.showerror("Error","Please agree our terms and conditions")
           else:
              conn = mysql.connector.connect(host="localhost", user="root", password="root", database="face_recognizer")
              my_cursor = conn.cursor()
              query = "SELECT * FROM register WHERE email=%s"
              value = (self.var_email.get(),)
              my_cursor.execute(query, value)
              row = my_cursor.fetchone()

              if row is not None:
                messagebox.showerror("Error", "User already exists. Please try another email.")
              else:
                my_cursor.execute("INSERT INTO register VALUES (%s,%s,%s,%s,%s,%s,%s)", (
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()
                                                                                     ))
                conn.commit()
                messagebox.showinfo("Success", "Registered Successfully")
                conn.close()
       except Exception as e:
           messagebox.showerror("Database Error", f"Error due to: {str(e)}")

    def return_login(self):
        self.root.destroy()  


class Face_Recognition_System:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #first image
        img=Image.open(r"images\tech.jpg")
        img=img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        first_label=Label(self.root,image=self.photoimg)
        first_label.place(x=0,y=0,width=500,height=150)

        #second image
        img1=Image.open(r"images\face.jpg")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        first_label=Label(self.root,image=self.photoimg1)
        first_label.place(x=500,y=0,width=500,height=150)

        #third image
        img2=Image.open(r"images\college.jpg")
        img2=img2.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        first_label=Label(self.root,image=self.photoimg2)
        first_label.place(x=1000,y=0,width=500,height=150)

        #background image
        img3=Image.open(r"images\back.jpg")
        img3=img3.resize((1530,810),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=810)

        title_label=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_label.place(x=0,y=0,width=1530,height=45)

        #===========time=========
        def time():
            string=strftime("%H:%M:%S%p")
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl= Label(title_label,font =('times new roman',14,'bold'),background='white',foreground='gray')
        lbl.place(x=0,y=0,width=110,height=50)
        time()


        #student button
        img4=Image.open(r"images\student1.jpg")
        img4=img4.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1= Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=200)

        b1_1= Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=200,y=300,width=220,height=40)

        
        #detect  face  button
        img5=Image.open(r"images\face.jpg")
        img5=img5.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1= Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=200)

        b1_1= Button(bg_img,text="Face Detector ",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=500,y=300,width=220,height=40)


        #attendance  button
        img6=Image.open(r"images\attendance.jpg")
        img6=img6.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1= Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=100,width=220,height=200)

        b1_1= Button(bg_img,text="Attendance Details ",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=800,y=300,width=220,height=40)

        #Help desk button
        img7=Image.open(r"images\help.jpg")
        img7=img7.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1= Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_desk_data)
        b1.place(x=1100,y=100,width=220,height=200)

        b1_1= Button(bg_img,text="Help Desk ",cursor="hand2",command=self.help_desk_data,font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=1100,y=300,width=220,height=40)

        #Train data button
        img8=Image.open(r"images\capturing.jpg")
        img8=img8.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1= Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=380,width=220,height=220)

        b1_1= Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=200,y=580,width=220,height=40)

        #Photos button
        img9=Image.open(r"images\photos.jpg")
        img9=img9.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1= Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220)

        b1_1= Button(bg_img,text="Photos ",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=500,y=580,width=220,height=40)

        #Developer button
        img10=Image.open(r"images\developer.jpg")
        img10=img10.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1= Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=800,y=380,width=220,height=220)

        b1_1= Button(bg_img,text="Developer ",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=800,y=580,width=220,height=40)


        #Exit button
        img11=Image.open(r"images\exit.jpg")
        img11=img11.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1= Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1100,y=380,width=220,height=220)

        b1_1= Button(bg_img,text="Exit ",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=1100,y=580,width=220,height=40)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition"," Are you sure you want to exit from this project",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return


        #functions button=================
         
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
           

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_desk_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)











if __name__=="__main__":
    main()


   