from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector


class Time_Schedule:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1280x720+0+0")
        self.root.title("Time Schdeule")

        #Bg Image
        img=Image.open(r"C:\Users\ankit\Desktop\New folder\itersoa.jpg")
        img=img.resize((1280,720),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        BgImage = Label(self.root, image=self.photoimg)
        BgImage.place(x=0,y=0,width=1280,height=720)

        title = Label(BgImage, text="TIME TABLE", font=("Times new roman", 25,"bold"),bg="white")
        title.place(x=0,y=0,width=1280,height=45)   

        main_frame = Frame(BgImage, bd=2, bg="white")
        main_frame.place(x=20,y=50,width=1240, height = 650)

        days = 5
        day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thrusday', 'Friday']
        periods = 6
        period_names = list(map(lambda x: 'Period ' + str(x), range(1, 6+1)))
        butt_grid = []
    

        def select_sec():
            global section
            global branch
            section = str(combo1.get())
            branch = str(combo2.get())
            update_table()
     

        def update_table():
            for i in range(days):
                for j in range(periods):
                    conn = mysql.connector.connect(host='localhost', username='root', password='Chiku@3037', database='attendance-system')
                    cursor = conn.cursor()
                    cursor.execute(f"SELECT SUBCODE, FID FROM SCHEDULE\
                        WHERE DAYID={i+1} AND PERIODID={j+1} AND BRANCH='{branch}' AND SECTION='{section}'")
                    cursor = list(cursor)
                    if len(cursor) != 0:
                        butt_grid[i][j]['text'] = str(cursor[0][0]) + '\n' + str(cursor[0][1])
                        butt_grid[i][j].update()
                        print(i, j, cursor[0][0])
                    else:
                        butt_grid[i][j]['text'] = "No Class"
                        butt_grid[i][j].update()    

        table = Frame(main_frame)
        table.pack()

        first_half = Frame(table)
        first_half.pack(side='left')

        for i in range(days):
            b = Label(first_half, text=day_names[i], font=('Consolas', 12, 'bold'), width=9, height=2, bd=5, relief='raised')
            b.grid(row=i+1, column=0)


        for i in range(periods):
            b = Label(first_half)
            b.grid(row=0, column=i+1)
            b.config(text=period_names[i], font=('Consolas', 12, 'bold'), width=9, height=1, bd=5, relief='raised')    

        for i in range(days):
            b = []
            for j in range(periods):

                bb = Button(first_half)
                bb.grid(row=i+1, column=j+1)
                bb.config(text='Hello World!', font=('Consolas', 10), width=13, height=3, bd=5, relief='raised', wraplength=80,
                    justify='center', command=lambda x=i, y=j: process_button(x, y))
                b.append(bb)

            butt_grid.append(b)
            b = []

        #Select Branch
        sec_select_f = Frame(main_frame, pady=15)
        sec_select_f.pack()

        Label(sec_select_f, text='Select Branch and Section:  ',font=('Consolas', 12, 'bold')).pack(side=LEFT)    
        
        conn = mysql.connector.connect(host='localhost', username='root', password='Chiku@3037', database='attendance-system')
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT BRANCH FROM SCHEDULE")
        br_li = [row[0] for row in cursor]  

        combo2 = ttk.Combobox(sec_select_f, values=br_li,)
        combo2.pack(side=LEFT)
        combo2.current(0)

        cursor.execute("SELECT DISTINCT SECTION FROM SCHEDULE")
        sec_li = [row[0] for row in cursor]
        
        combo1 = ttk.Combobox(sec_select_f, values=sec_li,)
        combo1.pack(side=LEFT, padx=10)
        combo1.current(0)

        b = Button(sec_select_f, text="OK",font=('Consolas', 12, 'bold'), padx=10, command=select_sec)
        b.pack(side=LEFT, padx=10)
        b.invoke()


        def process_button(d, p):
            add_p = Tk()

            # get subject code list from the database
            conn = mysql.connector.connect(host='localhost', username='root', password='Chiku@3037', database='attendance-system')
            cursor = conn.cursor()
            cursor.execute("SELECT SUBCODE FROM SUBJECTS")
            subcode_li = [row[0] for row in cursor]
            subcode_li.insert(0, 'NULL')

            # Label10
            Label(add_p,text='Select Subject',font=('Consolas', 12, 'bold')).pack()

            Label(add_p,text=f'Day: {day_names[d]}',font=('Consolas', 12)).pack()
            Label(add_p,text=f'Period: {p+1}',font=('Consolas', 12)).pack()

            tree = ttk.Treeview(add_p)
            tree['columns'] = ('one', 'two')
            tree.column("#0", width=0, stretch=NO)
            tree.column("one", width=70, stretch=NO)
            tree.column("two", width=80, stretch=NO)
            tree.heading('#0', text="")
            tree.heading('one', text="Faculty")
            tree.heading('two', text="Subject Code")

            conn = mysql.connector.connect(host='localhost', username='root', password='Chiku@3037', database='attendance-system')
            cursor = conn.cursor()
            cursor.execute("SELECT FACULTY.ID, FACULTY.SUBCODE_1, FACULTY.SUBCODE_2, SUBJECTS.SUBCODE\
            FROM FACULTY, SUBJECTS\
            WHERE FACULTY.SUBCODE_1=SUBJECTS.SUBCODE OR FACULTY.SUBCODE_2=SUBJECTS.SUBCODE")
            for row in cursor:
                
                tree.insert(
                    "",
                    0,
                    values=(row[0],row[-1])
                )
            tree.insert("", 0, value=('NULL', 'NULL'))
            tree.pack(pady=10, padx=30)

            Button(add_p, text="OK",padx=15,command=lambda x=d, y=p, z=tree, d=add_p: update_p(x, y, z, d)).pack(pady=20)

            add_p.mainloop()

        def update_p(d, p, tree, parent):
            conn = mysql.connector.connect(host='localhost', username='root', password='Chiku@3037', database='attendance-system')
            cursor = conn.cursor()
            try:
                if len(tree.selection()) > 1:
                    messagebox.showerror("Bad Select", "Select one subject at a time!")
                    parent.destroy()
                    return
                row = tree.item(tree.selection()[0])['values']
                if row[0] == 'NULL' and row[1] == 'NULL':
                    
                    cursor.execute(f"DELETE FROM SCHEDULE WHERE ID='{section+str((d+1)*10+(p+1))}'")
                    conn.commit()
                    update_table()
                    parent.destroy()
                    return

                conn.commit()
                cursor.execute(f"REPLACE INTO SCHEDULE (ID, DAYID, PERIODID, SUBCODE, BRANCH, SECTION, FID)\
                    VALUES ('{section+str((d+1)*10+(p+1))}', {d+1}, {p+1}, '{row[1]}', '{branch} ' , '{section}', '{row[0]}')")
                conn.commit()
                update_table()

            except IndexError:
                messagebox.showerror("Bad Select", "Please select a subject from the list!")
                parent.destroy()
                return

            parent.destroy()    

if __name__ == "__main__":
    root=Tk()  
    obj=Time_Schedule(root)
    root.mainloop()        