from tkinter import*
import tkinter
from tkinter import ttk
from tkinter import messagebox
import datetime
from PIL import Image,ImageTk
from time import strftime
from datetime import datetime
import mysql.connector
import random

class Room_Details:
    def __init__(self,root):
        self.root = root
        self.root.title("The Chippewa Hotel: Room Details")
        self.root.geometry("1295x950+250+75")

        #Labeltitle
        lbl_title = Label(self.root, text="MODIFY ROOM DETAILS", font=("times new roman", 18, "bold"), bg="black",fg="white", bd=1, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1595, height=50)

        #Logo
        img_1 = Image.open(r"C:\Users\Surya Saikiran\Desktop\Project\Logo.png")
        img_1 = img_1.resize((50, 50), Image.LANCZOS)
        self.photoimg_1 = ImageTk.PhotoImage(img_1)

        label_img = Label(self.root, image=self.photoimg_1, bd=2, relief=RIDGE)
        label_img.place(x=0, y=0, width=50, height=50)

        #Frame
        DataFrameRight = LabelFrame(self.root, bd=3, padx=2, relief=RIDGE, fg="black", font=("times new roman", 12, "bold"), text="Modify Room Details")
        DataFrameRight.place(x=30, y=70, width=540, height=620)

        #images
        img1 = Image.open(r"C:\Users\Surya Saikiran\Desktop\Project\hotel-1979406_960_720.jpg")
        img1 = img1.resize((500, 250), Image.LANCZOS)
        self.photoImg1 = ImageTk.PhotoImage(img1)
        l1 = Label(DataFrameRight, image=self.photoImg1, borderwidth=0)
        l1.place(x=15, y=10)

        #Labels & Entry

        #floor
        l_floor = Label(DataFrameRight, text="Floor:", fg="black", font=("times new roman", 15, "bold"))
        l_floor.place(x=15, y=280)

        self.floor_add_var = StringVar()
        floor_combo = ttk.Combobox(DataFrameRight, width=21, textvariable=self.floor_add_var, font=("times new roman", 15, "bold"), state="readonly")
        floor_combo['values'] = ("1", "2", "3", "4", "5")
        floor_combo.place(x=135, y=280)
        floor_combo.current(0)

        #roomno
        l_roomNo = Label(DataFrameRight, text="Room No:", fg="black", font=("times new roman", 15,"bold"))
        l_roomNo.place(x=15, y=330)

        self.room_add_var = StringVar()
        entry_roomno = ttk.Entry(DataFrameRight, textvariable=self.room_add_var, width=23, font=("times new roman", 15, "bold"))
        entry_roomno.place(x=135, y=330)

        #roomtype
        l_roomType = Label(DataFrameRight, text="Room Type:", fg="black", font=("times new roman", 15, "bold"))
        l_roomType.place(x=15, y=380)

        self.type_room = StringVar()
        roomType_combo = ttk.Combobox(DataFrameRight, width=21, textvariable=self.type_room, font=("times new roman", 15, "bold"), state="readonly")
        roomType_combo['values'] = ("Single", "Double", "Premium")
        roomType_combo.place(x=135, y=380)
        roomType_combo.current(0)

        #roomstatus
        l_roomstatus = Label(DataFrameRight, text="Room Status:", fg="black", font=("times new roman", 15, "bold"))
        l_roomstatus.place(x=15, y=430)

        self.room_status = StringVar()
        roomstatus_combo = ttk.Combobox(DataFrameRight, width=21, textvariable=self.room_status, font=("times new roman", 15, "bold"))
        roomstatus_combo['values'] = ("Available", "Occupied", "Maintenance")
        roomstatus_combo.place(x=135, y=430)
        roomstatus_combo.current(0)

        #Rightsideframe
        side_frame = LabelFrame(self.root, bd=4, text="Show Room Details", relief=RIDGE, font=("times new roman", 12, "bold"))
        side_frame.place(x=650, y=70, width=600, height=620)

        sc_x = ttk.Scrollbar(side_frame, orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM, fill=X)
        sc_y = ttk.Scrollbar(side_frame, orient=VERTICAL)
        sc_y.pack(side=RIGHT, fill=Y)

        self.room_table = ttk.Treeview(side_frame, column=("floor", "roomno", "roomtype", "roomstatus"), xscrollcommand=sc_x.set, yscrollcommand=sc_y.set)

        sc_x.config(command=self.room_table.xview)
        sc_y.config(command=self.room_table.yview)

        self.room_table.heading("floor", text="Floor")
        self.room_table.heading("roomno", text="Room No")
        self.room_table.heading("roomtype", text="Room Type")
        self.room_table.heading("roomstatus", text="Room Status")

        self.room_table["show"] = "headings"
        self.room_table.column("floor", width=20)
        self.room_table.column("roomno", width=50)
        self.room_table.column("roomtype", width=50)
        self.room_table.column("roomstatus", width=50)

        self.room_table.tag_configure('evenrow', background='light grey')
        self.room_table.tag_configure('oddrow', background='white')


        self.room_table.pack(fill=BOTH, expand=1)
        self.fetch_Room_data()

        for i, row in enumerate(self.room_table.get_children()):
            if i % 2 == 0:
                self.room_table.item(row, tags=('evenrow',))
            else:
                self.room_table.item(row, tags=('oddrow',))

        self.room_table.bind("<ButtonRelease>", self.get_cursor)




        button_frame = Frame(DataFrameRight, bd=0, relief=RIDGE)
        button_frame.place(x=15, y=500, width=480, height=40)

        add_btn = Button(button_frame, command= self.add_room , text="Save", font=("times new roman", 12, "bold"), width=12, fg="white", bg="green")
        add_btn.grid(row=0, column=0, pady=2)

        update_btn = Button(button_frame, command= self.room_update,text="Update", font=("times new roman", 12, "bold"), width=12, fg="white", bg="green")
        update_btn.grid(row=0, column=1, pady=2)

        delete_btn = Button(button_frame, command=self.roomDelete, text="Delete", font=("times new roman", 12, "bold"), width=12, fg="white", bg="green")
        delete_btn.grid(row=0, column=2, pady=2)

        #clear_btn = Button(button_frame, command=self.clear_room, text="Reset", font=("times new roman", 12, "bold"), width=12, fg="white", bg="green")
        #clear_btn.grid(row=0, column=3, pady=2)

    #Function_Declaration
    def add_room(self):
        if self.floor_add_var.get() == "" or self.room_add_var.get() == "" or self.room_add_var.get() == "":
            messagebox.showerror("Error", "All fields required", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="surya1@#", database="hotel")
            my_cursor = conn.cursor()
            my_cursor.execute("insert into roomdetails values(%s,%s,%s,%s)", (
                self.floor_add_var.get(),
                self.room_add_var.get(),
                self.type_room.get(),
                self.room_status.get()

            ))
            conn.commit()
            self.fetch_Room_data()
            # self.catchdata()
            self.clear_room()

            conn.close()
            messagebox.showinfo("Success", "Room Added successfully!!", parent=self.root)

    #Fetch_Data
    def fetch_Room_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="surya1@#", database="hotel")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from roomdetails")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("", END, values=i)
            conn.commit()
        conn.close()


    #clear_room
    def clear_room(self):
        self.floor_add_var.set("")
        self.room_add_var.set("")
        # self.type_room.set("")

    #get_cursor
    def get_cursor(self, event=" "):
        cursor_rows = self.room_table.focus()
        content = self.room_table.item(cursor_rows)
        row = content["values"]

        self.floor_add_var.set(row[0])
        self.room_add_var.set(row[1])
        self.type_room.set(row[2])
        self.room_status.set(row[3])

    #Delete
    def roomDelete(self):
        mDelete = messagebox.askyesno("Hotel Management System", "Do you delete this Room?", parent=self.root)
        if mDelete > 0:
            conn = mysql.connector.connect(host="localhost", user="root", password="surya1@#", database="hotel")
            my_cursor = conn.cursor()
            sql = "delete from roomdetails where roomno=%s"
            val = (self.room_add_var.get(),)
            my_cursor.execute(sql, val)
        else:
            if not mDelete:
                return

        conn.commit()
        self.fetch_Room_data()
        self.clear_room()
        conn.close()

    #Update
    def room_update(self):
        if self.floor_add_var.get() == "" or self.room_add_var.get() == "" or self.type_room.get() == "":
            messagebox.showwarning("Warning", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="surya1@#", database="hotel")
                my_cursor = conn.cursor()
                my_cursor.execute("update roomdetails set floor=%s, roomtype=%s, roomstatus=%s where roomno=%s", (
                    self.floor_add_var.get(),
                    self.type_room.get(),
                    self.room_status.get(),
                    self.room_add_var.get()
                ))
                conn.commit()
                self.fetch_Room_data()
                self.clear_room()
                conn.close()
                messagebox.showinfo("Success", "Data Successfully updated", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)




if __name__ == "__main__":
    root=Tk()
    obj=Room_Details(root)
    root.mainloop()