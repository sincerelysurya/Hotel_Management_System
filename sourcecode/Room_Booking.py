from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from fpdf import FPDF
from datetime import datetime
from tkinter import messagebox
import mysql.connector
from tkcalendar import DateEntry
from Room_Details import Room_Details

class Roombooking:
    def __init__(self,root):
        self.root = root
        self.root.title("The Chippewa Hotel: Room-Booking")
        self.root.geometry("1295x950+250+75")

        #Variables
        self.var_Booking_ID = IntVar()
        self.var_Customer_contact = StringVar()
        self.var_Checkin = StringVar()
        self.var_Checkout = StringVar()
        self.var_type_of_room = StringVar()
        self.var_available_room = StringVar()
        self.var_No_of_Days = StringVar()
        self.var_tax_paid = StringVar()
        self.var_sub_total = StringVar()
        self.var_total_cost = StringVar()
        self.var_booking_status = StringVar()

        #Labeltitle
        lbl_title = Label(self.root, text="ROOM BOOKING", font=("times new roman", 18, "bold"), bg="black",fg="white", bd=1, relief=GROOVE)
        lbl_title.place(x=0, y=0, width=1595, height=50)

        #Logo
        img_1 = Image.open(r"C:\Users\Surya Saikiran\Desktop\Project\Logo.png")
        img_1 = img_1.resize((50, 50), Image.LANCZOS)
        self.photoimg_1 = ImageTk.PhotoImage(img_1)

        label_img = Label(self.root, image=self.photoimg_1, bd=2, relief=RIDGE)
        label_img.place(x=0, y=0, width=50, height=50)

        #LabelFrame
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Room booking", font=("times new roman", 16, "bold"), padx=2)
        labelframeleft.place(x=5, y=70, width=495, height=640)

        #Label&Entry
        #Customercontact
        lbl_cust_contact = Label(labelframeleft, text="Customer contact:", font=("arial", 16, "bold"), padx=2, pady=6)
        lbl_cust_contact.grid(row=0, column=0, sticky=W)

        entry_contact = ttk.Entry(labelframeleft,textvariable= self.var_Customer_contact , width=22, font=("arial", 18, "bold"))
        entry_contact.grid(row=0, column=1, sticky=W)

        #Fetchdatabutton
        btnFetchData = Button(labelframeleft, command= self.fetch_contact ,text="Fetch data", font=("times new roman", 12, "bold"), width=11, bg="green", fg="white", relief=GROOVE)
        btnFetchData.place(x=377,y=4)

        #Booking_ID
        lbl_Booking_ID = Label(labelframeleft, text="Booking ID:", font=("arial", 16, "bold"), padx=2, pady=6)
        lbl_Booking_ID.grid(row=1, column=0, sticky=W)

        ent_Booking_ID = ttk.Entry(labelframeleft, textvariable=self.var_Booking_ID, width=22, font=("arial", 18, "bold"), state="readonly")
        ent_Booking_ID.grid(row=1, column=1, sticky=W)

        conn = mysql.connector.connect(host="localhost", username="root", password="surya1@#", database="hotel")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT MAX(booking_id) FROM booking")
        result = my_cursor.fetchone()

        if result[0] is None:
            total = 19980709
            self.var_Booking_ID.set(total)
        else:
            tipe = (int(result[0])) + 1
            self.var_Booking_ID.set(tipe)

        #Check-in_date
        check_in_date = Label(labelframeleft, text="Check-in Date:", font=("arial", 16, "bold"), padx=2, pady=6)
        check_in_date.grid(row=2, column=0, sticky=W)

        txtcheck_in_date = DateEntry(labelframeleft,textvariable= self.var_Checkin,background='darkgreen', foreground='white', date_pattern='mm/dd/yyyy', width=20, font=("arial", 18, "bold"), state="readonly")
        txtcheck_in_date.grid(row=2, column=1, sticky=W)

        txtcheck_in_date.bind('<Return>', self.set_check_in_date)
        txtcheck_in_date.bind('<Tab>', self.set_check_in_date)

        #Check-out_date
        check_out_date = Label(labelframeleft, text="Check-out Date:", font=("arial", 16, "bold"), padx=2, pady=6)
        check_out_date.grid(row=3, column=0, sticky=W)

        txtcheck_out_date = DateEntry(labelframeleft, textvariable=self.var_Checkout, background='darkgreen', foreground='white', date_pattern='mm/dd/yyyy', width=20, font=("arial", 18, "bold"), state="readonly")
        txtcheck_out_date.grid(row=3, column=1, sticky=W)

        txtcheck_out_date.bind('<Return>', self.set_check_out_date)
        txtcheck_out_date.bind('<Tab>', self.set_check_out_date)

        #Availableroom
        lblRoomAvailable = Label(labelframeleft, text="Room:", font=("arial", 16, "bold"), padx=2, pady=6)
        lblRoomAvailable.grid(row=4, column=0, sticky=W)

        conn = mysql.connector.connect(host="localhost", user="root", password="surya1@#", database="hotel")
        my_cursor = conn.cursor()
        my_cursor.execute("select roomno from roomdetails where roomstatus ='Available'")
        rows = my_cursor.fetchall()

        combo_Roomno = ttk.Combobox(labelframeleft, textvariable=self.var_available_room, font=("arial", 18, "bold"), width=20, state="readonly")
        combo_Roomno["value"] = rows
        combo_Roomno.current(0)
        combo_Roomno.grid(row=4, column=1, sticky=W)

        #combo_RoomType = ttk.Combobox(labelframeleft,textvariable= self.var_type_of_room, font=("arial", 16, "bold"), width=22,state="readonly")
        #combo_RoomType["value"] = ("Single", "Double", "Premium")
        #combo_RoomType.current(0)
        #combo_RoomType.grid(row=3, column=1)

        #txtRoomAvailable = ttk.Entry(labelframeleft,textvariable= self.var_available_room, width=22, font=("arial", 18, "bold"))
        #txtRoomAvailable.grid(row=4, column=1)

        # Book Room button
        #book_button = Button(labelframeleft, command=self.book_room, text="Book Room",font=("times new roman", 14, "bold"), bg="blue", fg="white", width=14, bd=4, relief=RIDGE)
        #book_button.grid(row=5, column=1, padx=2, pady=6)

        #BillButton
        btnBill = Button(labelframeleft, command=self.total, text="Calculate", font=("times new roman", 12, "bold"), width=11, bg="green", fg="white", relief=RAISED)
        btnBill.grid(row=5, column=1, padx=2, pady=6)

        # Roomtype
        label_RoomType = Label(labelframeleft, font=("arial", 16, "bold"), text="Room type:", padx=2, pady=6)
        label_RoomType.grid(row=6, column=0, sticky=W)

        txtRoomType = ttk.Entry(labelframeleft, textvariable=self.var_type_of_room, width=22, font=("arial", 18, "bold"), state="readonly")
        txtRoomType.grid(row=6, column=1)

        #NoofDays
        lblNoofDays = Label(labelframeleft, text="No. of Days:", font=("arial", 16, "bold"), padx=2, pady=6)
        lblNoofDays.grid(row=7, column=0, sticky=W)

        txtNoofDays = ttk.Entry(labelframeleft,textvariable= self.var_No_of_Days, width=22, font=("arial", 18, "bold"), state="readonly")
        txtNoofDays.grid(row=7, column=1)

        #Subtotal
        lblSubtotal = Label(labelframeleft, text="Sub Total:", font=("arial", 16, "bold"), padx=2, pady=6)
        lblSubtotal.grid(row=8, column=0, sticky=W)

        txtSubtotal = ttk.Entry(labelframeleft, textvariable=self.var_sub_total, width=22, font=("arial", 18, "bold"))
        txtSubtotal.grid(row=8, column=1)

        #Taxpaid
        lblTaxPaid = Label(labelframeleft, text="Tax:", font=("arial", 16, "bold"), padx=2, pady=6)
        lblTaxPaid.grid(row=9, column=0, sticky=W)

        txtTaxPaid = ttk.Entry(labelframeleft,textvariable= self.var_tax_paid, width=22, font=("arial", 18, "bold"))
        txtTaxPaid.grid(row=9, column=1)

        #TotalCost
        lblTotalCost = Label(labelframeleft, text="Total Cost:", font=("arial", 16, "bold"), padx=2, pady=6)
        lblTotalCost.grid(row=10, column=0, sticky=W)

        txtTotalCost = ttk.Entry(labelframeleft,textvariable= self.var_total_cost, width=22, font=("arial", 18, "bold"))
        txtTotalCost.grid(row=10, column=1)


        #Buttonframe
        ButtonFrame = Frame(labelframeleft, bd=0, relief=RAISED)
        ButtonFrame.place(x=0, y=540, width=490, height=40)

        #Buttons
        btn_Add_Data = Button(ButtonFrame,command= self.add_data, text="Confirm Booking", font=("times new roman", 12, "bold"), width=15, bg="green", fg="white", relief=RAISED)
        btn_Add_Data.grid(row=0, column=0, padx=1)

        btn_Update_Data = Button(ButtonFrame,command= self.update_data, text="Update", font=("times new roman", 12, "bold"), width=9, bg="yellow", fg="black", relief=RAISED)
        btn_Update_Data.grid(row=0, column=1, padx=1)

        btn_cancel_booking = Button(ButtonFrame, command=self.cancel_booking, text="Cancel Booking", font=("times new roman", 12, "bold"), width=15, bg="red", fg="black", relief=RAISED)
        btn_cancel_booking.grid(row=0, column=2, padx=1)

        btnReset = Button(ButtonFrame,command= self.reset_data,  text="Reset", font=("times new roman", 12, "bold"), width=10, bg="green", fg="white", relief=RAISED)
        btnReset.grid(row=0, column=3, padx=1)

        #Buttonframe2
        ButtonFrame2 = Frame(labelframeleft, bd=0, relief=RAISED)
        ButtonFrame2.place(x=0, y=500, width=450, height=40)

        #Buttons
        #btn_printbill = Button(ButtonFrame2, command=self.print_receipt , text="Print Receipt", font=("times new roman", 12, "bold"), width=15, bg="green", fg="white", relief=RAISED)
        #btn_printbill.grid(row=0, column=0, padx=1)

        btn_checkin = Button(ButtonFrame2, command=self.check_in, text="Check-in", font=("times new roman", 12, "bold"), width=15, bg="green", fg="white", relief=RAISED)
        btn_checkin.grid(row=0, column=1, padx=1)

        btn_checkout = Button(ButtonFrame2, command=self.check_out, text="Check-out", font=("times new roman", 12, "bold"), width=15, bg="green", fg="white", relief=RAISED)
        btn_checkout.grid(row=0, column=2, padx=1)


        #table&Scrollbar
        Table_frame = LabelFrame(self.root, text="View/Search Details", font=("times new roman", 16, "bold"), bd=3, relief=RIDGE)
        Table_frame.place(x=503, y=350, width=780, height=360)

        #Searchby
        lblSearch = Label(Table_frame, font=("times new roman", 15, "bold"), text="Search by:", padx=2, fg="black")
        lblSearch.grid(row=0, column=0, sticky=W, padx=5)

        #variable
        self.serch_var = StringVar()
        search_combo = ttk.Combobox(Table_frame, width=12, textvariable=self.serch_var, font=("times new roman", 15, "bold"), state="readonly")
        search_combo['values'] = ("Customer_contact", "Available_room")
        search_combo.grid(row=0, column=1, sticky=W, padx=3)
        search_combo.current(0)

        self.serchTxt_var = StringVar()
        txtSearch = ttk.Entry(Table_frame, width=28, textvariable=self.serchTxt_var, font=("times new roman", 15, "bold"))
        txtSearch.grid(row=0, column=2, padx=1)

        btnSearch = Button(Table_frame,command=self.search_data, text="Search", font=("times new roman", 12, "bold"), width=11, bg="green", fg="white", relief=RAISED)
        btnSearch.grid(row=0, column=3, padx=3)

        btnShowall = Button(Table_frame,command=self.fetch_data, text="Show all", font=("times new roman", 12, "bold"), width=11, bg="green", fg="white", relief=RAISED)
        btnShowall.grid(row=0, column=4, padx=3)

        #Show_details_table

        details_table = Frame(Table_frame, bd=2, relief=RIDGE)
        details_table.place(x=5, y=55, width=760, height=270)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.room_table = ttk.Treeview(details_table, column=("Booking_ID", "Customer_contact", "Check-in_Date", "Check-out_Date",  "Available_Room", "Type_of_Room", "No_of_Days", "Sub_Total", "Tax_Paid", "Total_Cost", "booking_status"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("Booking_ID", text="Booking ID")
        self.room_table.heading("Customer_contact", text="Customer Contact")
        self.room_table.heading("Check-in_Date", text="Check-in date")
        self.room_table.heading("Check-out_Date", text="Check-out date")
        self.room_table.heading("Available_Room", text="Room Number")
        self.room_table.heading("Type_of_Room", text="Room Type")
        self.room_table.heading("No_of_Days", text="Number of Days")
        self.room_table.heading("Sub_Total", text="Sub total")
        self.room_table.heading("Tax_Paid", text="Tax paid")
        self.room_table.heading("Total_Cost", text="Total cost")
        self.room_table.heading("booking_status", text="Booking Status")

        self.room_table["show"] = "headings"

        self.room_table.column("Booking_ID", width=100)
        self.room_table.column("Customer_contact", width=100)
        self.room_table.column("Check-in_Date", width=100)
        self.room_table.column("Check-out_Date", width=100)
        self.room_table.column("Available_Room", width=100)
        self.room_table.column("Type_of_Room", width=100)
        self.room_table.column("No_of_Days", width=100)
        self.room_table.column("Sub_Total", width=100)
        self.room_table.column("Tax_Paid", width=100)
        self.room_table.column("Total_Cost", width=100)
        self.room_table.column("booking_status", width=100)

        self.room_table.tag_configure('evenrow', background='light grey')
        self.room_table.tag_configure('oddrow', background='white')

        self.room_table.pack(fill=BOTH, expand=1)
        self.fetch_data()

        for i, row in enumerate(self.room_table.get_children()):
            if i % 2 == 0:
                self.room_table.item(row, tags=('evenrow',))
            else:
                self.room_table.item(row, tags=('oddrow',))

        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)


    #Function_Declaration

    def fetch_contact(self):
        if self.var_Customer_contact.get() == "":
            messagebox.showerror("Error", "Please enter a customer contact number", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="surya1@#", database="hotel")
            my_cursor = conn.cursor()
            query = ("select first_name from customer where mobile_number=%s")
            value = (self.var_Customer_contact.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","Number not found",parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDframe = Frame(self.root, bd=4, relief=RIDGE, padx=2)
                showDframe.place(x=505, y=82, width=775, height=250)

                lbldetails = Label(showDframe, text="Customer Details", font=("times new roman", 16, "bold"))
                lbldetails.place(x=0, y=0)


                lblfname = Label(showDframe, text="First name:", font=("arial", 12, "bold"))
                lblfname.place(x=0, y=40)

                lbl = Label(showDframe, text=row, font=("arial", 12, "bold"))
                lbl.place(x=150, y=40)

                #Lastname
                conn = mysql.connector.connect(host="localhost", user="root", password="surya1@#", database="hotel")
                my_cursor = conn.cursor()
                query = ("select last_name from customer where mobile_number=%s")
                value = (self.var_Customer_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lbllname = Label(showDframe, text="Last name:", font=("arial", 12, "bold"))
                lbllname.place(x=0, y=70)

                lbl1 = Label(showDframe, text=row, font=("arial", 12, "bold"))
                lbl1.place(x=150, y=70)

                #Gender
                conn = mysql.connector.connect(host="localhost", user="root", password="surya1@#", database="hotel")
                my_cursor = conn.cursor()
                query = ("select gender from customer where mobile_number=%s")
                value = (self.var_Customer_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblgender = Label(showDframe, text="Gender:", font=("arial", 12, "bold"))
                lblgender.place(x=0, y=100)

                lbl1 = Label(showDframe, text=row, font=("arial", 12, "bold"))
                lbl1.place(x=150, y=100)

                #email
                conn = mysql.connector.connect(host="localhost", user="root", password="surya1@#", database="hotel")
                my_cursor = conn.cursor()
                query = ("select email from customer where mobile_number=%s")
                value = (self.var_Customer_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblemail = Label(showDframe, text="E-mail:", font=("arial", 12, "bold"))
                lblemail.place(x=0, y=130)

                lbl1 = Label(showDframe, text=row, font=("arial", 12, "bold"))
                lbl1.place(x=150, y=130)


                #Mobilenumber
                conn = mysql.connector.connect(host="localhost", user="root", password="surya1@#", database="hotel")
                my_cursor = conn.cursor()
                query = ("select mobile_number from customer where mobile_number=%s")
                value = (self.var_Customer_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblmobilenumber = Label(showDframe, text="Mobile number:", font=("arial", 12, "bold"))
                lblmobilenumber.place(x=0, y=160)

                lbl1 = Label(showDframe, text=row, font=("arial", 12, "bold"))
                lbl1.place(x=150, y=160)


                #Nationality
                #conn = mysql.connector.connect(host="localhost", user="root", password="surya1@#", database="hotel")
                #my_cursor = conn.cursor()
                #query = ("select nationality from customer where mobile_number=%s")
                #value = (self.var_Customer_contact.get(),)
                #my_cursor.execute(query, value)
                #row = my_cursor.fetchone()

                #lblnationality = Label(showDframe, text="Nationality:", font=("arial", 12, "bold"))
                #lblnationality.place(x=0, y=190)

                #lbl1 = Label(showDframe, text=row, font=("arial", 12, "bold"))
                #lbl1.place(x=150, y=190)

    #add_data
    def add_data(self):
        if self.var_Customer_contact.get() == "" or self.var_Checkin.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="surya1@#", database="hotel")
                my_cursor = conn.cursor()

                # Get the room status for the selected room
                query = "SELECT roomstatus FROM roomdetails WHERE roomno = %s"
                my_cursor.execute(query, (self.var_available_room.get(),))
                room_status = my_cursor.fetchone()[0]

                if room_status == "Available":
                    self.var_booking_status.set("Booked")
                    my_cursor.execute("INSERT INTO booking VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                      (
                                          self.var_Booking_ID.get(),
                                          self.var_Customer_contact.get(),
                                          self.var_Checkin.get(),
                                          self.var_Checkout.get(),
                                          self.var_available_room.get(),
                                          self.var_type_of_room.get(),
                                          self.var_No_of_Days.get(),
                                          self.var_sub_total.get(),
                                          self.var_tax_paid.get(),
                                          self.var_total_cost.get(),
                                          self.var_booking_status.get()
                                      ))

                    # Update the room status to "Booked"
                    update_query = "UPDATE roomdetails SET roomstatus = %s WHERE roomno = %s"
                    my_cursor.execute(update_query, ("Booked", self.var_available_room.get()))

                    conn.commit()
                    self.fetch_data()
                    messagebox.showinfo("Success", "Room booked successfully!!", parent=self.root)
                else:
                    messagebox.showerror("Error", "This room is not available!", parent=self.root)

                conn.close()

            except Exception as es:
                messagebox.showerror("Error", f"This Room has already been booked: {str(es)}", parent=self.root)

    #Cancel_booking
    def cancel_booking(self):
        if self.var_Booking_ID.get() == "":
            messagebox.showerror("Error", "Please select a booking to cancel!", parent=self.root)
        elif self.var_booking_status.get() == "Completed":
            messagebox.showerror("Error", "This booking has been completed and cannot be canceled.", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="surya1@#", database="hotel")
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT available_room FROM booking WHERE Booking_ID=%s", (self.var_Booking_ID.get(),))
                result = my_cursor.fetchone()

                if result is None:
                    messagebox.showerror("Error", "Enter a booking ID to cancel", parent=self.root)

                elif self.var_booking_status.get() == "Canceled":
                    messagebox.showwarning("Warning", "This booking has already been canceled!", parent=self.root)

                else:
                    value = messagebox.askyesno("YesNo", "Do you want to cancel this booking?")
                    if value > 0:
                        my_cursor.execute(
                            "UPDATE booking b JOIN roomdetails r ON b.available_room=r.roomno SET b.booking_status='Canceled', r.roomstatus='Available' WHERE b.Booking_ID=%s",
                            (self.var_Booking_ID.get(),))
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("Success", "Booking has been canceled!!", parent=self.root)
                    else:
                        if not value:
                            return
            except Exception as es:
                messagebox.showerror("Error", f"Unable to cancel booking: {str(es)}", parent=self.root)

    #fetch_data
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="surya1@#", database="hotel")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from booking")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    #get_cursor
    def get_cursor(self, event=""):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content["values"]

        self.var_Booking_ID.set(row[0]),
        self.var_Customer_contact.set(row[1]),
        self.var_Checkin.set(row[2]),
        self.var_Checkout.set(row[3]),
        self.var_available_room.set(row[4]),
        self.var_type_of_room.set(row[5]),
        self.var_No_of_Days.set(row[6]),
        self.var_sub_total.set(row[7]),
        self.var_tax_paid.set(row[8]),
        self.var_total_cost.set(row[9]),
        self.var_booking_status.set(row[10])


    #update_data
    def update_data(self):
        if self.var_Customer_contact.get() == "" or self.var_Checkin.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="surya1@#", database="hotel")
            my_cursor = conn.cursor()
            my_cursor.execute(
                "update booking set check_in=%s,check_out=%s,type_of_room=%s,available_room=%s,no_of_days=%s,tax_paid=%s,sub_total=%s,total_cost=%s  where customer_contact=%s",
                (
                    self.var_Checkin.get(),
                    self.var_Checkout.get(),
                    self.var_type_of_room.get(),
                    self.var_available_room.get(),
                    self.var_No_of_Days.get(),
                    self.var_tax_paid.get(),
                    self.var_sub_total.get(),
                    self.var_total_cost.get(),
                    self.var_Customer_contact.get()

                ))
            conn.commit()
            self.fetch_data()
            #self.reset()
            conn.close()
            messagebox.showinfo("UPDATE", "Record has been updated successfully", parent=self.root)

    #reset_data
    def reset_data(self):
        #self.var_Customer_contact.set("")
        self.var_Checkin.set("")
        self.var_Checkout.set("")
        self.var_available_room.set("")
        self.var_No_of_Days.set("")
        self.var_tax_paid.set("")
        self.var_sub_total.set("")
        self.var_total_cost.set("")

    #search_data
    def search_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="surya1@#", database="hotel")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from booking where " +str(self.serch_var.get())+" LIKE '%"+str(self.serchTxt_var.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    #delete
    def roomDelete(self):
        mDelete = messagebox.askyesno("Chippewa Hotel Management System", "Do you want to delete this booking?", parent=self.root)
        if mDelete > 0:
            conn = mysql.connector.connect(host="localhost", username="root", password="surya1@#", database="hotel")
            my_cursor = conn.cursor()
            sql = "delete from booking where customer_contact=%s"
            val = (self.var_Customer_contact.get(),)
            my_cursor.execute(sql, val)
        else:
            if not mDelete:
                return

        conn.commit()
        self.fetch_data
        conn.close()

    def check_in(self):
        if self.var_Customer_contact.get() == "" or self.var_Booking_ID.get() == "" or self.var_available_room.get() =="":
            messagebox.showwarning("Warning", "All fields are required to check-in!")
        elif self.var_booking_status.get() == "Canceled":
            messagebox.showerror("Error", "This booking is canceled and cannot be checked-in!")
        elif self.var_booking_status.get() == "Booked":
            conn =mysql.connector.connect(host="localhost", user="root", password="surya1@#", database="hotel")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT available_room FROM booking WHERE Booking_ID=%s", (self.var_Booking_ID.get(),))
            result = my_cursor.fetchone()
            my_cursor.execute("UPDATE booking b JOIN roomdetails r ON b.available_room=r.roomno SET r.roomstatus='Occupied' WHERE b.Booking_ID=%s", (self.var_Booking_ID.get(),))
            my_cursor.execute("UPDATE booking SET booking_status='Checked-in' WHERE Booking_ID=%s", (self.var_Booking_ID.get(),))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Check-in successful!!", parent=self.root)
        else:
            messagebox.showerror("Error","404 not found")


    def check_out(self):
        if self.var_Customer_contact.get() == "" or self.var_Booking_ID.get() == "" or self.var_available_room.get() =="":
            messagebox.showwarning("Warning", "All fields are required to check-out!")
        elif self.var_booking_status.get() == "Canceled":
            messagebox.showerror("Error", "This booking is canceled and cannot be checked-out!")
        elif self.var_booking_status.get() == "Checked-in":
            conn =mysql.connector.connect(host="localhost", user="root", password="surya1@#", database="hotel")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT available_room FROM booking WHERE Booking_ID=%s", (self.var_Booking_ID.get(),))
            result = my_cursor.fetchone()
            my_cursor.execute("UPDATE booking b JOIN roomdetails r ON b.available_room=r.roomno SET r.roomstatus='Available' WHERE b.Booking_ID=%s", (self.var_Booking_ID.get(),))
            my_cursor.execute("UPDATE booking SET booking_status='Checked-out' WHERE Booking_ID=%s", (self.var_Booking_ID.get(),))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Check-out successful!!", parent=self.root)
        else:
            messagebox.showerror("Error","404 not found")




    #total
    def total(self):
        if self.var_Checkin.get() <= self.var_Checkout.get():
            room_no = self.var_available_room.get()
            conn = mysql.connector.connect(host="localhost", user="root", password="surya1@#", database="hotel")
            cursor = conn.cursor()
            sql = "select roomtype from roomdetails where roomno=%s"
            val = (room_no,)
            cursor.execute(sql,val)
            result = cursor.fetchone()
            self.var_type_of_room.set(str(result[0]))

            InDate = self.var_Checkin.get()
            OutDate = self.var_Checkout.get()
            InDate = datetime.strptime(InDate, "%m/%d/%Y")
            OutDate = datetime.strptime(OutDate, "%m/%d/%Y")
            self.var_No_of_Days.set(abs(OutDate - InDate).days + 1)

            if (self.var_type_of_room.get() == "Single"):
                q1 = float(69)
                q2 = float(self.var_No_of_Days.get())
                q3 = float(q1 * q2)
                Tax = "$" + str("%.2f" % ((q3) * 0.09))
                ST = "$" + str("%.2f" % ((q3)))
                TT = "$" + str("%.2f" % (q3 + ((q3) * 0.09)))
                self.var_tax_paid.set(Tax)
                self.var_sub_total.set(ST)
                self.var_total_cost.set(TT)

            elif (self.var_type_of_room.get() == "Double"):
                q1 = float(99)
                q2 = float(self.var_No_of_Days.get())
                q3 = float(q1 * q2)
                Tax = "$" + str("%.2f" % ((q3) * 0.09))
                ST = "$" + str("%.2f" % ((q3)))
                TT = "$" + str("%.2f" % (q3 + ((q3) * 0.09)))
                self.var_tax_paid.set(Tax)
                self.var_sub_total.set(ST)
                self.var_total_cost.set(TT)

            elif (self.var_type_of_room.get() == "Premium"):
                q1 = float(149)
                q2 = float(self.var_No_of_Days.get())
                q3 = float(q1 * q2)
                Tax = "$" + str("%.2f" % ((q3) * 0.15))
                ST = "$" + str("%.2f" % ((q3)))
                TT = "$" + str("%.2f" % (q3 + ((q3) * 0.15)))
                self.var_tax_paid.set(Tax)
                self.var_sub_total.set(ST)
                self.var_total_cost.set(TT)
        else:
            messagebox.showwarning("Warning", "Kindly review the Check-in and Check-out dates!", parent=self.root)

    def set_check_in_date(self, event):
        selected_date = self.var_Checkin.get_date()
        self.var_Checkin.set_date(selected_date)

    def set_check_out_date(self, event):
        selected_date = self.var_Checkout.get_date()
        self.var_Checkout.set_date(selected_date)

    def print_receipt(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="surya1@#", database="hotel")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM booking WHERE Booking_ID=%s", (self.var_Booking_ID.get(),))
        data = my_cursor.fetchall()

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Set page border and titles
        pdf.set_line_width(1)
        pdf.rect(5.0, 5.0, 200.0, 287.0)
        pdf.set_font("Arial", size=18, style='B')
        pdf.cell(200, 20, "THE CHIPPEWA HOTEL", 0, 1, 'C')
        pdf.cell(200, 20, "Receipt", 0, 1, 'C')
        pdf.set_font("Arial", size=12)

        # Print column names with corresponding data
        column_names = [name + ":" for name in my_cursor.column_names]
        spacer_cell_width = 25
        for row in data:
            for i, column_name in enumerate(column_names):
                pdf.cell(spacer_cell_width, 10, "", border=0)  # add spacer cell
                pdf.cell(50, 10, str(column_name), border=0)
                pdf.cell(10, 10, ":", border=0)
                pdf.set_font("Arial", size=14)
                pdf.cell(60, 10, str(row[i]), border=0)
                pdf.set_font("Arial", size=12)
                pdf.ln()
            pdf.ln(15)

        pdf.output("Invoice.pdf")

        conn.commit()
        self.fetch_data()
        conn.close()


if __name__ == "__main__":
    root = Tk()
    obj = Roombooking(root)
    root,mainloop()