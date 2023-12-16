from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
import datetime
import mysql.connector
import pandas as pd


class Report:
    def __init__(self,root):
        self.root = root
        self.root.title("The Chippewa Hotel: Reports")
        self.root.geometry("1295x950+250+75")

        #Labeltitle
        lbl_title = Label(self.root, text="GENERATE REPORTS", font=("times new roman", 18, "bold"), bg="black", fg="white", bd=1, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1595, height=50)

        #Logo
        img_1 = Image.open(r"C:\Users\Surya Saikiran\Desktop\Project\Logo.png")
        img_1 = img_1.resize((50, 50), Image.LANCZOS)
        self.photoimg_1 = ImageTk.PhotoImage(img_1)

        label_img = Label(self.root, image=self.photoimg_1, bd=2, relief=RIDGE)
        label_img.place(x=0, y=0, width=50, height=50)

        #Frame
        DataFrameRight = LabelFrame(self.root, bd=3, padx=2, relief=RIDGE, fg="black", font=("times new roman", 12, "bold"), text="Generate Customer Report")
        DataFrameRight.place(x=30, y=70, width=540, height=620)

        #images
        img1 = Image.open(r"C:\Users\Surya Saikiran\Desktop\Project\receptionist-at-hotel.jpeg")
        img1 = img1.resize((500, 350), Image.LANCZOS)
        self.photoImg1 = ImageTk.PhotoImage(img1)
        l1 = Label(DataFrameRight, image=self.photoImg1, borderwidth=0)
        l1.place(x=15, y=10)

        #CustomerreportButton
        btncreport = Button(DataFrameRight, command=self.customer_report, text="Customer Report", font=("times new roman", 12, "bold"), width=21, bg="maroon", fg="gold", relief=RAISED)
        btncreport.place(x=150, y=400)

        #Frame
        DataFrameleft = LabelFrame(self.root, bd=3, padx=2, relief=RIDGE, fg="black",font=("times new roman", 12, "bold"), text="Generate Booking Report")
        DataFrameleft.place(x=600, y=70, width=540, height=620)

        # images
        img2 = Image.open(r"C:\Users\Surya Saikiran\Desktop\Project\04.jpg")
        img2 = img2.resize((500, 350), Image.LANCZOS)
        self.photoImg2 = ImageTk.PhotoImage(img2)
        l2 = Label(DataFrameleft, image=self.photoImg2, borderwidth=0)
        l2.place(x=15, y=10)

        #BillButton
        btnbreport = Button(DataFrameleft, command=self.booking_report, text="Occupancy Report", font=("times new roman", 12, "bold"), width=21, bg="maroon", fg="gold", relief=RAISED)
        btnbreport.place(x=150, y=400)



    def customer_report(self):
        tip = messagebox.askyesno("YesNo", "Click Yes to download the Customer Report")
        if tip > 0:
            db = mysql.connector.connect(host="localhost", user="root", password="surya1@#", database="hotel")
            cursor = db.cursor()
            cursor.execute(
                "SELECT Customer_Ref, first_name, last_name, gender, email, mobile_number, nationality, id_proof, id_number, address , city FROM customer")
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[i[0] for i in cursor.description])
        else:
            if not tip:
                return

        # Create Excel workbook
        title = "Customer Report"
        now = datetime.datetime.now().strftime("%m-%d-%Y %I:%M:%S %p")
        writer = pd.ExcelWriter('customer_report.xlsx', engine='xlsxwriter')
        df.to_excel(writer, index=False, sheet_name=title)

        # Modify the worksheet
        workbook = writer.book
        worksheet = writer.sheets[title]

        # Set column widths
        worksheet.set_column(0, len(df.columns) - 1, 15)

        # Define formats
        title_format = workbook.add_format({'bold': True, 'font_size': 16, 'bg_color': 'yellow', 'align': 'center', 'valign': 'vcenter', 'border': 1})
        datetime_format = workbook.add_format({'bold': True, 'bg_color': '#C5D9F1', 'align': 'center', 'valign': 'vcenter', 'border': 1})
        header_format = workbook.add_format({'bold': True, 'bg_color': '#BFBFBF', 'align': 'center', 'valign': 'vcenter', 'border': 1})
        data_format = workbook.add_format({'border': 1})

        # Write title and datetime to worksheet
        worksheet.merge_range('A1:K1', title, title_format)
        worksheet.merge_range('A2:K2', f"Report Generated on: {now}", datetime_format)

        # Write header row
        for col_num, value in enumerate(df.columns.values):
            worksheet.write(2, col_num, value, header_format)

        # Write data rows
        for row_num, row_data in enumerate(data):
            worksheet.write(row_num + 3, 0, row_data[0], data_format)
            worksheet.write(row_num + 3, 1, row_data[1], data_format)
            worksheet.write(row_num + 3, 2, row_data[2], data_format)
            worksheet.write(row_num + 3, 3, row_data[3], data_format)
            worksheet.write(row_num + 3, 4, row_data[4], data_format)
            worksheet.write(row_num + 3, 5, row_data[5], data_format)
            worksheet.write(row_num + 3, 6, row_data[6], data_format)
            worksheet.write(row_num + 3, 7, row_data[7], data_format)
            worksheet.write(row_num + 3, 8, row_data[8], data_format)
            worksheet.write(row_num + 3, 9, row_data[9], data_format)
            worksheet.write(row_num + 3, 10, row_data[10], data_format)

        writer.save()

        # Show message box
        messagebox.showinfo("Export Successful", "Customer Report has been generated in spreadsheet format")


    def booking_report(self):
        tip = messagebox.askyesno("YesNo", "Click Yes to download the Report")
        if tip > 0:
            db = mysql.connector.connect(host="localhost", user="root", password="surya1@#", database="hotel")
            cursor = db.cursor()
            cursor.execute(
                "SELECT booking_id, customer.first_name, customer.last_name, customer_contact, check_in, check_out, available_room as room, type_of_room, no_of_days, sub_total, tax_paid as tax, total_cost FROM booking INNER JOIN customer ON customer.mobile_number = booking.customer_contact where booking_status = 'Checked-in';")
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[i[0] for i in cursor.description])
        else:
            if not tip:
                return

        # Create Excel workbook
        title = "Occupancy Report"
        now = datetime.datetime.now().strftime("%m-%d-%Y %I:%M:%S %p")
        writer = pd.ExcelWriter('occupancy_report.xlsx', engine='xlsxwriter')
        df.to_excel(writer, index=False, sheet_name=title)

        # Modify the worksheet
        workbook = writer.book
        worksheet = writer.sheets[title]

        # Set column widths
        worksheet.set_column(0, len(df.columns) - 1, 15)

        # Define formats
        title_format = workbook.add_format({'bold': True, 'font_size': 16, 'bg_color': 'yellow', 'align': 'center', 'valign': 'vcenter', 'border': 1})
        datetime_format = workbook.add_format({'bold': True, 'bg_color': '#C5D9F1', 'align': 'center', 'valign': 'vcenter', 'border': 1})
        header_format = workbook.add_format({'bold': True, 'bg_color': '#BFBFBF', 'align': 'center', 'valign': 'vcenter', 'border': 1})
        data_format = workbook.add_format({'border': 1})

        # Write title and datetime to worksheet
        worksheet.merge_range('A1:L1', title, title_format)
        worksheet.merge_range('A2:L2', f"Report Generated on: {now}", datetime_format)

        # Write header row
        for col_num, value in enumerate(df.columns.values):
            worksheet.write(2, col_num, value, header_format)

        # Write data rows
        for row_num, row_data in enumerate(data):
            worksheet.write(row_num + 3, 0, row_data[0], data_format)
            worksheet.write(row_num + 3, 1, row_data[1], data_format)
            worksheet.write(row_num + 3, 2, row_data[2], data_format)
            worksheet.write(row_num + 3, 3, row_data[3], data_format)
            worksheet.write(row_num + 3, 4, row_data[4], data_format)
            worksheet.write(row_num + 3, 5, row_data[5], data_format)
            worksheet.write(row_num + 3, 6, row_data[6], data_format)
            worksheet.write(row_num + 3, 7, row_data[7], data_format)
            worksheet.write(row_num + 3, 8, row_data[8], data_format)
            worksheet.write(row_num + 3, 9, row_data[9], data_format)
            worksheet.write(row_num + 3, 10, row_data[10], data_format)
            worksheet.write(row_num + 3, 11, row_data[11], data_format)
            #worksheet.write(row_num + 3, 12, row_data[12], data_format)
            #worksheet.write(row_num + 3, 13, row_data[13], data_format)

        writer.save()

        # Show message box
        messagebox.showinfo("Export Successful", "Occupancy Report has been generated in spreadsheet format")




if __name__ == "__main__":
    root=Tk()
    obj=Report(root)
    root.mainloop()