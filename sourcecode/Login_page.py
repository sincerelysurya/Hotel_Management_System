from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from main import TheChippewaHotel

def main():
    win = Tk()
    app = Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root = root
        self.root.title("The Chippewa Hotel: Employee Login")
        self.root.geometry("1550x800+0+0")

        #Frame
        frame = Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        #Label
        get_str = Label(frame,text="Employee Login",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=70,y=55)

        #Label
        username = Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=40,y=125)

        #Entry
        self.txtuser = ttk.Entry(frame,font=("times new roman",15))
        self.txtuser.place(x=40,y=150,width=270)

        #Label
        password =lbl= Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=40, y=205)

        #Entry
        self.txtpass = ttk.Entry(frame, font=("times new roman", 15), show="*")
        self.txtpass.place(x=40, y=230, width=270)

        #Loginbutton
        login_button = Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RAISED,fg="white",bg="green")
        login_button.place(x=110,y=300,width=120,height=35)

        #Registerbutton
        register_button = Button(frame,command=self.register_window,text="New User Register",font=("times new roman",10,"bold"),borderwidth=0,fg="gold", bg="black",activebackground="black")
        register_button.place(x=15, y=350, width=160)

        #Forgetpasswordbutton
        forgetpassword_button = Button(frame,command=self.forgot_password_window,text="Forgot Password?",font=("times new roman", 10, "bold"),borderwidth=0,fg="silver",bg="black",activebackground="black")
        forgetpassword_button.place(x=10, y=380, width=160)

        #show_password
        check_button = Checkbutton(frame, command=self.show_password , text="show password", font=("times new roman", 9, "bold"))
        check_button.place(x=40, y=264)

    def show_password(self):
        if self.txtpass.cget('show') == '*':
            self.txtpass.config(show='')
        else:
            self.txtpass.config(show='*')


    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)


    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error","All fields required")
        elif self.txtuser.get() == "admin" and self.txtpass.get() == "password":
            messagebox.showinfo("Valid","Admin Logged in successfully")
            self.new_window = Toplevel(self.root)
            self.app = TheChippewaHotel(self.new_window)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="surya1@#", database="hotel")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from employee where email=%s and password=%s", (
                self.txtuser.get(),
                self.txtpass.get()
            ))

            row = my_cursor.fetchone()
            # print(row)
            if row == None:
                messagebox.showerror("Error", "Invalid Username & password")
            else:
                messagebox.showinfo("Valid", "Click OK to Log in successfully")
                #open_main = messagebox.askyesno("YesNo", "Are you an employee of 'The Chippewa Hotel'?")
                #if open_main > 0:
                self.new_window = Toplevel(self.root)
                self.app = TheChippewaHotel(self.new_window)
                #else:
                #    if not open_main:
                #        return
            conn.commit()
            conn.close()


    #Reset
    def reset_pass(self):
        if self.combo_securiy_Q.get()=="Select" or self.txt_security.get()=="" or self.txt_newpass.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root2)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="surya1@#",database="hotel")
                cur=conn.cursor()
                query=("select * from employee where email=%s and securityQ=%s and securityA=%s")
                value=(self.txtuser.get(),self.combo_securiy_Q.get(),self.txt_security.get(),)
                cur.execute(query,value)
                row=cur.fetchone()
                # print(row)
                if row==None:
                    messagebox.showerror("Error","Please select the correct security question or enter correct answer",parent=self.root2)
                else:
                    query=("update employee set password=%s where email=%s")
                    value=(self.txt_newpass.get(),self.txtuser.get())
                    cur.execute(query,value)
                    # row2=cur.fetchone()
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success","Your password has been reset,Please login with new password",parent=self.root2)
                    self.root2.destroy()
                    # self.reset()
                    self.txtuser.focus()

            except Exception as es:
                messagebox.showerror("Error",f"Error Due To:{str(es)}",parent=self.root2)



    #Password_reset_window
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the e-mail address to reset the password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="surya1@#",database="hotel")
            my_cursor=conn.cursor()
            query=("select * from employee where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","Please enter valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("The Chippewa Hotel: Password reset")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Password reset",font=("times new roman",20,"bold"),bg="green", fg="silver")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select security questions:",font=("times new roman",15,"bold"),fg="black")
                security_Q.place(x=50,y=80)

                self.combo_securiy_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_securiy_Q["values"]=("Select a question","What's your Birth Place?", "What's your favorite color?", "What's your favorite song?")
                self.combo_securiy_Q.place(x=50,y=110,width=250)
                self.combo_securiy_Q.current(0)


                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),fg="black")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_security.place(x=50,y=180,width=250)


                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),fg="black")
                new_password.place(x=50,y=220)

                self.txt_newpass = ttk.Entry(self.root2,font=("times new roman",15,"bold"), show="*")
                self.txt_newpass.place(x=50,y=250,width=250)

                #show_password
                check1_button = Checkbutton(self.root2, command=self.show_reset_password , text="show password", font=("times new roman", 9, "bold"))
                check1_button.place(x=47, y=280)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),bd=3, relief = RAISED, fg="white", bg="green")
                btn.place(x=120,y=320,width=100)

    def show_reset_password(self):
        if self.txt_newpass.cget('show') == '*':
            self.txt_newpass.config(show='')
        else:
            self.txt_newpass.config(show='*')



class Register:
    def __init__(self,root):
        self.root = root
        self.root.title("The Chippewa Hotel: Employee Registration")
        self.root.geometry("1600x900+0+0")

        #Variables
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_password = StringVar()
        self.var_confirm_password = StringVar()
        self.var_check = IntVar()



        #Frame
        frame = Frame(self.root, bg="black")
        frame.place(x=370, y=100, width=800, height=550)

        #RegisterLabel
        register_label = Label(frame, text="Employee Registration",font=("times new roman",20,"bold"),fg="gold",bg="black")
        register_label.place(x=20,y=20)

        #Row1
        #Label&Entry
        fname = Label(frame,text="First Name",font=("times new roman",15,"bold"),fg="white",bg="black")
        fname.place(x=50,y=100)

        fname_entry = ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)

        #Label&Entry
        lname = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), fg="white", bg="black")
        lname.place(x=370, y=100)

        self.txt_lname = ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txt_lname.place(x=370, y=130, width=250)

        #Row2
        #Label&Entry
        contact = Label(frame,text="Contact Number",font=("times new roman",15,"bold"),fg="white",bg="black")
        contact.place(x=50,y=170)

        self.txt_contact = ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.txt_contact.place(x=50,y=200,width=250)

        #Label&Entry
        email = Label(frame,text="E-mail",font=("times new roman", 15, "bold"),fg="white",bg="black")
        email.place(x=370, y=170)

        self.txt_email = ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txt_email.place(x=370,y=200,width=250)

        #Row3
        #Label&combo
        securityQ = Label(frame,text="Security Question",font=("times new roman",15,"bold"),fg="white",bg="black")
        securityQ.place(x=50,y=240)

        self.combo_securityQ = ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_securityQ["values"] = ("Select a question","What's your Birth Place?","What's your favorite color?","What's your favorite song?")
        self.combo_securityQ.place(x=50,y=270,width=250)
        self.combo_securityQ.current(0)

        #Label&Entry
        securityA = Label(frame,text="Security Answer",font=("times new roman",15,"bold"),fg="white",bg="black")
        securityA.place(x=370,y=240)

        self.txt_securityA = ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman", 15, "bold"))
        self.txt_securityA.place(x=370,y=270,width=250)

        #Row4
        #Label&Entry
        password = Label(frame, text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=50,y=310)

        self.txt_password = ttk.Entry(frame,textvariable=self.var_password,font=("times new roman", 15, "bold"), show="*")
        self.txt_password.place(x=50,y=340,width=250)

        #Label&Entry
        confirm_password = Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        confirm_password.place(x=370,y=310)

        self.txt_confirm_password = ttk.Entry(frame,textvariable=self.var_confirm_password,font=("times new roman",15,"bold"), show="*")
        self.txt_confirm_password.place(x=370,y=340,width=250)


        #checkbutton
        checkbutton = Checkbutton(frame,variable=self.var_check,text="I agree to the terms & conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        checkbutton.place(x=50,y=380)

        #Registernowbutton
        registernow_button = Button(frame,command=self.register_data,text="Register now",font=("times new roman",15,"bold"),bd=3,relief=RAISED,fg="white", bg="green", activebackground="black")
        registernow_button.place(x=50,y=440,width=150)

        #Loginbutton
        signin_button = Button(frame,command=self.return_login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RAISED,fg="white",bg="green")
        signin_button.place(x=370,y=440,width=150)



    #Register_data
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select a question":
            messagebox.showerror("Error","All fields are required")
        elif self.var_password.get() != self.var_confirm_password.get():
            messagebox.showerror("Error","Passwords must be same")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error","Must agree to the terms & conditions to continue")
        else:
            conn = mysql.connector.connect(host="localhost",user="root",password="surya1@#",database="hotel")
            my_cursor = conn.cursor()
            query = ("select * from employee where email=%s")
            value = (self.var_email.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exists, please try another email")
            else:
                my_cursor.execute("insert into employee values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                       self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_password.get()
                                                                                     ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registered successfully")
            self.root.destroy()

    def return_login(self):
        self.root.destroy()





if __name__ == "__main__":
    main()