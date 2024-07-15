import os
from tkinter import*
from tkinter import Tk, Frame, Label, Entry, StringVar,ttk,filedialog,messagebox
from tkcalendar import DateEntry
import pandas as pd
import openpyxl
from PIL import Image,ImageTk
import database
class Employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title('Employee Management System')
        self.root.config(bg='#163149')
        # self.root.resizable(True,True)
        # Variables
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_age = StringVar()
        self.var_gender = StringVar()
        
        self.var_phone = StringVar()
        self.var_Date_Of_Birth = StringVar()
        self.var_email = StringVar()
        self.var_department = StringVar()
        self.var_Date_Of_joining = StringVar()
        self.var_skill = StringVar()
        self.var_bs = StringVar()
        self.var_ts = StringVar()
        self.var_address = StringVar()
        self.var_search=StringVar()
        self.var_search_text = StringVar()
        # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        # Frames
        # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        # image frame
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=10,y=0,width=1898,height=210)      
        img1=Image.open('Images/ems.jpg')
        img1=img1.resize((1890,210),Image.LANCZOS)
        self.photo1=ImageTk.PhotoImage(img1)
        self.img_1=Label(img_frame,image=self.photo1)
        self.img_1.place(x=0,y=0,width=1895,height=200)
        # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        # main frame
        Main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='#0e7579')
        Main_frame.place(x=10,y=220,width=1895,height=780)
        # upper frame
        Entry_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='Employee Information',font=('times new roman',11,'bold'),fg='red')
        Entry_frame.place(x=10,y=10,width=1870,height=420)
        Entry_frame_bg = Image.open('Images/back.jpg')  # Replace 'path_to_your_image.jpg' with your image file path
        Entry_frame_bg = Entry_frame_bg.resize((1870, 420), Image.LANCZOS)  # Resize the image to fit the frame
        self.upper_frame_bg_photo = ImageTk.PhotoImage(Entry_frame_bg)
        self.upper_frame_bg_label = Label(Entry_frame, image=self.upper_frame_bg_photo)
        self.upper_frame_bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        # button frame
        button_frame = Frame(Entry_frame, bd=2, relief=RIDGE, bg='white')
        button_frame.place(x=300, y=320, width=1105, height=50)
        # down frame
        Down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='Employee Table',font=('times new roman',11,'bold'),fg='red')
        Down_frame.place(x=10,y=435,width=1870,height=330)
         # search frame
        search_frame=LabelFrame(Down_frame,bd=2,relief=RIDGE,bg='white',text='Search Table',font=('times new roman',11,'bold'),fg='red')
        search_frame.place(x=5,y=0,width=1855,height=60)
         # employee table
        table_frame=Frame(Down_frame,bd=2,relief=RIDGE,bg='white')
        table_frame.place(x=5,y=60,width=1855,height=240)
        #///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        # /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        emp_ID = Label(Entry_frame, text="Employee ID", font=('Calibri', 16))
        emp_ID.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        txt_id = Entry(Entry_frame, textvariable=self.var_id, font=('Calibri', 16), width=25, bd=2)
        txt_id.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        Name = Label(Entry_frame,text="Name",font=('Calibri', 16))
        Name.grid(row=1,column=2,padx=10,pady=10,sticky="w")
        txt_name = Entry(Entry_frame,textvariable=self.var_name,font=('Calibri',16),width=28,bd=2)
        txt_name.grid(row=1,column=3,padx=10,pady=10,sticky="w")

        Age = Label(Entry_frame, text="Age", font=("Calibri", 16))
        Age.grid(row=1, column=4, padx=10, pady=10, sticky="w")
        txt_Age = Entry(Entry_frame, textvariable=self.var_age, font=("Calibri", 16), width=24, bd=2)
        txt_Age.grid(row=1, column=5, padx=10, pady=10, sticky="w")

        Gender = Label(Entry_frame, text="Gender", font=("Calibri", 16))
        Gender.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        comboGender = ttk.Combobox(Entry_frame, font=("Calibri", 16), width=23, textvariable=self.var_gender,
                                   state="readonly")
        comboGender['values'] = ("Select Gender", "Male", "Female")
        comboGender.current(0)
        comboGender.grid(row=2, column=1, padx=10, sticky="w")

        Phone = Label(Entry_frame, text="Phone No", font=("Calibri", 16))
        Phone.grid(row=2, column=2, padx=1, pady=10, sticky="w")
        
        txt_phone = Entry(Entry_frame, textvariable=self.var_phone, font=("Calibri", 16), width=28, bd=2)
        txt_phone.grid(row=2, column=3, padx=10, pady=10, sticky="w")

        Date_of_Birth = Label(Entry_frame, text="Date_Of_Birth", font=("Calibri", 16))
        Date_of_Birth.grid(row=2, column=4, padx=10, pady=10, sticky="w")
        Date_Of_Birth_cal = DateEntry(Entry_frame, textvariable=self.var_Date_Of_Birth, font=("Calibri", 16), width=23, bd=2)
        Date_Of_Birth_cal.grid(row=2, column=5, padx=10, pady=10, sticky="w")

        Email = Label(Entry_frame, text="Email Id", font=('Calibri', 16))
        Email.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        txt_Email = Entry(Entry_frame, textvariable=self.var_email, font=('Calibri', 16), width=25, bd=2)
        txt_Email.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        Dipartment = Label(Entry_frame, text="Department", font=("Calibri", 16))
        Dipartment.grid(row=3, column=2, padx=10, pady=10, sticky="w")
        comboDipartment = ttk.Combobox(Entry_frame, font=("Calibri", 16), width=26, textvariable=self.var_department,
                                       state="readonly")
        comboDipartment['values'] = ("Select Department", "HR", "Softwere Enginiyaer", "Developer", "Tester", "Worker")
        comboDipartment.current(0)
        comboDipartment.grid(row=3, column=3, padx=10, sticky="w")

        Date_of_join = Label(Entry_frame, text="Date_Of_Joining", font=("Calibri", 16))
        Date_of_join.grid(row=3, column=4, padx=10, pady=10, sticky="w")
        Date_Of_joine_cal = DateEntry(Entry_frame, textvariable=self.var_Date_Of_joining, font=("Calibri", 16), width=23, bd=2)
        Date_Of_joine_cal.grid(row=3, column=5, padx=10, pady=10, sticky="w")

        Skill = Label(Entry_frame, text="Skill", font=("Calibri", 16))
        Skill.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        comboSkill = ttk.Combobox(Entry_frame, font=("Calibri", 16), width=23, textvariable=self.var_skill,
                                       state="readonly")
        comboSkill['values'] = ("Select Skill", "Accounting", "Python", "Java", "SQL", "Python & SQL", "Java & SQL","NULL")
        comboSkill.current(0)
        comboSkill.grid(row=4, column=1, padx=10, sticky="w")

        Basic = Label(Entry_frame, text="Basic salary", font=('Calibri', 16))
        Basic.grid(row=4, column=2, padx=10, pady=10, sticky="w")
        txt_Basic = Entry(Entry_frame, textvariable=self.var_bs, font=('Calibri', 16), width=28, bd=2)
        txt_Basic.grid(row=4, column=3, padx=10, pady=10, sticky="w")

        Total = Label(Entry_frame, text="Total Salary", font=('Calibri', 16))
        Total.grid(row=4, column=4, padx=10, pady=10, sticky="w")
        txt_Total = Entry(Entry_frame, textvariable=self.var_ts, font=('Calibri', 16), width=24, bd=2)
        txt_Total.grid(row=4, column=5, padx=10, pady=10, sticky="w")

        Address = Label(Entry_frame, text="Address", font=("Calibri", 16))
        Address.grid(row=5, column=0, padx=10, pady=10, sticky="w")
        txt_Address = Entry(Entry_frame, width=90 , font=("Calibri", 16),textvariable=self.var_address)
        txt_Address.grid(row=5, column=1, columnspan=4, padx=10, sticky="w")
        # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        img_mask=Image.open('Images/emplogo.png')
        img_mask=img_mask.resize((220,200),Image.LANCZOS)
        self.photomas=ImageTk.PhotoImage(img_mask)
        self.img_mask=Label(Entry_frame,image=self.photomas)
        self.img_mask.place(x=1600,y=1,width=220,height=200)
        # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        # BUttons
        style = ttk.Style()
        style.theme_use('clam')
        # Create buttons with different styles
        style = ttk.Style()
        style.theme_use('clam')
        # Create buttons with different styles
        style.configure('Save.TButton',
                        font=('Arial', 15, 'bold'),
                        foreground='white',
                        background='#4079e5',  # Set the background color for 'Save' button
                        borderwidth=0,
                        width=18,
                        padding=5
                        )
        btn_save = ttk.Button(button_frame, text="Save", style='Save.TButton',command=self.insert)
        btn_save.grid(row=0, column=0, padx=5, pady=5)

        style.configure('Update.TButton',
                        font=('Arial', 15, 'bold'),
                        foreground='white',
                        background='#40E645',  # Set the background color for 'Update' button
                        borderwidth=0,
                        width=18,
                        padding=5
                        )
        btn_update = ttk.Button(button_frame, text="Update", style='Update.TButton',command=self.update)
        btn_update.grid(row=0, column=1, padx=5, pady=5)

        style.configure('Delete.TButton',
                        font=('Arial', 15, 'bold'),
                        foreground='white',
                        background='#E64040',  # Set the background color for 'Delete' button
                        borderwidth=0,
                        width=18,
                        padding=5
                        )
        btn_delete = ttk.Button(button_frame, text="Delete", style='Delete.TButton',command=self.delete)
        btn_delete.grid(row=0, column=2, padx=5, pady=5)

        style.configure('Clear.TButton',
                        font=('Arial', 15, 'bold'),
                        foreground='white',
                        background='#e5db40',  # Set the background color for 'Clear' button
                        borderwidth=0,
                        width=18,
                        padding=5
                        )
        btn_clear = ttk.Button(button_frame, text="Clear", style='Clear.TButton',command=self.clear_fields)
        btn_clear.grid(row=0, column=3, padx=5, pady=5)

        style.configure('Print.TButton',
                        font=('Arial', 15, 'bold'),
                        foreground='white',
                        background='#e69940',  # Set the background color for 'Print' button
                        borderwidth=0,
                        width=18,
                        padding=5,
                        )
        btn_print = ttk.Button(button_frame, text="Print Data",style='Print.TButton',command=self.download_database)
        btn_print.grid(row=0, column=4, padx=5, pady=5)
        # search
        com_text_search=ttk.Combobox(search_frame,state="readonly",font=("arial",12,"bold"),textvariable=self.var_search,width=18)
        com_text_search['value']=("Select Option","Phone","id")
        com_text_search.current(0)
        com_text_search.grid(row=0,column=1,sticky=W,padx=5)
        text_search=ttk.Entry(search_frame,width=22,font=('arial',11,'bold'),textvariable=self.var_search_text)
        text_search.grid(row=0,column=2,padx=5)

        style.configure('Search.TButton',
                        font=('Arial', 15, 'bold'),
                        foreground='white',
                        borderwidth=1,
                        width=14,
                        padding=2,
                        background='blue')
        btn_search=ttk.Button(search_frame,command=self.search,text="Search",style='Search.TButton')
        btn_search.grid(row=0,column=3,padx=5)
        btn_showAll=ttk.Button(search_frame,command=self.showall,text="Show All",style='Search.TButton')
        btn_showAll.grid(row=0,column=4,padx=5)       
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_Y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.employee_table=ttk.Treeview(table_frame,column=("ID","Name","Age","Gender","Phone","Date_Of_Birth","Email","Department","Date_of _Joining","Skill","Basic Salary","Total Salary","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_Y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_Y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.employee_table.xview)
        scroll_Y.config(command=self.employee_table.yview)
        self.employee_table.heading("#1",text="Id")
        self.employee_table.heading("#2", text="Name")
        self.employee_table.heading("#3", text="Age")
        self.employee_table.heading("#4", text="Gender")
        self.employee_table.heading("#5", text="Phone")
        self.employee_table.heading("#6", text="Date_of_Birth")
        self.employee_table.heading("#7", text="Email")
        self.employee_table.heading("#8", text="Department")
        self.employee_table.heading("#9",text="Date_of_joining")
        self.employee_table.heading("#10", text="Skill")
        self.employee_table.heading("#11", text="Basic Salary")
        self.employee_table.heading("#12", text="Total Salary")
        self.employee_table.heading("#13", text="Address")
        self.employee_table['show']='headings'
        self.employee_table.column("#1",width=100)
        self.employee_table.column("#2",width=100)
        self.employee_table.column("#3",width=100)
        self.employee_table.column("#4",width=100)
        self.employee_table.column("#5",width=100)
        self.employee_table.column("#6",width=100)
        self.employee_table.column("#7",width=100)
        self.employee_table.column("#8",width=100)
        self.employee_table.column("#9",width=100)
        self.employee_table.column("#10",width=100)
        self.employee_table.column("#11",width=100)
        self.employee_table.column("#12",width=100)    
        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_db = database.EmployeeDB()   
    def download_database(self):
        try:
            data = self.employee_db.fetch_data()
            df = pd.DataFrame(data, columns=["ID","Name","Age","Gender","Phone","Date_Of_Birth","Email","Department","Date_of _Joining","Skill","Basic Salary","Total Salary","Address"])
            file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
            if file_path:
                df.to_excel(file_path, index=False)
                messagebox.showinfo("Success", f"Database downloaded as {file_path}!")
        except Exception as e:
            messagebox.showerror("Error", f"Error downloading database: {str(e)}")
    def add_to_treeview(self):
        employee_data = self.employee_db.fetch_data()
        self.employee_table.delete(*self.employee_table.get_children())
        for employee in employee_data:
            self.employee_table.insert('', END, values=employee)
    
    def insert(self):
        id = self.var_id.get()
        name = self.var_name.get()
        age = self.var_age.get()
        gender = self.var_gender.get()
        phone = self.var_phone.get()
        Date_Of_Birth = self.var_Date_Of_Birth.get()
        email = self.var_email.get()
        department = self.var_department.get()
        Date_Of_join = self.var_Date_Of_joining.get()
        skill = self.var_skill.get()
        bs = self.var_bs.get()
        ts = self.var_ts.get()
        address = self.var_address.get()

        if not id or not name or not age or not gender or not phone or not Date_Of_Birth or not email or not department or not Date_Of_join or not skill or not bs or not ts or not address:
            messagebox.showerror("Error", "All fields are required!")
            return
        
        if self.employee_db.check_id_exists(id):
            messagebox.showerror("Error", "ID already exists!")
            return
        if self.employee_db.check_phone_exists(phone):
            messagebox.showerror("Error", "Phone number already exists!")
            return

        # Insert into the database
        try:
            self.employee_db.insert_data(id, name, age, gender, phone, Date_Of_Birth, email, department, Date_Of_join, skill, bs, ts, address)
            messagebox.showinfo("Success", "Record inserted successfully!")
            self.add_to_treeview()  # Refresh the treeview with updated data
            self.clear_fields()  # Clear input fields after insertion
        except Exception as e:
            messagebox.showerror("Error", f"Error inserting record: {str(e)}")

    def update(self):
        selected_item = self.employee_table.focus()  # Get the selected item from the treeview
        values = self.employee_table.item(selected_item, 'values')  # Get values of the selected item
        if not values:
            messagebox.showerror("Error", "Please select a record to update!")
            return

        # Extracting values from the selected item
        id = values[0]
        # Retrieve the new values from the entry fields
        name = self.var_name.get()
        age = self.var_age.get()
        gender = self.var_gender.get()
        phone = self.var_phone.get()
        Date_Of_Birth = self.var_Date_Of_Birth.get()
        email = self.var_email.get()
        department = self.var_department.get()
        Date_Of_join = self.var_Date_Of_joining.get()
        skill = self.var_skill.get()
        bs = self.var_bs.get()
        ts = self.var_ts.get()
        address = self.var_address.get()

        if not id or not name or not age or not gender or not phone or not Date_Of_Birth or not email or not department or not Date_Of_join or not skill or not bs or not ts or not address:
            messagebox.showerror("Error", "All fields are required!")
            return

        # Update the database record
        try:
            self.employee_db.update_data(id, name, age, gender, phone, Date_Of_Birth, email, department, Date_Of_join, skill, bs, ts, address)
            messagebox.showinfo("Success", "Record updated successfully!")
            self.add_to_treeview()  # Refresh the treeview with updated data
            self.clear_fields()  # Clear input fields after update
        except Exception as e:
            messagebox.showerror("Error", f"Error updating record: {str(e)}")
    
    def delete(self):
        selected_item = self.employee_table.focus()  # Get the selected item from the treeview
        values = self.employee_table.item(selected_item, 'values')  # Get values of the selected item
        if not values:
            messagebox.showerror("Error", "Please select a record to delete!")
            return

        id = values[0]  # Extract ID of the selected item

        # Ask for confirmation before deletion
        confirmation = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this record?")
        if confirmation:
            try:
                # Delete the record from the database
                self.employee_db.delete_data(id)
                messagebox.showinfo("Success", "Record deleted successfully!")
                self.add_to_treeview()  # Refresh the treeview with updated data
            except Exception as e:
                messagebox.showerror("Error", f"Error deleting record: {str(e)}")

    def clear_fields(self):
        self.var_id.set("")
        self.var_name.set("")
        self.var_age.set("")
        self.var_gender.set("Select Gender")
        
        self.var_phone.set("")
        self.var_Date_Of_Birth.set("")
        self.var_email.set("")
        self.var_department.set("Select Department")
        self.var_Date_Of_joining.set("")
        self.var_skill.set("Select Skill")
        self.var_bs.set("")
        self.var_ts.set("")
        self.var_address.set("")
    
    def search(self):
        if self.var_search.get() == '' or self.var_search_text.get() == '':
            messagebox.showerror("Error", "Please enter a search term and select an option!")
        else:
            try:
                search_term = self.var_search.get()
                search_text = self.var_search_text.get()
                
                if search_term == "id":
                    # Search by ID
                    data = self.employee_db.search_by_id(search_text)
                elif search_term == "Phone":
                    # Search by phone number
                    data = self.employee_db.search_by_phone(search_text)
                else:
                    messagebox.showerror("Error", "Invalid search option!")
                    return

                self.employee_table.delete(*self.employee_table.get_children())
                
                if not data:
                    messagebox.showinfo("No Data", "No data found for the given search criteria.")
                else:
                    for employee in data:
                        self.employee_table.insert('', END, values=employee)
            except Exception as e:
                messagebox.showerror("Error", f"Error during search: {str(e)}")

    def display(self, event):
        selected_item = self.employee_table.focus()
        if selected_item:
            row = self.employee_table.item(selected_item)["values"]
            self.clear_fields()
            if row:
                self.var_id.set(row[0])
                self.var_name.set(row[1])
                self.var_age.set(row[2])
                self.var_gender.set(row[3])
                self.var_phone.set(row[4])
                self.var_Date_Of_Birth.set(row[5])
                self.var_email.set(row[6])
                self.var_department.set(row[7])
                self.var_Date_Of_joining.set(row[8])
                self.var_skill.set(row[9])
                self.var_bs.set(row[10])
                self.var_ts.set(row[11])
                self.var_address.set(row[12])


    def showall(self):
        self.add_to_treeview()
if __name__=="__main__":
    root=Tk()
    obj=Employee(root)
    obj.add_to_treeview()
    obj.employee_table.bind('<ButtonRelease-1>', obj.display)
    root.mainloop()