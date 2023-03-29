from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector


class Time_Schedule:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1110x670+0+0")
        self.root.title("Time Schdeule")

        self.var_Sec=StringVar()
        self.var_branch=StringVar()
        self.var_Id=StringVar()

        title = Label(self.root, text="TIME TABLE", font=("Times new roman", 25,"bold"),bg="white")
        title.place(x=0,y=0,width=1110,height=45)   

        main_frame = Frame(self.root, bd=2, bg="white")
        main_frame.place(x=0,y=45,width=1110, height = 670)

        # get branch and section list from the database
        conn = mysql.connector.connect(host='localhost', username='root', password='Chiku@3037', database='attendance-system')
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT BRANCH, SECTION FROM STUDENT")
        results = cursor.fetchall()
        br_li = list(set([row[0] for row in results]))
        sec_li = list(set([row[1] for row in results]))
        br_li.insert(0, 'Select Branch')
        sec_li.insert(0, 'Select Section')

        label_br_sec=Label(main_frame,text="Select Branch and Section: ", font=("times new roman", 16,"bold"),bg="white")
        label_br_sec.grid(row=3,column=0, padx=10, pady=10, sticky=W)

        branch_combo=ttk.Combobox(main_frame, values=br_li,textvariable=self.var_branch,width=20,font=("times new roman",16,"bold"), state="readonly")
        branch_combo.current(0)
        branch_combo.grid(row=3, column=1, padx=10, pady=10, sticky=W)

        sec_combo=ttk.Combobox(main_frame, values=sec_li,textvariable=self.var_Sec,width=20,font=("times new roman",16,"bold"), state="readonly")
        sec_combo.current(0)
        sec_combo.grid(row=3, column=2, padx=10, pady=10, sticky=W)

        #TimeTable frame
        table = Frame(main_frame, bd=2, bg="white")
        table.place(x=0, y=55, width=1100, height=600)

        tt = Frame(table, bg="white")
        tt.place(x=0, y=5, width=1100, height=600)

        days = 6
        day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        periods = 6
        period_names = list(map(lambda x: 'Period ' + str(x), range(1, 6+1)))

        for i in range(days):
            b = Label(tt, text=day_names[i], font=('Times new roman', 15, 'bold'), width=12, height=3, bd=5, relief=RIDGE, bg="white")
            b.grid(row=i+1, column=0)

        for j in range(periods):
            b = Label(tt, text=period_names[j], font=('Times new roman', 15, 'bold'), width=12, height=2, bd=5, relief=RIDGE, bg="white")
            b.grid(row=0, column=j+1)

        

        def update_data():
            branch=self.var_branch.get()
            section=self.var_Sec.get()  

            b = [[None for j in range(periods)] for i in range(days)]      
            for i in range(days):
                for j in range(periods):
                    conn = mysql.connector.connect(host='localhost', username='root', password='Chiku@3037', database='attendance-system')
                    cursor = conn.cursor()
                    cursor.execute(f"SELECT SUBCODE, FID FROM SCHEDULE\
                        WHERE ID='{branch+'-'+section+'-'+str((i+1)*10+(j+1))}'")
                    cursor = list(cursor)
                    b[i][j] = Button(tt, text='Hello World!', font=('Times new roman', 12), width=12, height=3, bd=5, relief=RIDGE, bg="white",
                        justify=CENTER, command=lambda x=i, y=j: change_subject(x,y))
                    b[i][j].grid(row=i+1, column=j+1)
                    if len(cursor) != 0:
                        b[i][j]['text'] = str(cursor[0][0]) + '\n' + str(cursor[0][1])
                        b[i][j].update()
                    else:
                        b[i][j]['text'] = "No Class"
                        b[i][j].update() 

        #Button    
        OK_bt=Button(main_frame,text="OK",command=update_data, width=10,font=("times new roman", 16,"bold"),bg="white")
        OK_bt.grid(row=3,column=3, padx=10, pady=10)  

        def change_subject(d,p):  
            root=Tk() 
            root.config(bg="white")

            Label(root,text='Select Subject',font=('Times new roman', 12, 'bold'), bg="white").pack()
            Label(root,text=f'Day: {day_names[d]}',font=('Times new roman', 12), bg="white").pack()
            Label(root,text=f'Period: {period_names[p]}',font=('Times new roman', 12), bg="white").pack()

            self.tt=ttk.Treeview(root, column=("faculty", "subcode"))

            self.tt.heading("faculty", text="Faculty")
            self.tt.heading("subcode", text="Subject Code")

            self.tt["show"]="headings"

            self.tt.column("faculty", width=80)
            self.tt.column("subcode", width=100)

            conn = mysql.connector.connect(host='localhost', username='root', password='Chiku@3037', database='attendance-system')
            cursor = conn.cursor()
            cursor.execute("SELECT FACULTY.ID, FACULTY.SUBCODE_1, FACULTY.SUBCODE_2, SUBJECTS.SUBCODE\
            FROM FACULTY, SUBJECTS\
            WHERE FACULTY.SUBCODE_1=SUBJECTS.SUBCODE OR FACULTY.SUBCODE_2=SUBJECTS.SUBCODE")
            result=cursor.fetchall()

            for row in result:
                
                self.tt.insert("", 0, values=(row[0],row[-1]))

            self.tt.insert("", 0, value=('NULL', 'NULL'))
            self.tt.pack(pady=10, padx=30)

            OK_bt = Button(root, text="OK",padx=15,command=lambda x=d, y=p, z=self.tt, d=root: update_subject(x, y, z, d), bg="white").pack(pady=20)

        def update_subject(d,p,tree, parent):
            branch=self.var_branch.get()
            section=self.var_Sec.get()


            conn = mysql.connector.connect(host='localhost', username='root', password='Chiku@3037', database='attendance-system')
            cursor = conn.cursor()
            cursor.execute("Select ID from Schedule")
            result=cursor.fetchall()

            try:
                if len(tree.selection()) > 1:
                    messagebox.showerror("Bad Select", "Select one subject at a time!")
                    parent.destroy()
                    return

                row = tree.item(tree.selection()[0])['values']
                if row[0] == 'NULL' and row[-1] == 'NULL':
                    cursor.execute(f"DELETE FROM SCHEDULE WHERE ID='{branch+'-'+section+'-'+str((d+1)*10+(p+1))}'")
                    conn.commit()
                    update_data()
                    parent.destroy()
                    return   

                cursor.execute(f"REPLACE INTO SCHEDULE (ID, DAYID, PERIODID, SUBCODE, BRANCH, SECTION, FID)\
                    VALUES ('{branch+'-'+section+'-'+str((d+1)*10+(p+1))}', {d+1}, {p+1}, '{row[-1]}', '{branch} ' , '{section}', '{row[0]}')")
                conn.commit()
                update_data()     

            except IndexError:
                messagebox.showerror("Bad Select", "Please select a subject from the list!")
                parent.destroy()
                return        

            parent.destroy()        

if __name__ == "__main__":
    root=Tk()  
    obj=Time_Schedule(root)
    root.mainloop()          