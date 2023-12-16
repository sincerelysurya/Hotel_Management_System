from tkinter import *
from PIL import  Image,ImageTk   #pip install pillow

from datetime import datetime

from Customer import Customer_Window
from Room_Booking import Roombooking
from Room_Details import Room_Details
from Report import Report

class TheChippewaHotel:
    def __init__(self,root):
        self.root = root
        self.root.title("The Chippewa Hotel: Home")
        self.root.geometry("1920x1080+0+0")

        #Title
        label_title = Label(self.root,text="CHIPPEWA HOTEL MANAGEMENT SYSTEM",font=("times new roman",30,"bold"),bg="black",fg="white",bd=1,relief=RIDGE)
        label_title.place(x=0,y=0,width=1550,height=50)

        #Main_Frame
        main_frame = Frame(self.root,bd=0,relief=RIDGE)
        main_frame.place(x=0,y=50,width=1550,height=900)

        #Button_Frame
        button_frame = Frame(main_frame,bd=0,relief=RIDGE)
        button_frame.place(x=0,y=200,width=250,height=250)

        customer_button = Button(button_frame, command=self.cust_details,text="CUSTOMER",width=22,font=("times new roman",16,"bold"),bg="black",fg="White",bd=1,relief=RIDGE)
        customer_button.grid(row=0,column=0,pady=1)

        room_button = Button(button_frame, command= self.roombooking, text="BOOKING", width=22, font=("times new roman", 16, "bold"),bg="black",fg="White",bd=1,relief=RIDGE)
        room_button.grid(row=1, column=0,pady=1)

        details_button = Button(button_frame, command= self.roomdetails, text="ROOM DETAILS", width=22, font=("times new roman", 16, "bold"), bg="black", fg="White", bd=1, relief=RIDGE)
        details_button.grid(row=2, column=0,pady=1)

        report_button = Button(button_frame, command= self.report, text="REPORTS", width=22, font=("times new roman", 16, "bold"), bg="black", fg="White", bd=1, relief=RIDGE)
        report_button.grid(row=3, column=0,pady=1)

        logout_button = Button(button_frame, command= self.logout, text="LOGOUT", width=22, font=("times new roman", 16, "bold"), bg="black", fg="White", bd=1, relief=RIDGE)
        logout_button.grid(row=4, column=0,pady=1)

        #Logo
        img_2 = Image.open(r"C:\Users\Surya Saikiran\Desktop\Project\Logo.png")
        img_2 = img_2.resize((250,250), Image.LANCZOS)
        self.photoimg_2 = ImageTk.PhotoImage(img_2)

        label_img = Label(self.root,image=self.photoimg_2,bd=2,relief=RIDGE)
        label_img.place(x=0,y=0,width=250,height=250)

        #Hotel_Image
        img_1 = Image.open(r"C:\Users\Surya Saikiran\Desktop\Project\pexels-photo-262048.jpeg")
        img_1 = img_1.resize((1580, 820), Image.LANCZOS)
        self.photoimg_1 = ImageTk.PhotoImage(img_1)

        label_img = Label(self.root, image=self.photoimg_1, bd=2, relief=RIDGE)
        label_img.place(x=250,y=50,width=1580,height=820)

        #images
        img_3 = Image.open(r"C:\Users\Surya Saikiran\Desktop\Project\pexels-photo-14022374.jpeg")
        img_3 = img_3.resize((250,340),Image.LANCZOS)
        self.photoimg_3 = ImageTk.PhotoImage(img_3)

        label_img = Label(self.root, image=self.photoimg_3, bd=1, relief=RIDGE)
        label_img.place(x=0,y=460,width=250,height=340)

    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Customer_Window(self.new_window)

    def roombooking(self):
        self.new_window = Toplevel(self.root)
        self.app = Roombooking(self.new_window)

    def roomdetails(self):
        self.new_window = Toplevel(self.root)
        self.app = Room_Details(self.new_window)

    def report(self):
        self.new_window = Toplevel(self.root)
        self.app = Report(self.new_window)

    def logout(self):
        self.root.destroy()









if __name__ == '__main__':
    root = Tk()
    obj = TheChippewaHotel(root)
    root.mainloop()
