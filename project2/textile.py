from ast import Delete, Return
from cProfile import label
from email.mime import image, message
from multiprocessing import connection
from re import search
from telnetlib import STATUS
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox

from tkinter import messagebox
from turtle import bgcolor, width
from PIL import Image,ImageTk
import mysql.connector






class Employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Employee Management System") 
#variables:
        self.var_dep=StringVar()
        self.var_name=StringVar()
        self.var_designition=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_married=StringVar()
        self.var_dob=StringVar()
        self.var_doj =StringVar()
        self.var_idproofcomb=StringVar()
        self.var_idproof=StringVar()
        self.var_gender=StringVar()
        self.var_phone=StringVar()
        self.var_pms=StringVar()
        self.var_ctc=StringVar()

        lbl_title=Label(self.root,text='STARK INDUSTRIES MANAGEMENT SYSTEM',font=('times new roman',30,'bold'),fg='white',bg='black')
        lbl_title.place(x=0,y=0,width=1530,height=50)
        # logo
        img_logo=Image.open('photo/logo.jpg')
        img_logo=img_logo.resize((50,50),Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=270,y=0,width=50,height=50)

        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='black')
        img_frame.place(x=0,y=50,width=1530,height=160)
#1st
        img1=Image.open('photo/ph1.jpg')
        img1=img1.resize((540,160),Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(img1)

        self.img1=Label(img_frame,image=self.photo1)
        self.img1.place(x=0,y=0,width=540,height=140)
#2nd
        img2=Image.open('photo/logo.jpg')
        img2=img2.resize((540,160),Image.ANTIALIAS)
        self.photo2=ImageTk.PhotoImage(img2)

        self.img2=Label(img_frame,image=self.photo2)
        self.img2.place(x=540,y=0,width=500,height=140)
#3rd
        img3=Image.open('photo/download.jpg')
        img3=img1.resize((540,160),Image.ANTIALIAS)
        self.photo3=ImageTk.PhotoImage(img3)

        self.img3=Label(img_frame,image=self.photo3)
        self.img3.place(x=1000,y=0,width=540,height=140)

        Main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='black')
        Main_frame.place(x=10,y=220,width=1500,height=560)

        upper_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,bg='slategrey',text='Employee_Information',font=('times new roman',11,'bold'),fg='blue')
        upper_frame.place(x=10,y=10,width=1480,height=250)

        # Labels and Entry fields
        lbl_dep=Label(upper_frame,text="Department",font=('arial',10,'bold'),bg='royalblue')
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)

        combo_dep=ttk.Combobox(upper_frame,textvariable=self.var_dep,font=('arial',11,'bold'),width=17,state='readonly')
        combo_dep['value']=('select Department','Admin','HR','Manager','Planing','Sales','Heads Of Department','Marketing','Coders')
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10, sticky=W)
    #name
        lbl_Name=Label(upper_frame,font=("arial",10,"bold"),text="Name:",bg="royalblue")
        lbl_Name.grid(row=0,column=2,sticky=W,padx=2,pady=7)

        txt_name=ttk.Entry(upper_frame,textvariable=self.var_name,width=22,font=("arial",11,"bold"))
        txt_name.grid(row=0,column=3,padx=2,pady=7)

# lbl_Designition
        lbl_Designition=Label(upper_frame,font=("arial",10,"bold"),text="Designition:",bg="royalblue")
        lbl_Designition.grid(row=1,column=0,sticky=W,padx=2,pady=7)

        txt_Designition=ttk.Entry(upper_frame,textvariable=self.var_designition,width=22,font=("arial",11,"bold"))
        txt_Designition.grid(row=1,column=1,padx=2,pady=7)
# Email
        lbl_Email=Label(upper_frame,font=("arial",10,"bold"),text="Email:",bg="royalblue")
        lbl_Email.grid(row=1,column=2,sticky=W,padx=2,pady=7)

        txt_Email=ttk.Entry(upper_frame,textvariable=self.var_email,width=22,font=("arial",11,"bold"))
        txt_Email.grid(row=1,column=3,padx=2,pady=7)
 #address

        lbl_Address=Label(upper_frame,font=("arial",11,"bold"),text="Address:",bg="royalblue")
        lbl_Address.grid(row=2,column=0,sticky=W,padx=2,pady=7)

        txt_Address=ttk.Entry(upper_frame,textvariable=self.var_address,width=22,font=("arial",11,"bold"))
        txt_Address.grid(row=2,column=1,padx=2,pady=7)
#married
        lbl_married =Label(upper_frame,font=("arial",11,"bold"),text="Married status:",bg="royalblue")
        lbl_married.grid(row=2,column=2,sticky=W,padx=2,pady=7)

        com_txt_married=ttk.Combobox(upper_frame,textvariable=self.var_married,state="readonly",font=("arial",11,"bold"),width=18)
        com_txt_married['value']=("Married","Unmarried")
        com_txt_married.current(0)
        com_txt_married.grid(row=2,column=3,sticky=W,padx=2,pady=2)
#dob  
        lbl_dob=Label(upper_frame,font=("arial",11,"bold"),text="DOB:",bg="royalblue")
        lbl_dob.grid(row=3,column=0,sticky=W,padx=2,pady=7)

        txt_dob=ttk.Entry(upper_frame,textvariable=self.var_dob,width=22,font=("arial",11,"bold"))
        txt_dob.grid(row=3,column=1,padx=2,pady=7)
#doj  
        lbl_doj=Label(upper_frame,font=("arial",11,"bold"),text="DOJ:",bg="royalblue")  
        lbl_doj.grid(row=3,column=2,sticky=W,padx=2,pady=7)

        txt_doj=ttk.Entry(upper_frame,textvariable=self.var_doj,width=22,font=("arial",11,"bold"))
        txt_doj.grid(row=3,column=3,padx=2,pady=7)
#Id Proof
        com_txt_proof=ttk.Combobox(upper_frame,textvariable=self.var_idproofcomb,state="readonly",font=("arial",11,"bold"),width=18)
        com_txt_proof['value']=("Select ID Proof","Aadhar Card","PAN Card","Driving License","Voter ID","Passport")
        com_txt_proof.current(0)
        com_txt_proof.grid(row=4,column=0,sticky=W,padx=2,pady=7)

        txt_proof=ttk.Entry(upper_frame,textvariable=self.var_idproof,width=22,font=("arial",11,"bold"))
        txt_proof.grid(row=4,column=1,padx=2,pady=7)
#gender
        lbl_gender=Label(upper_frame,font=("arial",11,"bold"),text="Gender:",bg="royalblue")
        lbl_gender.grid(row=4,column=2,sticky=W,padx=2,pady=7)

        com_txt_gender=ttk.Combobox(upper_frame,textvariable=self.var_gender,state="readonly",font=("arial",11,"bold"),width=18)
        com_txt_gender['value']=("Male","Female","Others")
        com_txt_gender.current(0)
        com_txt_gender.grid(row=4,column=3,sticky=W,padx=2,pady=7)
 # phone
        lbl_Phone=Label(upper_frame,font=("arial",10,"bold"),text="Phone:",bg="royalblue")
        lbl_Phone.grid(row=0,column=4,sticky=W,padx=2,pady=7)

        txt_Phone=ttk.Entry(upper_frame,textvariable=self.var_phone,width=22,font=("arial",11,"bold"))
        txt_Phone.grid(row=0,column=5,padx=2,pady=7)
# PMS
        lbl_PMS=Label(upper_frame,font=("arial",10,"bold"),text="PMS Percentage:",bg="royalblue")
        lbl_PMS.grid(row=2,column=4,sticky=W,padx=2,pady=7)

        txt_PMS=ttk.Entry(upper_frame,textvariable=self.var_pms,width=22,font=("arial",11,"bold"))
        txt_PMS.grid(row=2,column=5,padx=2,pady=7)
# CTC
        lbl_CTC=Label(upper_frame,font=("arial",10,"bold"),text="CTC:",bg="royalblue")
        lbl_CTC.grid(row=1,column=4,sticky=W,padx=2,pady=7)

        txt_CTC=ttk.Entry(upper_frame,textvariable=self.var_ctc,width=22,font=("arial",11,"bold"))
        txt_CTC.grid(row=1,column=5,padx=2,pady=7)
#mask img
        img_mask=Image.open('photo/cph5.png')
        img_mask=img_mask.resize((220,220),Image.ANTIALIAS)
        self.photo4=ImageTk.PhotoImage(img_mask)

        self.img_mask=Label(upper_frame,image=self.photo4)
        self.img_mask.place(x=970,y=0,width=170,height=220)
#Button frame
        Button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='gray')
        Button_frame.place(x=1150,y=0,width=170,height=220)

        btn_add=Button(Button_frame,text="Save",command=self.add_data,font=("arial",15,"bold"),width=12,bg='blue',fg='white')
        btn_add.grid(row=0,column=0,padx=1,pady=5)
        
        btn_Update=Button(Button_frame,text="Update",command=self.update_data,font=("arial",15,"bold"),width=12,bg='blue',fg='white')
        btn_Update.grid(row=1,column=0,padx=1,pady=5)

        btn_Delete=Button(Button_frame,text="Delete",command=self.delete_data,font=("arial",15,"bold"),width=12,bg='blue',fg='white')
        btn_Delete.grid(row=2,column=0,padx=1,pady=5)

        btn_Clear=Button(Button_frame,text="Clear",command=self.reset_data,font=("arial",15,"bold"),width=12,bg='blue',fg='white')
        btn_Clear.grid(row=3,column=0,padx=1,pady=5)

        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,bg='grey',text='Employee_Information Table',font=('times new roman',11,'bold'),fg='blue')
        down_frame.place(x=10,y=250,width=1480,height=270)
#search frame

        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,bg='black',text='Search Employee information',font=('times new roman',11,'bold'),fg='white')
        search_frame.place(x=0,y=0,width=1470,height=50)

        search_by=Label(search_frame,font=("arial",11,"bold"),text="Search By:",fg="black",bg="royalblue")
        search_by.grid(row=0,column=0,sticky=W,padx=5)

        self.var_com_search=StringVar()

        com_txt_search=ttk.Combobox(search_frame,textvariable=self.var_com_search,state="readonly",
                                                        font=("arial",12,"bold"),width=10)
        com_txt_search['value']=("Select option","phone","Id_proof","Name")                                                      
        com_txt_search.current(0) 
        com_txt_search.grid(row=0,column=1,sticky=W,padx=5) 

        self.var_search=StringVar()

        txt_search=ttk.Entry(search_frame,textvariable=self.var_search,width=22,font=("arial",11,"bold"))   
        txt_search.grid(row=0,column=3,padx=5) 

        btn_search=Button(search_frame,text="search",command=self.search_data,font=("arial",8,"bold"),width=10,bg='blue',fg='white')
        btn_search.grid(row=0,column=4,padx=5)

        btn_ShowAll=Button(search_frame,text="ShowAll",command=self.fetch_data,font=("arial",8,"bold"),width=10,bg='blue',fg='white')
        btn_ShowAll.grid(row=0,column=5,padx=5)

        img5=Image.open('photo/stark.jpg')
        img5=img5.resize((500,250),Image.ANTIALIAS)
        self.photo5=ImageTk.PhotoImage(img5)

        self.img2=Label(search_frame,image=self.photo5)
        self.img2.place(x=700,y=0,width=500,height=30)
#table frame
        Table_frame=Frame(down_frame,bd=3,relief=RIDGE,)
        Table_frame.place(x=0,y=60,width=1325,height=140)
#scrool baar
        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL) 
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.employee_table=ttk.Treeview(Table_frame,column=("dep","name","designation","email","address","married","dob","doj","idproofcomb","idproof","gender","phone","pms","ctc",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading('dep',text='Department')
        self.employee_table.heading('name',text='Name')
        self.employee_table.heading('designation',text='Designation')
        self.employee_table.heading('email',text='Email')
        self.employee_table.heading('address',text='Address')
        self.employee_table.heading('married',text='Married Status')
        self.employee_table.heading('dob',text='DOB')
        self.employee_table.heading('doj',text='DOJ')
        self.employee_table.heading('idproofcomb',text='ID Type')
        self.employee_table.heading('idproof',text='ID Proof')
        self.employee_table.heading('gender',text='Gender')
        self.employee_table.heading('phone',text='Phone')
        self.employee_table.heading('pms',text='PMS')
        self.employee_table.heading('ctc',text='CTC')

        self.employee_table['show']='headings'

        self.employee_table.column("dep",width=100)
        self.employee_table.column("name",width=100)
        self.employee_table.column("designation",width=100)
        self.employee_table.column("email",width=100)
        self.employee_table.column("address",width=100)
        self.employee_table.column("married",width=100)
        self.employee_table.column("dob",width=100)
        self.employee_table.column("doj",width=100)
        self.employee_table.column("idproofcomb",width=100)
        self.employee_table.column("idproof",width=100)
        self.employee_table.column("gender",width=100)
        self.employee_table.column("phone",width=100)
        self.employee_table.column("pms",width=100)
        self.employee_table.column("ctc",width=100)

        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
            if self.var_dep.get()=="" or self.var_email.get()=="":
                    messagebox.showerror('Error','All fields are required')
            else:
                try:
                        cconn=mysql.connector.connect(host='localhost',username='root',password="1234",database='mynewdata2')
                        my_cursor=cconn.cursor()
                        my_cursor.execute('insert into employee1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                                                                                        self.var_dep.get(),
                                                                                                                        self.var_name.get(),
                                                                                                                        self.var_designition.get(),
                                                                                                                        self.var_email.get(),
                                                                                                                        self.var_address.get(),
                                                                                                                        self.var_married.get(),
                                                                                                                        self.var_dob.get(),
                                                                                                                        self.var_doj .get(),
                                                                                                                        self.var_idproofcomb.get(),
                                                                                                                        self.var_idproof.get(),
                                                                                                                        self.var_gender.get(),
                                                                                                                        self.var_phone.get(),
                                                                                                                        self.var_pms.get(),
                                                                                                                        self.var_ctc.get()
                                                                                                                ))
                        cconn.commit()
                        self.fetch_data()
                        cconn.close()
                        messagebox.showinfo('Success','Employee has been added!',parent=self.root) 
                except Exception  as es:
                        messagebox.showerror('Error',f'due To:{str(es)}',parent=self.root)  

    def fetch_data(self):
            cconn=mysql.connector.connect(host='localhost',username='root',password="1234",database='mynewdata2')
            my_cursor=cconn.cursor()
            my_cursor.execute('select * from employee1')
            data=my_cursor.fetchall()
            if len(data)!=0:
                    self.employee_table.delete(*self.employee_table.get_children())
                    for i in data:
                            self.employee_table.insert("",END,values=i)
            cconn.commit()
            cconn.close()
    def get_cursor(self,event=""):
            cursor_row=self.employee_table.focus()
            content=self.employee_table.item(cursor_row)
            data=content['values']

            self.var_dep.set(data[0])
            self.var_name.set(data[1])
            self.var_designition.set(data[2])
            self.var_email.set(data[3])
            self.var_address.set(data[4])
            self.var_married.set(data[5])
            self.var_dob.set(data[6])
            self.var_doj.set(data[7])
            self.var_idproofcomb.set(data[8])
            self.var_idproof.set(data[9])
            self.var_gender.set(data[10])
            self.var_phone.set(data[11])
            self.var_pms.set(data[12])
            self.var_ctc.set(data[13])

    def update_data(self):
            if self.var_dep.get()=="" or self.var_email.get()=="":
                    messagebox.showerror('Error','All fields are required')
            else:
                try:
                        update=messagebox.askyesno('Update','Are You Sure update this employee1 data')
                        if update>0:

                                cconn=mysql.connector.connect(host='localhost',username='root',password="1234",database='mynewdata2')
                                my_cursor=cconn.cursor()
                                my_cursor.execute('update employee1 set Department=%s,Name=%s,Designation=%s,Email=%s,Address=%s,Married_status=%s,DOB=%s,DOJ=%s,Id_proof_type=%s,Gender=%s,Phone=%s,PMS=%s,ctc=%s where Id_proof=%s',(
                                                                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                                                                self.var_name.get(),
                                                                                                                                                                                                                                self.var_designition.get(),
                                                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                                                self.var_married.get(),
                                                                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                                                                self.var_doj .get(),
                                                                                                                                                                                                                                self.var_idproofcomb.get(),
                                                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                                                                self.var_pms.get(),
                                                                                                                                                                                                                                self.var_ctc.get(),
                                                                                                                                                                                                                                self.var_idproof.get()                                                                                                              
                                                                                                                                                                                                                                ))
                        else:
                                if not update:
                                        return
                        cconn.commit()
                        self.fetch_data()
                        cconn.close()
                        messagebox.showinfo('success','Employee Successfully Updated',parent=self.root)
                except Exception as es:
                        messagebox.showerror('Error',f'due To:{str(es)}',parent=self.root)

    def delete_data(self):
            if self.var_idproof.get()=="":
                    messagebox.showerror('Error','All Fields are required')
            else:
                    try:
                            Delete=messagebox.askyesno('Delete','Are you sure delete this employee',parent=self.root)
                            if Delete>0:
                                    cconn=mysql.connector.connect(host='localhost',username='root',password="1234",database='mynewdata2')
                                    my_cursor=cconn.cursor()
                                    sql='delete from employee1 where Id_proof=%s'
                                    value=(self.var_idproof.get(),)
                                    my_cursor.execute(sql,value)
                            else:
                                    if not Delete:
                                            return
                            cconn.commit()
                            self.fetch_data()
                            cconn.close()
                            messagebox.showinfo('Delete','Employee Successfully Deleted',parent=self.root)
                    except Exception as es:
                        messagebox.showerror('Error',f'due To:{str(es)}',parent=self.root)

    
    
    def reset_data(self):
            self.var_dep.set("Select Department")
            self.var_name.set("")
            self.var_designition.set("")
            self.var_email.set("")
            self.var_address.set("")
            self.var_married.set("Married")
            self.var_dob.set("")
            self.var_doj.set("")
            self.var_idproofcomb.set("Select Id Proof")
            self.var_idproof.set("")
            self.var_gender.set("")
            self.var_phone.set("")
            self.var_pms.set("")
            self.var_ctc.set("")


    def search_data(self):
            if self.var_com_search.get()==''or self.var_search.get()=='':
                    messagebox.showerror('Error','Please select option')
            else:
                    try:
                            cconn=mysql.connector.connect(host='localhost',username='root',password="1234",database='mynewdata2')
                            my_cursor=cconn.cursor()
                            my_cursor.execute('select * from employee1 where ' +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get()+"%'"))
                            rows=my_cursor.fetchall()
                            if len(rows)!=0:
                                    self.employee_table.delete(*self.employee_table.get_children())
                                    for i in rows:
                                            self.employee_table.insert("",END,values=i)
                            cconn.commit
                            cconn.close()
                            
                            
                    except Exception as es:
                        messagebox.showerror('Error',f'due To:{str(es)}',parent=self.root)
   












if __name__=="__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()

