from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

class Faculty_Registration:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1280x720+0+0")
        self.root.title("Faculty Details")

        self.var_Name=StringVar()
        self.var_Id=StringVar()
        self.var_Email=StringVar()
        self.var_subCode1=StringVar()
        self.var_subCode2=StringVar()


        #Bg Image
        bg_img=Image.open(r"C:\Users\ankit\Desktop\New folder\iter.png")
        bg_img=bg_img.resize((1280,720),Image.ANTIALIAS)
        self.photobg_img=ImageTk.PhotoImage(bg_img)

        BgImage = Label(self.root, image=self.photobg_img)
        BgImage.place(x=0,y=0,width=1280,height=720)

        title = Label(BgImage, text="FACULTY DETAILS", font=("Times new roman", 25,"bold"),bg="white")
        title.place(x=0,y=0,width=1280,height=45)

        main_frame = Frame(BgImage, bd=2, bg="white")
        main_frame.place(x=20,y=50,width=1240, height = 650)

        #Details Frame
        det_frame=LabelFrame(main_frame, bd=2, relief=RIDGE, text="Faculty Details", font=("times new roman",14,"bold"), bg="white")
        det_frame.place(x=20, y=30, width=400, height=440)

        #Name
        Name_label=Label(det_frame,text="Name:", font=("times new roman", 14,"bold"),bg="white")
        Name_label.grid(row=0, column=0, padx=10, pady=20,sticky=W)

        Name_Entry=Entry(det_frame, textvariable=self.var_Name,width=23,font=("times new roman",12,"bold"),bg="white")
        Name_Entry.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        #Id
        Id_label=Label(det_frame,text="ID:", font=("times new roman", 14,"bold"),bg="white")
        Id_label.grid(row=1, column=0, padx=10, pady=10,sticky=W)

        Id_Entry=Entry(det_frame, textvariable=self.var_Id,width=23,font=("times new roman",12,"bold"),bg="white")
        Id_Entry.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        #Email
        Email_label=Label(det_frame,text="Email ID:", font=("times new roman", 14,"bold"),bg="white")
        Email_label.grid(row=2,column=0, padx=10, pady=10, sticky=W)

        Email_Entry=Entry(det_frame, textvariable=self.var_Email,width=23,font=("times new roman",12,"bold"),bg="white")
        Email_Entry.grid(row=2, column=1, padx=2, pady=10, sticky=W)

    
        # get subject code list from the database
        conn = mysql.connector.connect(host='localhost', username='root', password='Chiku@3037', database='attendance-system')
        cursor = conn.cursor()
        cursor.execute("select SUBCODE FROM subjects")
        subcode_li = [row[0] for row in cursor]
        subcode_li.insert(0, 'NULL')

        #SubCode1
        SubCode1_label=Label(det_frame,text="SUBCODE 1:", font=("times new roman", 14,"bold"),bg="white")
        SubCode1_label.grid(row=5,column=0, padx=10, pady=15, sticky=W)

        SubCode1_combo=ttk.Combobox(det_frame, values=subcode_li,textvariable=self.var_subCode1,width=20,font=("times new roman",13,"bold"), state="readonly")
        SubCode1_combo.current(0)
        SubCode1_combo.grid(row=5, column=1, padx=2, pady=10, sticky=W)

        #SubCode2
        SubCode2_label=Label(det_frame,text="SUBCODE 2:", font=("times new roman", 14,"bold"),bg="white")
        SubCode2_label.grid(row=6,column=0, padx=10, pady=15, sticky=W)

        SubCode2_combo=ttk.Combobox(det_frame, values=subcode_li,textvariable=self.var_subCode2,width=20,font=("times new roman",13,"bold"), state="readonly")
        SubCode2_combo.current(0)
        SubCode2_combo.grid(row=6, column=1, padx=2, pady=10, sticky=W)

        #Buttons
        Bt_frame=Frame(main_frame,bd=2,relief=RIDGE,bg="white")
        Bt_frame.place(x=20, y=490, width=404,height=35)
        
        save_photo_bt=Button(Bt_frame,text="Save", command=self.add_data ,width=10,font=("times new roman", 12,"bold"),bg="white")
        save_photo_bt.grid(row=0,column=0)

        delete_bt=Button(Bt_frame,text="DELETE", command=self.delete_data,width=10,font=("times new roman", 12,"bold"),bg="white")
        delete_bt.grid(row=0,column=1)

        reset_bt=Button(Bt_frame,text="Reset", command=self.reset_data, width=10,font=("times new roman", 12,"bold"),bg="white")
        reset_bt.grid(row=0,column=2)

        Update_bt=Button(Bt_frame,text="Update",command=self.update_data, width=10,font=("times new roman", 12,"bold"),bg="white")
        Update_bt.grid(row=0,column=3)

        #Details Fetch Frame
        Search_frame=LabelFrame(main_frame, bd=2, relief=RIDGE, text="SEARCH SYSTEM", font=("times new roman",14,"bold"), bg="white")
        Search_frame.place(x=450, y=30, width=750, height=90)

        #Search
        search_label=Label(Search_frame,text="Search by:", font=("times new roman", 14,"bold"), width=10,bg="white")
        search_label.grid(row=0, column=0, padx=2, sticky=W)

        self.var_com_search=StringVar()
        search_combo=ttk.Combobox(Search_frame, textvariable=self.var_com_search, font=("times new roman",14,"bold"), state="readonly", width=10)
        search_combo["values"]=("Select", "Id")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=5, pady=10, sticky=W)

        self.var_search=StringVar()
        roll_Entry=Entry(Search_frame,textvariable=self.var_search,width=20,font=("times new roman",14,"bold"),bg="white")
        roll_Entry.grid(row=0, column=2, padx=5, pady=10, sticky=W)

        search_bt=Button(Search_frame,command=self.search_data,text="Search", width=10,font=("times new roman", 14,"bold"),bg="white")
        search_bt.grid(row=0,column=3, padx=5)
                
        showall_bt=Button(Search_frame,command=self.fetch_data,text="Show all", width=10,font=("times new roman", 14,"bold"),bg="white")
        showall_bt.grid(row=0,column=4, padx=5)

        #Faculty details frame
        table_frame=Frame(main_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=450, y=130, width=750, height=400)

        
        scroll_y=ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.faculty_table=ttk.Treeview(table_frame, column=("name", "id", "email", "subcode1", "subcode2"), yscrollcommand=scroll_y.set)
        
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.faculty_table.yview)

        self.faculty_table.heading("name", text="Name")
        self.faculty_table.heading("id", text="ID")
        self.faculty_table.heading("email", text="Email")
        self.faculty_table.heading("subcode1", text="Subject Code 1")
        self.faculty_table.heading("subcode2", text="Subject Code 2")

        self.faculty_table["show"]="headings"

        self.faculty_table.column("name", width=130)
        self.faculty_table.column("id", width=2)
        self.faculty_table.column("email", width=150)
        self.faculty_table.column("subcode1", width=35)
        self.faculty_table.column("subcode2", width=35)
        

        self.faculty_table.pack(fill=BOTH, expand=1)
        self.faculty_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

        #Add Data
    def add_data(self):
        if self.var_branch.get()=="Select branch" or self.var_Name.get()=="" or self.var_Id.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='Chiku@3037', database='attendance-system')
                my_cursor = conn.cursor()  
                my_cursor.execute("insert into faculty values(%s,%s,%s,%s,%s)", (
                                                            self.var_Name.get(),
                                                            self.var_Id.get(),
                                                            self.var_Email.get(),
                                                            self.var_subCode1.get(),
                                                            self.var_subCode2.get()
                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Details added successfully")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}")   

    def fetch_data(self):
        conn = mysql.connector.connect(host='localhost', username='root', password='Chiku@3037', database='attendance-system')
        my_cursor = conn.cursor()  
        my_cursor.execute("Select * from faculty")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.faculty_table.delete(*self.faculty_table.get_children())
            for i in data:
                self.faculty_table.insert("",END, values=i)                                      
            conn.commit()
        conn.close() 


    def get_cursor(self, event=""):
        cursor_focus=self.faculty_table.focus() 
        content=self.faculty_table.item(cursor_focus)   
        data=content["values"]

        self.var_Name.set(data[0]),
        self.var_Id.set(data[1]),
        self.var_Email.set(data[2]),
        self.var_subCode1.set(data[3]),
        self.var_subCode2.set(data[4])

    #update
    def update_data(self):
        if self.var_branch.get()=="Select branch" or self.var_Name.get()=="" or self.var_Id.get()=="":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                Update=messagebox.askyesno("Update", "Do you want to update the details?")  
                if Update>0:
                    conn = mysql.connector.connect(host='localhost', username='root', password='Chiku@3037', database='attendance-system')
                    my_cursor = conn.cursor() 
                    my_cursor.execute("Update faculty set Name=%s, Email=%s, SUBCODE_1=%s, SUBCODE_2=%s where Id=%s", (
                                                                                                                    self.var_Name.get(),
                                                                                                                    self.var_Email.get(),
                                                                                                                    self.var_subCode1.get(),
                                                                                                                    self.var_subCode2.get(),
                                                                                                                    self.var_Id.get()
                                                                                                                ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success", "Faculty details added successfully", parent=self.root)        
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}")

    #delete
    def delete_data(self):
        if self.var_Roll.get()=="":
            messagebox.showerror("Error", "Roll No is mandatory")
        else:
            try:
                delete=messagebox.askyesno("Delete", "Do you want to delete the details?")   
                if delete>0:
                    conn = mysql.connector.connect(host='localhost', username='root', password='Chiku@3037', database='attendance-system')
                    my_cursor = conn.cursor() 
                    sql="delete from faculty where Id=%s"
                    val=(self.var_Id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Faculty details deleted successfully", parent=self.root)  
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}")    

    #reset
    def reset_data(self):
        self.var_Name.set("")
        self.var_Id.set("")
        self.var_Email.set("")
        self.var_subCode1.set("Select Subject Code")
        self.var_subCode2.set("Select Subject Code")

    #search data
    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Please select option")   
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='Chiku@3037', database='attendance-system')
                my_cursor = conn.cursor() 
                my_cursor.execute("select * from faculty where " +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                rows=my_cursor.fetchall()

                if len(rows)!=0:
                    self.faculty_table.delete(*self.faculty_table.get_children())
                    for i in rows:
                        self.faculty_table.insert("",END,values=i)


                    conn.commit()
                conn.close()        
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}")


if __name__ == "__main__":
    root=Tk()  
    obj=Faculty_Registration(root)
    root.mainloop()          