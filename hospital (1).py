import mysql.connector
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import simpledialog
from PIL import ImageTk, Image
import sqlite3

starting_window = Tk()
width= starting_window.winfo_screenwidth()
height= starting_window.winfo_screenheight()
starting_window.geometry('%dx%d' %(width, height) )
starting_window.title('Hospital')
photo = PhotoImage(file = "icon.png")
starting_window.iconphoto(False,photo)
img = ImageTk.PhotoImage(Image.open("starting_sc.jpg"))
imglabel = Label(starting_window, image=img, width = 1920, height =1080)
imglabel.image = img
imglabel.place(x=0, y = 0)
t1 = Label(starting_window, text = 'Welcome to Abc Hospital', font = ('Times',30,'bold')).place(x = 480, y = 15)
con = sqlite3.connect('hospital1.db')
cur = con.cursor()



class main:
    def __init__(self):
        self.a = Tk()
        
    #def main_screen():
        
        #a = Tk()
        self.a.title("Hospital Managment")
        width= self.a.winfo_screenwidth()
        height= self.a.winfo_screenheight()
        self.a.geometry("%dx%d" % (width, height))
        photo = PhotoImage(file = "icon.png")
        self.a.iconphoto(False, photo)
        self.a.resizable(True, True)
        self.a.configure(bg="skyblue")
        img = ImageTk.PhotoImage(Image.open("starting_sc.jpg"))
        imglabel = Label(self.a, image=img, width = 1920, height =1080)
        imglabel.image = img
        imglabel.place(x=100, y = 100)
        
        Label(self.a, text="Welcome in ABC Hospital ",justify = LEFT, padx = 20,width = 50, height = 10, bg= 'skyblue', fg='blue').place(x=800, y = 100)
        btn1 = Button(self.a, text='Doctor!', width=40,height=5, bd='10', bg='blue',fg='white', command=self.doc_tab)
        btn2 = Button(self.a, text='Patient!', width=40,height=5, bd='10',bg='blue',fg='white', command = self.calling_appointment)
        btn3 = Button(self.a, text='Admin!', width=40,height=5, bd='10',bg='blue',fg='white', command=self.start_admin)
        btn1.place(x = 200, y= 500)
        btn2.place(x = 600, y= 500)
        btn3.place(x = 1000, y= 500)

        MenuBar1 = Menu(self.a)
        SubMenu1 = Menu(MenuBar1, tearoff = 0)
        MenuBar1.add_cascade(label = 'Help', menu = SubMenu1)
        SubMenu1.add_command(label = 'About', command = self.about)

        self.a.config(menu = MenuBar1)

    def about(self):
        messagebox.showinfo("About","This is a Hospital appointment booking software")

    def calling_appointment(self):
        h = appointment()

    def doc_tab(self):
        doc = Frame(self.a)
        doc.configure(bg="skyblue")
        doc.pack(side="top", expand=True, fill="both")
        Label(doc, text = 'Doctor Pannel',bg = 'blue', width =1000).place(x=0,y=0)
        '''
        img = ImageTk.PhotoImage(Image.open("image1.jpg"))
        imglabel = Label(doc, image=img, width = 300, height =300)
        imglabel.image = img
        imglabel.place(x=100, y = 100)
        '''

        Label(doc,text= "", justify = LEFT, padx = 20,width = 50, height = 10, bg= 'skyblue', fg='blue').place(x=700, y = 20)

        Label(doc, text = "select Doctor ID to show Schedule of the Doctor  ", 
              background = 'blue', foreground ="white", 
              font = ("Times New Roman", 15)).place(x=600, y=100)
        n = StringVar()
        d = ttk.Combobox(doc, width = 27, textvariable = n)
        d['values'] = ('D001', 
                              'D002',
                              'D003',
                       'D004')
        d.place(x = 700, y=200)
        
        def disp_doc(event):
            global dd
            dd = Tk()
            dd.title("Doctor Details")
            width= dd.winfo_screenwidth()/2
            height= dd.winfo_screenheight()/2
            dd.geometry("%dx%d" % (width, height))

            MenuBar1 = Menu(a)
            SubMenu1 = Menu(MenuBar1, tearoff = 0)
            MenuBar1.add_cascade(label = 'Help', menu = SubMenu1)
            SubMenu1.add_command(label = 'About', command = self.about)

            a.config(menu = MenuBar1)
            for row in cur.execute('SELECT * FROM doctor1 where Doc_id=?',(d.get(),)):
                     #print(row)
                     l = Label(dd, text="  Docter Name:     "+ row[1],justify = LEFT, padx = 20, bg= 'skyblue', fg='blue')
                     l.place(x=50, y = 100)
                     l2 = Label(dd, text="  Docter ID:        "+row[0],justify = LEFT, padx = 20, bg= 'skyblue', fg='blue')
                     l2.place(x=400, y = 100)
                     l6 = Label(dd, text="  Specialization:   "+row[2],justify = LEFT, padx = 20, bg= 'skyblue', fg='blue')
                     l6.place(x=50, y = 200)
                     
                     l3 = Label(dd, text="  Docter Days:      "+row[4],justify = LEFT, padx = 20,  bg= 'skyblue', fg='blue')
                     l3.place(x=50, y = 300)
                     l4 = Label(dd, text="  Docter Time:      "+row[5],justify = LEFT, padx = 20, bg= 'skyblue', fg='blue')
                     l4.place(x=400, y = 300)
                     l5 = Label(dd, text="  Fee per Visit:    "+str(row[3]),justify = LEFT, padx = 20, bg= 'skyblue', fg='blue')
                     l5.place(x=400, y = 200)
            #print(d.get()," " , type(x))
            #rec(x)
       
        d.bind('<<ComboboxSelected>>',disp_doc)
        d.current()
        

        btnBack = Button(doc, text='show all doctors details!', width=20,height=2,bg='skyblue',fg='white', command=self.Disp_doc)
        btnBack.place(x=1000,y=200)
        def main_screen():
            doc.destroy()
            
        btnBack = Button(doc, text='Main Page!', width=20,height=2,bg='skyblue',fg='white', command=main_screen)
        btnBack.place(x=1000,y=700)
    def Disp_doc(self):
        global dd
        dd = Tk();
        dd.title("Docters Detail")
        width= dd.winfo_screenwidth()/2+300
        height= dd.winfo_screenheight()/2
        dd.geometry("%dx%d" % (width, height))
        la=Label(dd,text='              Doctors Detail                ',borderwidth=2,relief='ridge',anchor='w',bg='skyblue')
        la.grid(row=0,column=4)
        l=Label(dd,width=25,text='  Docter ID    ',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        l.grid(row=3,column=2)
        l2=Label(dd,width=25,text='  Docter Name    ',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        l2.grid(row=3,column=3)
        l3=Label(dd,width=25,text='  Specialization:    ',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        l3.grid(row=3,column=4)
        l4=Label(dd,width=25,text='  Fee per Visit    ',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        l4.grid(row=3,column=5)
        l5=Label(dd,width=25,text='  Docter Days:    ',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        l5.grid(row=3,column=6)
        l6=Label(dd,width=25,text='  Docter Time:    ',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        l6.grid(row=3,column=7)
        i=4 
        for doc in cur.execute('SELECT * FROM doctor1'):
                 #print(doc)
                 k=2
                 for j in range(len(doc)):
                         e = Label(dd,width=25, text=doc[j], bd =3, fg='blue', borderwidth=2, relief='ridge', anchor="w")
                         e.grid(row=i, column=k)
                         k=k+1
                 i=i+1
    def Disp_doc_details(self,d):
            global dd
            dd = Tk()
            #Frame(self.a,width=500,height=500,bg='silver').place(x=300,y=300);
            dd.title("Docter Details")
            width= dd.winfo_screenwidth()/2
            height= dd.winfo_screenheight()/2
            dd.geometry("%dx%d" % (width, height))
            for row in cur.execute('SELECT * FROM doctor1 where Doc_id=?',(d,)):
                     #print(row)
                     l = Label(dd, text="  Docter Name:     "+ row[1],justify = LEFT, padx = 20, bg= 'skyblue', fg='blue')
                     l.place(x=50, y = 100)
                     l2 = Label(dd, text="  Docter ID:        "+row[0],justify = LEFT, padx = 20, bg= 'skyblue', fg='blue')
                     l2.place(x=400, y = 100)
                     l6 = Label(dd, text="  Specialization:   "+row[2],justify = LEFT, padx = 20, bg= 'skyblue', fg='blue')
                     l6.place(x=50, y = 200)
                     
                     l3 = Label(dd, text="  Docter Days:      "+row[4],justify = LEFT, padx = 20,  bg= 'skyblue', fg='blue')
                     l3.place(x=50, y = 300)
                     l4 = Label(dd, text="  Docter Time:      "+row[5],justify = LEFT, padx = 20, bg= 'skyblue', fg='blue')
                     l4.place(x=400, y = 300)
                     l5 = Label(dd, text="  Fee per Visit:    "+str(row[3]),justify = LEFT, padx = 20, bg= 'skyblue', fg='blue')
                     l5.place(x=400, y = 200)
    def start_admin(self):
                    log = login()

class login:
    def __init__(self):
        self.b = Tk()
        self.b.title("Login Details")
        width= self.b.winfo_screenwidth()/2
        height= self.b.winfo_screenheight()/2
        self.b.geometry("%dx%d" % (width, height))
        '''photo = PhotoImage(file = "bird.png")
        self.a.iconphoto(False, photo)
        self.a.resizable(True, True)
        self.a.configure(bg="skyblue")
        img = ImageTk.PhotoImage(Image.open("D:\Python\hospital_managmet\image1.jpg"))
        imglabel = Label(self.a, image=img, width = 300, height =300)
        imglabel.image = img
        imglabel.place(x=100, y = 100)
        '''
        Label(self.b, text="Login Page for Admin ",justify = LEFT, padx = 20,width = 70, height = 2, bg= 'skyblue', fg='blue').place(x=50, y = 5)
        l1 = Label(self.b, text='Enter User Id', width=20,height=2, bd='10', bg='blue',fg='white')
        l2 = Label(self.b, text='Enter Password', width=20,height=2, bd='10', bg='blue',fg='white')
        self.e1 = Entry(self.b)
        self.e2 = Entry(self.b)
        l1.place(x = 100, y= 100)
        l2.place(x = 100, y= 250)
        self.e1.place(x = 300, y= 120)
        self.e2.place(x = 300, y= 280)
        btn1 = Button(self.b, text='Login..', width=20,height=2,bg='skyblue',fg='white',command=self.login)
        btn1.place(x = 250, y= 350)

    def login(self):
        if self.e1.get() =="admin" and self.e2.get()=="admin123":
             messagebox.showinfo("About","Login.....")
             self.b.destroy()
             t = admin_jobs()
        else:
             messagebox.showinfo("About","Sorry please enter correct user id and password")

class admin_jobs: 
    def __init__(self):
        self.b = Tk()
        self.b.title("Administrative Works")
        width= self.b.winfo_screenwidth()
        height= self.b.winfo_screenheight()
        self.b.geometry("%dx%d" % (width, height))
        t1 = Label(self.b,  text = 'Administrative Works -', font = ('Times',20,'bold')).place( x = 20, y = 30)
        btn1 = Button(self.b, text = 'Update Doctor', font = ('',15,''),width=30,height=5, bd='10', bg='blue',fg='white', command = self.update_doctor).place (x = 100, y = 300)
        btn2 = Button(self.b, text = 'Add Doctor', font = ('',15,''),width=30,height=5, bd='10', bg='blue',fg='white', command = self.add_doctor).place (x = 500, y = 300)
        btn3 = Button(self.b, text = 'Delete Doctor', font = ('',15,''),width=30,height=5, bd='10', bg='blue',fg='white', command = self.delete_doctor).place (x = 900, y = 300)

    def update_doctor(self):
        global Window5
        Window5 = Tk()
        Window5.title("Login Details")
        width= Window5.winfo_screenwidth()/2
        height= Window5.winfo_screenheight()/2
        Window5.geometry("%dx%d" % (width, height))
        btn1 = Button(Window5, text = 'Update Doctor Department', font = ('',13,''), bg='blue',fg='white', command = self. update_dept).place(x = 230, y = 60)
        btn2 = Button(Window5, text = 'Update Doctor Fee', font = ('',13,''), bg='blue',fg='white', command = self.update_fee).place(x = 230, y = 130)
        btn3 = Button(Window5, text = 'Update Doctor Days', font = ('',13,''), bg='blue',fg='white', command = self.update_day).place(x = 230, y = 190)
        btn4 = Button(Window5, text = 'Update Doctor Time', font = ('',13,''), bg='blue',fg='white', command = self.update_time).place(x = 230, y = 260)
        global doc_id2
        doc_id2 = simpledialog.askstring("Update Doctor", "Enter Doctor ID to continue -",
                                parent=Window5)
        
    def update_dept(self):
        new_val = simpledialog.askstring("Update Doctor", "Enter Doctor Dept to continue -",
                                parent=Window5)
        rec = (new_val,doc_id2)
        sql = "Update doctor1 set dept = ? where Doc_id = ?"
        try:    #exception error
            cur.execute(sql,rec)
            con.commit()
            messagebox.showinfo("Update Department", "Department Updated!")
        except:
            con.rollback()
            messagebox.showinfo("Update Department", "Department not Updated!!")

    def update_fee(self):
        new_val = simpledialog.askstring("Update Doctor", "Enter Doctor fee to continue -",
                                parent=Window5)
        rec = (new_val,doc_id2)
        sql = "Update doctor1 set fee = ? where Doc_id = ?"
        try:    #exception error
            cur.execute(sql, rec)
            con.commit()
            messagebox.showinfo("Update Fee", "Fee Updated!")
        except:
            con.rollback()
            messagebox.showinfo("Update Fee", "Fee not Updated!!")

    def update_day(self):
        new_val = simpledialog.askstring("Update Doctor", "Enter Doctor Days to continue -",
                                parent=Window5)
        rec = (new_val,doc_id2)
        sql = "Update doctor1 set days = ? where Doc_id = ?"
        try:    #exception error
            cur.execute(sql, rec)
            con.commit()
            messagebox.showinfo("Update Days", "Day Updated!")
        except:
            con.rollback()
            messagebox.showinfo("Update Days", "Day not Updated!!")

    def update_time(self):
        new_val = simpledialog.askstring("Update Doctor", "Enter Doctor Time to continue -",
                                parent=Window5)
        rec = (new_val,doc_id2)
        sql = "Update doctor1 set time = ? where Doc_id = ?"
        try:    #exception error
            cur.execute(sql, rec)
            con.commit()
            messagebox.showinfo("Update Time", "Time Updated!")
        except:
            con.rollback()
            messagebox.showinfo("Update Time", "Time not Updated!!")

    def add_doctor(self):
        global Window10
        Window10 = Tk()
        Window10.title("Add Doctor")
        width= Window10.winfo_screenwidth()/2
        height= Window10.winfo_screenheight()/2
        Window10.geometry("%dx%d" % (width, height))
        t1 = Label(Window10, text = 'Add Doctor -', font = ('',20,'')).place( x =10, y = 5)
        t2 = Label(Window10, text = 'Enter Doctor ID - ', font = ('',13,'')).place( x = 20, y = 75)
        t3 = Label(Window10, text = 'Enter Doctor Name - ', font = ('',13,'')).place( x = 20, y = 115)
        t4 = Label(Window10, text = 'Enter Doctor Department - ', font = ('',13,'')).place( x = 20, y = 155)
        t5 = Label(Window10, text = 'Enter Doctor Fee - ', font = ('',13,'')).place( x = 20, y = 195)
        t6 = Label(Window10, text = 'Enter Doctor Days - ', font = ('',13,'')).place( x = 20, y = 235)
        t7 = Label(Window10, text = 'Enter Doctor Time - ', font = ('',13,'')).place( x = 20, y = 275)

        global e1, e2, e3, e4, e5, e6
        e1 = Entry(Window10) 
        e2 = Entry(Window10)
        e3 = Entry(Window10)
        e4 = Entry(Window10)
        e5 = Entry(Window10)
        e6 = Entry(Window10)

        e1.place(x = 170, y =75)
        e2.place(x = 190, y =115)
        e3.place(x = 220, y =155)
        e4.place(x = 180, y =195)
        e5.place(x = 180, y =235)
        e6.place(x = 180, y =275)

        b1 = Button(Window10, text = 'Add Doctor', font = ('Times',13,''), command = self.adding_doctor).place(x = 10, y = 300)

    def adding_doctor(self):
        doc_id = e1.get()
        doc_name = e2.get()
        doc_dept = e3.get()
        doc_fee = e4.get()
        doc_day = e5.get()
        doc_time = e6.get()
        rec = (doc_id,doc_name,doc_dept,doc_fee,doc_day,doc_time)
        print(rec)
        sql = "INSERT INTO doctor1 VALUES (?,?,?,?,?,?)"
        try:    #exception error
            cur.execute(sql, rec)
            con.commit()
            messagebox.showinfo("Add Doctor", "Doctor Added!")
            Window10.destroy()
        except:
            con.rollback()
            messagebox.showinfo("Add Doctor", "Doctor not Added!!")
            Window10.destroy()
            
    def delete_doctor(self):
        global doc_del
        doc_del = simpledialog.askstring("Delete Doctor", "Enter Doctor ID to delete -",
                                parent=self.b)
        self.deletin_doc()

    def deletin_doc(self):
        sql = "delete from doctor1 where Doc_id = ?" 
        rec =(doc_del,)
        try:    #exception error
            cur.execute(sql,rec)
            con.commit()
            messagebox.showinfo("Delete Doctor", "Doctor Deleted!")
        except sqlite3.Error as e:
            con.rollback()
            messagebox.showinfo("Delete Doctor", "Doctor not Deleted!!", e)        
        
class appointment:
    def __init__(self):
        self.obj = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'fellowes', database = 'hospital')
        self.cur = self.obj.cursor()
        a = Tk()
        width= a.winfo_screenwidth()
        height= a.winfo_screenheight()
        a.geometry('%dx%d' %(width, height) )
        '''
        photo = PhotoImage(file = "icon.png")
        a.iconphoto(False,photo)
        '''
        a.title('Hospital')
        '''
        img = ImageTk.PhotoImage(Image.open("home_screen1.jpg"))
        imglabel = Label(a, image=img, width = 1920, height =1080)
        imglabel.image = img
        imglabel.place(x=0, y = 0)
        '''
        t1 = Label(a, text = 'Appointment -', font = ('Times', 25,'')).place(x = 570, y = 20)
        b1 = Button(a, text = 'Show doctors', font = ('Times', 15,''), command = self.show_doctors).place(x = 200, y = 300)
        b2 = Button(a, text = 'Book Appointment', font = ('Times', 15,''), command = self.booking_appointment).place(x = 460, y = 300)
        b3 = Button(a, text = 'Update Apointment', font = ('Times', 15,''), command = self.update_apointment).place(x = 770, y = 300)
        b4 = Button(a, text = 'History', font = ('Times', 15, ''), command = self.history).place(x = 1070, y = 300)
        b5 = Button(a, text = 'Back', font = ('Times', 15,''), command = lambda: a.destroy()).place(x = 660, y = 500)

        MenuBar1 = Menu(a)
        SubMenu1 = Menu(MenuBar1, tearoff = 0)
        MenuBar1.add_cascade(label = 'Help', menu = SubMenu1)
        SubMenu1.add_command(label = 'About', command = self.about)

        a.config(menu = MenuBar1)

    def booking_appointment(self):
        global Window
        Window = Tk()
        Window.geometry('600x400')
        '''
        photo = PhotoImage(file = "icon.png")
        Window.iconphoto(False,photo)
        '''
        Window.title('Booking Appointment')
        title1 = Label(Window, text = 'Book Appointment -', font = ('Times', 20,'')).place(x = 20, y = 20)

        global hjk
        hjk = StringVar()
        r1 = Radiobutton(Window, text = '1st Time', font = ('',15,''), value ='1stTime', variable = hjk)
        r2 = Radiobutton(Window, text = 'Follow -UP', font = ('',15,''), value ='Follow-UP', variable = hjk)
        r1.place(x = 20, y =80)
        r2.place(x = 160, y =80)
        b1 = Button(Window, text = 'Next', font = ('',13,''), command = self.radio_button).place(x = 330, y = 84)

    def radio_button(self):
#line 410        r = str(hjk.get())
        print(r)
        if r == '1stTime':
            self.st_time()
        if r == 'Follow-UP':
            self.appointment_continu()
        else:
            print('novalue')

    def st_time(self):
        global window2
        window2 = Tk()
        window2.geometry('600x400')
        '''
        photo = PhotoImage(file = "icon.png")
        window2.iconphoto(False,photo)
        '''
        window2.title('1st Time')
        t1 = Label(window2, text = '1st time -', font = ('Times',20,'')).place(x = 20, y = 20)
        t2 = Label(window2, text = 'Enter Name :-', font = ('', 15,'')).place(x = 25, y = 90)
        t3 = Label(window2, text = 'Select Blood Group :-', font = ('', 15,'')).place(x = 25, y = 135)
        t4 = Label(window2, text = 'Any Allergies :-', font = ('', 15,'')).place(x = 25, y = 180)
        t5 = Label(window2, text = "Previous Doctor's name :-", font = ('', 15,'')).place(x = 25, y = 225)
        global name, allergie, dc
        name = Entry(window2)
        name.place(x = 170, y = 100)
        def get_value(event):
            global bg
            bg =  d.get()
            
        qyz = StringVar()
        d = ttk.Combobox(window2, width = 20, textvariable = qyz)
        d['value'] = ('---none---', 'A+','B+','O+','AB+','A-','B-','O-','AB-')   
        d.place(x = 240, y = 140)
        d.current(0)
        d.bind("<<ComboboxSelected>>",get_value)

        allergie = Entry(window2, width = 50)
        allergie.place(x = 170, y = 185)
        dc = Entry(window2)
        dc.place(x = 270, y = 230)
        b1 = Button(window2, text = 'Submit', font = ('',13,''), command = self.save_history).place(x = 190, y = 300)
        b2 = Button(window2, text = 'Cancel', font = ('',13,''), command = lambda: window2.destroy()).place(x = 350, y = 300)


    def save_history(self):
        n1 = name.get()
        a1 = allergie.get()
        d1 = dc.get()
        sql = "INSERT INTO patient_history VALUES (%s,%s,%s,%s)"
        rec = (n1,bg,a1,d1)
        try:    #exception error
            self.cur.execute(sql,rec)
            self.obj.commit()
            messagebox.showinfo("1st- Time", "History Saved!")
            self.close()
            self.appointment_continu()
            
        except:
            self.obj.rollback()
            messagebox.showinfo("1st- Time", "History not Saved!")
            self.close()
            
    def close(self):
        window2.destroy()

    def appointment_continu(self):
        t1 = Label(Window, text = '        ', font = ('', 18,'')).place(x = 330, y = 84)
        t2 = Label(Window, text = 'Enter Name :-', font = ('', 15,'')).place(x = 25, y = 120)
        t3 = Label(Window, text = 'Enter Age :-', font = ('', 15,'')).place(x = 25, y = 165)
        t4 = Label(Window, text = 'Choose Doctor :-', font = ('', 15,'')).place(x = 25, y = 210)
        t5 = Label(Window, text = 'Choose Timing :-', font = ('', 15,'')).place(x = 25, y = 255)
        t6 = Label(Window, text = 'Choose Day :-', font = ('', 15,'')).place(x = 25, y = 295)

        global Name, Age
        Name = Entry(Window)
        Age = Entry(Window)
        Name.place(x = 190, y = 125)
        Age.place(x = 190, y = 170)
        def get_value(event):
            global doctor, day1, time1
            doctor =  d.get()
            time1 = t.get()
            day1 = day.get()

        cba = StringVar()
        xyz = StringVar()
        qyz = StringVar()
        d = ttk.Combobox(Window, width = 20, textvariable = cba)
        sql = 'select name from doctors'
        self.cur.execute(sql)
        v = self.cur.fetchall()
        d['value'] = ('---none---', v[0], v[1], v[2], v[3], v[4], v[5])   
        d.place(x = 190, y = 215)
        d.current(0)
        d.bind("<<ComboboxSelected>>",get_value)
        

        t = ttk.Combobox(Window, width = 20, textvariable = xyz)
        t['value'] = ('---none---','6am-7am','7am-8am','8am-9am','9am-10am','10am-11am','11am-12am' ,'12am-1pm','2pm-3pm','4pm-5pm','6pm-7pm','8pm-9pm','9pm-10pm')
        t.place(x = 190, y = 260)
        t.current(0)
        t.bind("<<ComboboxSelected>>",get_value)
        
        day = ttk.Combobox(Window, width = 20, textvariable = qyz)
        day['value'] = ('---none---', 'Sunday', 'Monday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
        day.place(x = 190, y = 300)
        day.current(0)
        day.bind("<<ComboboxSelected>>",get_value)

        b1 = Button(Window, text = 'Book Now', font = ('Times',13,'bold'), command = self.save_appointment).place ( x = 150, y = 350)
        b2 = Button(Window, text = 'Cancel', font = ('Times',13,'bold'), command = self.cancel).place ( x = 350, y = 350)
        
    def show_doctors(self):
        Window3 = Tk()
        Window3.geometry("585x200")
        Window3.title('Show Doctors')
        '''
        photo = PhotoImage(file = "icon.png")
        Window3.iconphoto(False,photo)
        '''
        l1 = Label(Window3, text = 'Name', width = 20, borderwidth = 2, relief = 'ridge').grid(row = 0, column = 0)
        l1 = Label(Window3, text = 'Specality', width = 20, borderwidth = 2, relief = 'ridge').grid(row = 0, column = 1)
        l1 = Label(Window3, text = 'Timings', width = 20, borderwidth = 2, relief = 'ridge').grid(row = 0, column = 2)
        l1 = Label(Window3, text = 'Doctor ID', width = 20, borderwidth = 2, relief = 'ridge').grid(row = 0, column = 3)

        sql1 = 'select * from doctors'
        count = 1

        try:
            self.cur.execute(sql1)
            for v1 in self.cur:
                for v2 in range(len(v1)):
                    b = Label(Window3, text = v1[v2], width = 20, borderwidth = 2, relief = 'ridge')
                    b.grid( row = count, column = v2)
                count = count + 1
        except:
            messagebox.showinfo('veiw item', 'Table not printed')
        b1 = Button(Window3, text = 'Cancel', font = ('Times',10,'bold'), command = lambda: Window3.destroy()).place ( x = 270, y = 170)

    def update_apointment(self):
        global Window1
        Window1 = Tk()
        Window1.geometry('450x400')
        Window1.title('Update Apointment')
        '''
        photo = PhotoImage(file = "icon.png")
        Window1.iconphoto(False,photo)
        '''
        title1 = Label(Window1, text = 'Update Appointment -', font = ('Times', 20,'')).place(x = 20, y = 20)
        
        b1 = Button(Window1, text =  'Update Day', font = ('Times',15,'bold'), command = self.update_day).place ( x = 160, y = 100)
        b2 = Button(Window1, text =  'Update Time', font = ('Times',15,'bold'), command = self.update_time).place ( x = 155, y = 160)
        b3 = Button(Window1, text =  'Update Doctor', font = ('Times',15,'bold'), command = self.update_doctor).place ( x = 150, y = 220)
        b4 = Button(Window1, text = 'Cancel', font = ('Times',13,'bold'), command = self.cancel1).place ( x = 185, y = 330)

    def update_day(self):
        global Window
        self.cancel1()
        Window = Tk()
        Window.geometry('450x400')
        '''
        photo = PhotoImage(file = "icon.png")
        Window.iconphoto(False,photo)
        '''
        Window.title('Update Apointment Day')
        t1 = Label(Window, text = 'Update Day -', font = ('Times', 20,'bold')).place(x = 10, y = 10)
        t2 = Label(Window, text = 'Enter patient name -', font = ('',15,'')).place(x = 20, y = 90)
        t2 = Label(Window, text = 'Select new Day -', font = ('',15,'')).place(x = 20, y = 130)
        global p_id
        p_id = Entry(Window)
        p_id.place(x = 220, y = 95)
        
        def get_value(event):
            global nd1
            nd1 = nd.get()
        qyz = StringVar()    
        nd = ttk.Combobox(Window, width = 20, textvariable = qyz)
        nd['value'] = ('---none---', 'Sunday', 'Monday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
        nd.place(x = 195, y = 135)
        nd.current(0)
        nd.bind("<<ComboboxSelected>>",get_value)

        b1 = Button(Window, text = 'Update', font = ('Times', 15,'bold'), command = self.updatin_day).place(x = 180, y = 250)

    def updatin_day(self):
        id1 = p_id.get()
        sql = "UPDATE patient_details SET day = %s WHERE name = %s"
        rec = (nd1,id1)
        try:    #exception error
            self.cur.execute(sql,rec)
            self.obj.commit()
            messagebox.showinfo("record updated", " record updated succussfully")
            self.cancel()
        except:
            self.obj.rollback()
            messagebox.showinfo("record updated","  record not updated")
            self.cancel()

    def update_time(self):
        global Window
        self.cancel1()
        Window = Tk()
        Window.geometry('450x400')
        '''
        photo = PhotoImage(file = "icon.png")
        Window.iconphoto(False,photo)
        '''
        Window.title('Update Apointment Time')
        t1 = Label(Window, text = 'Update Time -', font = ('Times', 20,'bold')).place(x = 10, y = 10)
        t2 = Label(Window, text = 'Enter patient name -', font = ('',15,'')).place(x = 20, y = 90)
        t2 = Label(Window, text = 'Select new Time -', font = ('',15,'')).place(x = 20, y = 130)
        global p_id2
        p_id2 = Entry(Window)
        p_id2.place(x = 220, y = 95)
        
        def get_value(event):
            global nt1
            nt1 = nd.get()
            
        qyz = StringVar()    
        nd = ttk.Combobox(Window, width = 20, textvariable = qyz)
        nd['value'] = ('---none---','6am-7am','7am-8am','8am-9am','9am-10am','10am-11am','11am-12am' ,'12am-1pm','2pm-3pm','4pm-5pm','6pm-7pm','8pm-9pm','9pm-10pm') 
        nd.place(x = 195, y = 135)
        nd.current(0)
        nd.bind("<<ComboboxSelected>>",get_value)

        b1 = Button(Window, text = 'Update', font = ('Times', 15,'bold'), command = self.updatin_time).place(x = 180, y = 250)

    def updatin_time(self):
        id2 = p_id2.get()
        sql = "UPDATE patient_details SET timings = %s WHERE name = %s"
        rec = (nt1,id2)
        try:    #exception error
            self.cur.execute(sql,rec)
            self.obj.commit()
            messagebox.showinfo("record updated", " record updated succussfully")
            self.cancel()
        except:
            self.obj.rollback()
            messagebox.showinfo("record updated","  record not updated")
            self.cancel()

    def update_doctor(self):
        global Window
        self.cancel1()
        Window = Tk()
        Window.geometry('450x400')
        '''
        photo = PhotoImage(file = "icon.png")
        Window.iconphoto(False,photo)
        '''
        Window.title('Update Apointment Doctor')
        t1 = Label(Window, text = 'Update Time -', font = ('Times', 20,'bold')).place(x = 10, y = 10)
        t2 = Label(Window, text = 'Enter patient name -', font = ('',15,'')).place(x = 20, y = 90)
        t2 = Label(Window, text = 'Select new Time -', font = ('',15,'')).place(x = 20, y = 130)
        global p_id3
        p_id3 = Entry(Window)
        p_id3.place(x = 220, y = 95)
        
        def get_value(event):
            global nd1
            nd1 = nd.get()
        sql = 'select name from doctors'    
        self.cur.execute(sql)
        v = self.cur.fetchall()
            
        qyz = StringVar()    
        nd = ttk.Combobox(Window, width = 20, textvariable = qyz)
        nd['value'] = ('---none---', v[0], v[1], v[2], v[3], v[4], v[5])
        nd.place(x = 195, y = 135)
        nd.current(0)
        nd.bind("<<ComboboxSelected>>",get_value)

        b1 = Button(Window, text = 'Update', font = ('Times', 15,'bold'), command = self.updatin_doctor).place(x = 180, y = 250)

    def updatin_doctor(self):
        id3 = p_id3.get()
        sql = "UPDATE patient_details SET doctor = %s WHERE name = %s"
        rec = (nd1,id3)
        try:    #exception error
            self.cur.execute(sql,rec)
            self.obj.commit()
            messagebox.showinfo("record updated", " record updated succussfully")
            self.cancel()
        except:
            self.obj.rollback()
            messagebox.showinfo("record updated","  record not updated")
            self.cancel()


    def save_appointment(self):
        global n
        n = Name.get()
        age = Age.get()
        sql = "INSERT INTO patient_details VALUES (%s,%s,%s,%s,%s)"
        rec = (n,age,doctor,time1,day1)
        try:    #exception error
            self.cur.execute(sql,rec)
            self.obj.commit()
            messagebox.showinfo("Appointment", " Appointment Saved!")
            self.cancel
            
        except:
            self.obj.rollback()
            messagebox.showinfo("Appointment", " Appointment not Saved!")
            self.cancel

    def about(self):
        messagebox.showinfo("About","This is a Hospital appointment booking software")

    def cancel(self):
        Window.destroy()

    def cancel1(self):
        Window1.destroy()

    def history(self):
        global Window4
        Window4 = Tk()
        Window4.geometry("585x200")
        Window4.title('Patient History')
        '''
        photo = PhotoImage(file = "icon.png")
        Window.iconphoto(False,photo)
        '''
        t1 = Label(Window4, text = 'History', font = ('',20,'')).grid(row = 1, column = 0)
        global p_name
        p_name = simpledialog.askstring("History", "Enter patient name",
                                parent=Window4)
        b1 = Button(Window4, text = 'Next', font = ('',13,''), command = self.printin_history).grid(row = 2, column = 0)

    def printin_history(self):
        l1 = Label(Window4, text = 'Name', width = 20, borderwidth = 2, relief = 'ridge').grid(row = 3, column = 0)
        l1 = Label(Window4, text = 'Blood Group', width = 20, borderwidth = 2, relief = 'ridge').grid(row = 3, column = 1)
        l1 = Label(Window4, text = 'Allergies', width = 20, borderwidth = 2, relief = 'ridge').grid(row = 3, column = 2)
        l1 = Label(Window4, text = 'Doctor', width = 20, borderwidth = 2, relief = 'ridge').grid(row = 3, column = 3)
        print(p_name)
        sql1 = 'select * from patient_history where name = %s' % (p_name)
        count = 4

        try:
            self.cur.execute(sql1)
            for v1 in self.cur:
                for v2 in range(len(v1)):
                    b = Label(Window4, text = v1[v2], width = 20, borderwidth = 2, relief = 'ridge')
                    b.grid( row = count, column = v2)
                count = count + 1
        except:
            messagebox.showinfo('veiw item', 'Table not printed')
        b1 = Button(Window4, text = 'Close', font = ('Times',10,'bold'), command = lambda: Window4.destroy()).place ( x = 270, y = 170)
        
        
def start():
    starting_window.destroy()
    m = main()

starting_window.after(2000,start)
