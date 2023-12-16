from tkinter import *
from tkinter import ttk
from PIL import  Image,ImageTk
import random
from tkinter import messagebox
import mysql.connector

class Customer_Window:
    def __init__(self,root):
        self.root = root
        self.root.title("The Chippewa Hotel: Customer")
        self.root.geometry("1295x950+250+75")

        #Variables
        self.var_Customer_Ref = StringVar()
        #x = random.randint(100000,999999)
        #self.var_Customer_Ref.set(str(x))

        self.var_first_name = StringVar()
        self.var_last_name = StringVar()
        self.var_gender = StringVar()
        self.var_email = StringVar()
        self.var_mobile_number = StringVar()
        self.var_nationality = StringVar()
        self.var_post = StringVar()
        self.var_id_proof = StringVar()
        self.var_id_number = StringVar()
        self.var_address = StringVar()
        self.var_city = StringVar()
        self.var_postcode = StringVar()

        #Labeltitle
        lbl_title = Label(self.root, text="ADD CUSTOMER DETAILS",font=("times new roman",18,"bold"),bg="black",fg="white",bd=1,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1595,height=50)

        #Logo
        img_1 = Image.open(r"C:\Users\Surya Saikiran\Desktop\Project\Logo.png")
        img_1 = img_1.resize((50,50), Image.LANCZOS)
        self.photoimg_1 = ImageTk.PhotoImage(img_1)

        label_img = Label(self.root,image=self.photoimg_1,bd=2,relief=RIDGE)
        label_img.place(x=0,y=0,width=50,height=50)

        #LabelFrame
        labelframeleft = LabelFrame(self.root,bd=1,relief=RIDGE,text="Customer Details",font=("times new roman",16,"bold"),padx=2)
        labelframeleft.place(x=5,y=70,width=475,height=640)

        #Label&Entry
        lbl_cust_ref = Label(labelframeleft,text="Customer ID:",font=("arial",16,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        entry_ref = ttk.Entry(labelframeleft,textvariable=self.var_Customer_Ref,width=22,font=("arial",18,"bold"), state="readonly")
        entry_ref.grid(row=0,column=1)

        conn = mysql.connector.connect(host="localhost", username="root", password="surya1@#", database="hotel")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT MAX(customer_ref) FROM customer")
        result = my_cursor.fetchone()

        if result[0] is None:
            total = 1
            self.var_Customer_Ref.set(total)
        else:
            tipe = (int(result[0])) + 1
            self.var_Customer_Ref.set(tipe)

        #FirstName
        fname = Label(labelframeleft,text="First Name:",font=("arial",16,"bold"),padx=2,pady=6)
        fname.grid(row=1, column=0, sticky=W)

        txtfname = ttk.Entry(labelframeleft,textvariable=self.var_first_name, width=22, font=("arial", 18, "bold"))
        txtfname.grid(row=1, column=1)

        #Last_name
        lname = Label(labelframeleft, text="Last Name*:", font=("arial", 16, "bold"), padx=2, pady=6)
        lname.grid(row=2, column=0, sticky=W)

        txtlname = ttk.Entry(labelframeleft,textvariable=self.var_last_name, width=22, font=("arial", 18, "bold"))
        txtlname.grid(row=2, column=1)

        #Gendercombobox
        label_gender = Label(labelframeleft,font=("arial", 16, "bold"),text="Gender:",padx=2,pady=6)
        label_gender.grid(row=3,column=0,sticky=W)

        combo_gender = ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial", 16, "bold"),width=22,state="readonly")
        combo_gender["value"] = ("Male", "Female")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)

        #email
        lblemail = Label(labelframeleft,font=("arial", 16, "bold"),text="Email:",padx=2,pady=6)
        lblemail.grid(row=4,column=0,sticky=W)

        txtemail = ttk.Entry(labelframeleft,textvariable=self.var_email,font=("arial", 16, "bold"),width=24)
        txtemail.grid(row=4,column=1)

        #mobilenumber
        lblmobile = Label(labelframeleft, font=("arial", 16, "bold"), text="Mobile Number*:", padx=2, pady=6)
        lblmobile.grid(row=5, column=0, sticky=W)

        txtmobile = ttk.Entry(labelframeleft,textvariable=self.var_mobile_number, font=("arial", 16, "bold"), width=24)
        txtmobile.grid(row=5, column=1)

        #nationality
        lblnationality = Label(labelframeleft,font=("arial", 16, "bold"),text="Nationality:",padx=2,pady=6)
        lblnationality.grid(row=6,column=0,sticky=W)

        combo_nationality = ttk.Combobox(labelframeleft,textvariable=self.var_nationality, font=("arial", 16, "bold"), width=22, state="readonly")
        combo_nationality["value"] = ("Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic (CAR)", "Chad", "Chile", "China", "Colombia", "Comoros", "Democratic Republic of the Congo", "Republic of the Congo", "Costa Rica", "Cote d'Ivoire", "Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Macedonia (FYROM)", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar (Burma)", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Korea", "Norway", "Oman", "Pakistan", "Palau", "Palestine", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Korea", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates (UAE)", "United Kingdom (UK)", "United States of America (USA)", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City (Holy See)", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe","Other")
        combo_nationality.current(0)
        combo_nationality.grid(row=6, column=1)

        #id_proof_combobox
        lblidproof = Label(labelframeleft,font=("arial", 16, "bold"),text="ID Proof:",padx=2,pady=6)
        lblidproof.grid(row=7,column=0,sticky=W)

        combo_idproof = ttk.Combobox(labelframeleft,textvariable=self.var_id_proof, font=("arial", 16, "bold"), width=22, state="readonly")
        combo_idproof["value"] = ("Driver License", "State ID","University/College ID","Other")
        combo_idproof.current(0)
        combo_idproof.grid(row=7, column=1)

        #idnumber
        lblIdNumber = Label(labelframeleft, font=("arial", 16, "bold"), text="ID Number:", padx=2, pady=6)
        lblIdNumber.grid(row=8, column=0, sticky=W)

        txtIdNumber = ttk.Entry(labelframeleft,textvariable=self.var_id_number,font=("arial", 16, "bold"), width=24)
        txtIdNumber.grid(row=8, column=1)

        #address
        lblAddress = Label(labelframeleft, font=("arial", 16, "bold"), text="Address:", padx=2, pady=6)
        lblAddress.grid(row=9, column=0, sticky=W)

        txtAddress = ttk.Entry(labelframeleft,textvariable=self.var_address,font=("arial", 16, "bold"), width=24)
        txtAddress.grid(row=9, column=1)

        #City
        lblcity = Label(labelframeleft, font=("arial", 16, "bold"), text="City:", padx=2, pady=6)
        lblcity.grid(row=10, column=0, sticky=W)

        txtcity = ttk.Entry(labelframeleft,textvariable=self.var_city, font=("arial", 16, "bold"), width=24)
        txtcity.grid(row=10, column=1)

        #Postcode
        #lblPostCode = Label(labelframeleft, font=("arial", 16, "bold"), text="PostCode:", padx=2, pady=6)
        #lblPostCode.grid(row=11, column=0, sticky=W)

        #txtpostcode = ttk.Entry(labelframeleft,textvariable=self.var_post, font=("arial", 16, "bold"), width=24)
        #txtpostcode.grid(row=11, column=1)

        #Buttonframe
        ButtonFrame = Frame(labelframeleft, bd=0, relief=RAISED)
        ButtonFrame.place(x=0, y=520, width=450, height=40)

        #Buttons
        btnadddata = Button(ButtonFrame,command=self.add_data, text="Save",font=("times new roman", 12, "bold"), width=11,bg="green", fg="white",relief=RAISED)
        btnadddata.grid(row=0, column=0, padx=1)

        btnupdate = Button(ButtonFrame, command=self.update_data, text="Update", font=("times new roman", 12, "bold"), width=11, bg="green", fg="white",relief=RAISED)
        btnupdate.grid(row=0, column=1, padx=1)

        #btnUpdate = Button(ButtonFrame, command=self.mDelete, text="Delete",font=("times new roman", 12, "bold"), width=11, bg="green", fg="white",relief=RAISED)
        #btnUpdate.grid(row=0, column=2, padx=1)

        btnreset = Button(ButtonFrame, command=self.reset_data,text="Reset", font=("times new roman", 12, "bold"), width=12, bg="green", fg="white",relief=RAISED)
        btnreset.grid(row=0, column=3, padx=1)

        # table&Scrollbar
        Table_frame = LabelFrame(self.root, text="Search/View Customer Details", font=("times new roman", 16, "bold"), bd=3, relief=RIDGE)
        Table_frame.place(x=485, y=71, width=820, height=640)

        #Searchby
        lblSearch = Label(Table_frame, font=("times new roman", 15, "bold"), text="Search by:", padx=2, fg="black")
        lblSearch.grid(row=0, column=0, sticky=W, padx=5)

        #variable
        self.search_var = StringVar()
        search_combo = ttk.Combobox(Table_frame, width=12, textvariable=self.search_var, font=("times new roman", 15,"bold"), state="readonly")
        search_combo['values'] = ("Select Option", "Email", "Mobile_number")
        search_combo.grid(row=0, column=1, sticky=W, padx=3)
        search_combo.current(0)

        self.searchTxt_var = StringVar()
        txtSearch = ttk.Entry(Table_frame, width=28, textvariable=self.searchTxt_var, font=("times new roman", 15,"bold"))
        txtSearch.grid(row=0, column=2, padx=1)

        btnExit = Button(Table_frame, text="Search",command= self.search_data ,font=("times new roman", 12, "bold"), width=11, bg="green", fg="white",relief=RAISED)
        btnExit.grid(row=0, column=3, padx=3)

        btnshowall = Button(Table_frame, text="Show all", command= self.fetch_data ,font=("times new roman", 12, "bold"), width=11, bg="green", fg="white",relief=RAISED)
        btnshowall.grid(row=0, column=4, padx=3)

        #Table&Scrollbar
        details_table = Frame(Table_frame, bd=2, relief=RIDGE)
        details_table.place(x=5, y=55, width=780, height=555)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.Cust_Details_Table = ttk.Treeview(details_table, column =("Customer ref","First name","Last name","gender","E-mail","Mobile number","nationality","Id proof","Id number","address","city"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("Customer ref", text="Customer ID")
        self.Cust_Details_Table.heading("First name", text="First Name")
        self.Cust_Details_Table.heading("Last name", text="Last Name")
        self.Cust_Details_Table.heading("gender", text="Gender")
        self.Cust_Details_Table.heading("E-mail", text="E-mail")
        self.Cust_Details_Table.heading("Mobile number", text="Mobile Number")
        self.Cust_Details_Table.heading("nationality", text="Nationality")
        self.Cust_Details_Table.heading("Id proof", text="ID Proof")
        self.Cust_Details_Table.heading("Id number", text="ID Number")
        self.Cust_Details_Table.heading("address", text="Address")
        self.Cust_Details_Table.heading("city", text="City")
        #self.Cust_Details_Table.heading("postcode", text="postcode")

        self.Cust_Details_Table["show"] = "headings"
        self.Cust_Details_Table.column("Customer ref", width=75)
        self.Cust_Details_Table.column("First name", width=130)
        self.Cust_Details_Table.column("Last name", width=80)
        self.Cust_Details_Table.column("gender", width=50)
        self.Cust_Details_Table.column("E-mail", width=150)
        self.Cust_Details_Table.column("Mobile number", width=100)
        self.Cust_Details_Table.column("nationality", width=120)
        self.Cust_Details_Table.column("Id proof", width=100)
        self.Cust_Details_Table.column("Id number", width=100)
        self.Cust_Details_Table.column("address", width=100)
        self.Cust_Details_Table.column("city", width=100)
        #self.Cust_Details_Table.column("postcode", width=100)

        self.Cust_Details_Table.tag_configure('evenrow', background='light grey')
        self.Cust_Details_Table.tag_configure('oddrow', background='white')


        self.Cust_Details_Table.pack(fill=BOTH, expand=1)
        self.fetch_data()

        for i, row in enumerate(self.Cust_Details_Table.get_children()):
            if i % 2 == 0:
                self.Cust_Details_Table.item(row, tags=('evenrow',))
            else:
                self.Cust_Details_Table.item(row, tags=('oddrow',))

        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)

    #Function Declaration

    #add_data
    def add_data(self):
        if self.var_last_name.get() == "" or self.var_mobile_number.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="surya1@#", database="hotel")
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT MAX(customer_ref) FROM customer")
                result = my_cursor.fetchone()

                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                    self.var_Customer_Ref.get(),
                    self.var_first_name.get(),
                    self.var_last_name.get(),
                    self.var_gender.get(),
                    self.var_email.get(),
                    self.var_mobile_number.get(),
                    self.var_nationality.get(),
                    self.var_id_proof.get(),
                    self.var_id_number.get(),
                    self.var_address.get(),
                    self.var_city.get(),
                    self.var_postcode.get()
                     ))

                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                messagebox.showinfo("Success", "Customer has been inserted", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f" Customer already exits in the system", parent=self.root)

    #Update_data
    def update_data(self):
        if self.var_Customer_Ref.get() == "" or self.var_last_name.get() == "" or self.var_mobile_number.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="surya1@#", database="hotel")
            my_cursor = conn.cursor()
            my_cursor.execute("update customer set  first_name=%s,last_name=%s,gender=%s,email=%s,mobile_number=%s,nationality=%s,id_proof=%s,id_number=%s,address=%s,city=%s,postcode=%s where Customer_Ref=%s",(

                    self.var_first_name.get(),
                    self.var_last_name.get(),
                    self.var_gender.get(),
                    self.var_email.get(),
                    self.var_mobile_number.get(),
                    self.var_nationality.get(),
                    self.var_id_proof.get(),
                    self.var_id_number.get(),
                    self.var_address.get(),
                    self.var_city.get(),
                    self.var_postcode.get(),
                    self.var_Customer_Ref.get()
            ))
            conn.commit()
            self.fetch_data()
            self.reset_data()
            conn.close()
            messagebox.showinfo("UPDATE", "Record has been updated successfully", parent=self.root)

    #Fetch_data
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="surya1@#",database="hotel")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer")
        rows = my_cursor.fetchall()
        if len(rows)!= 0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #Get_cursor
    def get_cursor(self,event=""):
        cursor_row = self.Cust_Details_Table.focus()
        content = self.Cust_Details_Table.item(cursor_row)
        row = content["values"]

        self.var_Customer_Ref.set(row[0]),
        self.var_first_name.set(row[1]),
        self.var_last_name.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_email.set(row[4]),
        self.var_mobile_number.set(row[5]),
        self.var_nationality.set(row[6]),
        self.var_id_proof.set(row[7]),
        self.var_id_number.set(row[8]),
        self.var_address.set(row[9]),
        self.var_city.set(row[10]),
        self.var_postcode.set(row[11])

    #Reset_data
    def reset_data(self):
        self.var_first_name.set(""),
        self.var_last_name.set(""),
        self.var_email.set(""),
        self.var_mobile_number.set(""),
        self.var_id_number.set(""),
        self.var_address.set(""),
        self.var_city.set(""),
        self.var_postcode.set("")


    #Delete_data
    def mDelete(self):
        mDelete = messagebox.askyesno("Delete", "Do you want to delete this customer?", parent=self.root)
        if mDelete > 0:
            conn = mysql.connector.connect(host="localhost", username="root", password="surya@1#", database="hotel")
            my_cursor = conn.cursor()
            sql = "delete from customer where customer_ref=%s"
            val = (self.var_Customer_Ref.get(),)
            my_cursor.execute(sql, val)
        else:
            if not mDelete:
                return

        conn.commit()
        self.fetch_data()
        # self.clear_room()
        conn.close()

    #Search_data
    def search_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='surya1@#',database='hotel')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer where " +str(self.search_var.get())+" LIKE '%"+str(self.searchTxt_var.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()




if __name__ == "__main__":
    root = Tk()
    obj = Customer_Window(root)
    root,mainloop()


