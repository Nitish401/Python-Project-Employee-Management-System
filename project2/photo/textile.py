from ast import Return
from cProfile import label
from email.mime import image, message
from multiprocessing import connection
from re import search
from telnetlib import STATUS
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter.messagebox import showerror
from tkinter import messagebox
from turtle import bgcolor, width
from PIL import Image,ImageTk
import mysql.connector





class Employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x750+0+0")
        self.root.title(" Employee Management System")
#variables:
        self.var_dep=StringVar()
        self.var_name=StringVar()
        self.var_Designition=StringVar()
        self.var_Email=StringVar()
        self.var_address=StringVar()
        self.var_married=StringVar()
        self.var_dob=StringVar()
        self.var_doj =StringVar()
        self.var_aadhar=StringVar()
        self.var_gender=StringVar()
        self.var_phone=StringVar()
        self.var_ctc=StringVar()
        self.var_pms=StringVar()
       



        lbl_title=Label(self.root,text='HAREN TEXTILES EMPLOYEE MANAGEMENT SYSTEM',font=('times new roman',30,'bold'),fg='darkblue',bg='white')
        lbl_title.place(x=0,y=0,width=1400,height=50)
        # logo
        img_logo=Image.open('photo/logo.png')
        img_logo=img_logo.resize((50,50),Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)

       


        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=100,y=0,width=50,height=50)
#img frame
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=50,width=1330,height=160)

# img1
        img1=Image.open('photo/ph1.jpg')
        img1=img1.resize((540,160),Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(img1)


        self.img1=Label(img_frame,image=self.photo1)
        self.img1.place(x=0,y=0,width=540,height=140)

#img2   
        img2=Image.open('photo/ph2.jpg')
        img2=img2.resize((540,160),Image.ANTIALIAS)
        self.photo2=ImageTk.PhotoImage(img2)


        self.img2=Label(img_frame,image=self.photo1)
        self.img2.place(x=0,y=0,width=540,height=140)


#main frame
       
        Main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        Main_frame.place(x=10,y=220,width=1450,height=560)

#upper frame
        upper_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,bg='white',text='Employee_Information',font=('times new roman',11,'bold'),fg='red')
        upper_frame.place(x=10,y=10,width=1330,height=240)

        # Labels and Entry fields
        lbl_dep=Label(upper_frame,text="Department",font=('arial',10,'bold'),bg='white')
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)

        combo_dep=ttk.Combobox(upper_frame,textvariable=self.var_dep,font=('arial',11,'bold'),width=17,state='readonly')
        combo_dep['value']=('select Department','Admin','HR','Opex','Warping','Weaving','Dyeing','Knitting','folding')
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10, sticky=W)
    #name
        lbl_Name=Label(upper_frame,font=("arial",10,"bold"),text="Name:",bg="white")
        lbl_Name.grid(row=0,column=2,sticky=W,padx=2,pady=7)

        txt_name=ttk.Entry(upper_frame,textvariable=self.var_name,width=22,font=("arial",11,"bold"))
        txt_name.grid(row=0,column=3,padx=2,pady=7)
# # lbl_Designition
        lbl_Designition=Label(upper_frame,font=("arial",10,"bold"),text="Designition:",bg="white")
        lbl_Designition.grid(row=1,column=0,sticky=W,padx=2,pady=7)

        txt_Designition=ttk.Entry(upper_frame,textvariable=self.var_Designition,width=22,font=("arial",11,"bold"))
        txt_Designition.grid(row=1,column=1,padx=2,pady=7)
# Email
        lbl_Email=Label(upper_frame,font=("arial",10,"bold"),text="Email:",bg="white")
        lbl_Email.grid(row=1,column=2,sticky=W,padx=2,pady=7)

        txt_Email=ttk.Entry(upper_frame,textvariable=self.var_Email,width=22,font=("arial",11,"bold"))
        txt_Email.grid(row=1,column=3,padx=2,pady=7)
    #address

        lbl_Address=Label(upper_frame,font=("arial",10,"bold"),text="Address:",bg="white")
        lbl_Address.grid(row=2,column=0,sticky=W,padx=2,pady=7)

        txt_Address=ttk.Entry(upper_frame,textvariable=self.var_address,width=22,font=("arial",11,"bold"))
        txt_Address.grid(row=2,column=1,padx=2,pady=7)
    
    #married
    #@@@@lbl_PMS=Label(upper_frame,font=("arial",10,"bold"),text="PMS Percentage:",bg="white")
        #lbl_PMS.grid(row=2,column=4,sticky=W,padx=2,pady=7)

       # txt_PMS=ttk.Entry(upper_frame,textvariable=self.var_pms,width=22,font=("arial",11,"bold"))
        #txt_PMS.grid(row=2,column=5,padx=2,pady=7)



        #lbl_married =Label(upper_frame,textvariable=self.var_married,font=("arial",10,"bold"),text="married:",bg="white")
        #lbl_married.grid(row=3,column=4,sticky=W,padx=2,pady=7)
       
        #txt_married=ttk.Entry(upper_frame,textvariable=self.var_married,width=22,font=("arial",11,"bold"))
        #txt_married.grid(row=4,column=5,padx=2,pady=7)
    
    #lbl_gender=Label(upper_frame,font=("arial",10,"bold"),text="Gender:",bg="white")
       # lbl_gender.grid(row=4,column=2,sticky=W,padx=2,pady=7)

        #txt_gender=ttk.Entry(upper_frame,textvariable=self.var_gender,width=22,font=("arial",11,"bold"))
       # txt_gender.grid(row=4,column=3,padx=2,pady=7)


      #dob  
        lbl_dob=Label(upper_frame,font=("arial",10,"bold"),text="DOB:",bg="white")
        lbl_dob.grid(row=3,column=0,sticky=W,padx=2,pady=7)

        txt_dob=ttk.Entry(upper_frame,textvariable=self.var_dob,width=22,font=("arial",11,"bold"))
        txt_dob.grid(row=3,column=1,padx=2,pady=7)
    
      #doj  
        lbl_doj=Label(upper_frame,font=("arial",10,"bold"),text="DOJ:",bg="white")  
        lbl_doj.grid(row=3,column=2,sticky=W,padx=2,pady=7)

        txt_doj=ttk.Entry(upper_frame,textvariable=self.var_doj,width=22,font=("arial",11,"bold"))
        txt_doj.grid(row=3,column=3,padx=2,pady=7)

    #aadhar
        lbl_aadhar=Label(upper_frame,font=("arial",10,"bold"),text="Aadhar No:",bg="white")
        lbl_aadhar.grid(row=4,column=0,sticky=W,padx=2,pady=7)

        txt_aadhar=ttk.Entry(upper_frame,textvariable=self.var_aadhar,width=22,font=("arial",11,"bold"))
        txt_aadhar.grid(row=4,column=1,padx=2,pady=7)

       # gender
        lbl_gender=Label(upper_frame,font=("arial",10,"bold"),text="Gender:",bg="white")
        lbl_gender.grid(row=2,column=2,sticky=W,padx=2,pady=7)

        txt_gender=ttk.Entry(upper_frame,textvariable=self.var_gender,width=22,font=("arial",11,"bold"))
        txt_gender.grid(row=2,column=3,padx=2,pady=7)


#lbl_married=Label(upper_frame,textvariable=self.var_married,font=("arial",10,"bold"),text="Married Status:",bg="white")
       # lbl_married.grid(row=2,column=2,sticky=W,padx=2,pady=7)

        #txt_Married=ttk.Entry(upper_frame,textvariable=self.var_married,width=22,font=("arial",11,"bold"))
        #txt_Married.grid(row=2,column=3,padx=2,pady=7)
        # phone
        lbl_Phone=Label(upper_frame,font=("arial",10,"bold"),text="Phone:",bg="white")
        lbl_Phone.grid(row=0,column=4,sticky=W,padx=2,pady=7)

        txt_Phone=ttk.Entry(upper_frame,textvariable=self.var_phone,width=22,font=("arial",11,"bold"))
        txt_Phone.grid(row=0,column=5,padx=2,pady=7)

        
        # CTC
        lbl_CTC=Label(upper_frame,font=("arial",10,"bold"),text="CTC:",bg="white")
        lbl_CTC.grid(row=1,column=4,sticky=W,padx=2,pady=7)

        txt_CTC=ttk.Entry(upper_frame,textvariable=self.var_ctc,width=22,font=("arial",11,"bold"))
        txt_CTC.grid(row=1,column=5,padx=2,pady=7)

        # PMS
        lbl_PMS=Label(upper_frame,font=("arial",10,"bold"),text="PMS Percentage:",bg="white")
        lbl_PMS.grid(row=2,column=4,sticky=W,padx=2,pady=7)

        txt_PMS=ttk.Entry(upper_frame,textvariable=self.var_pms,width=22,font=("arial",11,"bold"))
        txt_PMS.grid(row=2,column=5,padx=2,pady=7)

        

#mask img
        img_mask=Image.open('photo/cph5.png')
        img=img_mask.resize((220,220),Image.ANTIALIAS)
        self.photo2=ImageTk.PhotoImage(img_mask)

        self.img_mask=Label(upper_frame,image=self.photo2)
        self.img_mask.place(x=935,y=0,width=220,height=220)

#Button frame
        Button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        Button_frame.place(x=1180,y=2,width=140,height=210)

        btn_add=Button(Button_frame,text="Add",command=self.add_data,font=("arial",15,"bold"),width=10,bg='blue',fg='white')
        btn_add.grid(row=0,column=0,padx=1,pady=5)
        
        btn_Update=Button(Button_frame,text="Update",font=("arial",15,"bold"),width=10,bg='blue',fg='white')
        btn_Update.grid(row=1,column=0,padx=1,pady=5)

#delete Frame
        

        btn_Delete=Button(Button_frame,text="Delete",font=("arial",15,"bold"),width=10,bg='blue',fg='white')
        btn_Delete.grid(row=2,column=0,padx=1,pady=5)

#clear Frame 
        

        btn_Clear=Button(Button_frame,text="Clear",font=("arial",15,"bold"),width=10,bg='blue',fg='white')
        btn_Clear.grid(row=3,column=0,padx=1,pady=5)

        
        
        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,bg='white',text='Employee_Information_table',font=('times new roman',11,'bold'),fg='red')
        down_frame.place(x=10,y=250,width=1330,height=270)

        #search frame

        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,bg='white',text='Search Employee information',font=('times new roman',11,'bold'),fg='red')
        search_frame.place(x=0,y=0,width=1330,height=60)

        search_by=Label(search_frame,font=("arial",11,"bold"),text="Search By:",fg="white",bg="red")
        search_by.grid(row=0,column=0,sticky=W,padx=5)


        com_txt_search=ttk.Combobox(search_frame,state="readonly",
                                                        font=("arial",12,"bold"),width=10)
        com_txt_search['value']=("Select option","phone","Aadhar card","Name")                                                      
        com_txt_search.current(0) 
        com_txt_search.grid(row=0,column=1,sticky=W,padx=5) 

        txt_search=ttk.Entry(search_frame,width=22,font=("arial",11,"bold"))   
        txt_search.grid(row=0,column=3,padx=5) 
        
        btn_search=Button(search_frame,text="search",font=("arial",11,"bold"),width=14,bg='blue')
        btn_search.grid(row=0,column=4,padx=5)

        btn_ShowAll=Button(search_frame,text="ShowAll",font=("arial",11,"bold"),width=14,bg='blue')
        btn_ShowAll.grid(row=0,column=5,padx=5)

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#Emplyoee table=+=+=+=+=+=+=+====================================#

# table frame
        Table_frame=Frame(down_frame,bd=3,relief=RIDGE,)
        Table_frame.place(x=0,y=60,width=1325,height=130)

        #scrool baar
        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL) 
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.employee_table=ttk.Treeview(Table_frame,column=("dep","name","designation","phone","gender","pms","aadhar","ctc","email","address","dob","doj","married"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)


        self.employee_table.heading('dep',text='Department')
        self.employee_table.heading('name',text='Name')
        self.employee_table.heading('designation',text='Designation')
        self.employee_table.heading('phone',text='Phone')
        self.employee_table.heading('gender',text='Gender')
        self.employee_table.heading('pms',text='pms')
        self.employee_table.heading('aadhar',text='Aadhar')
        self.employee_table.heading('ctc',text='CTC')
        self.employee_table.heading('email',text='Email')
        self.employee_table.heading('address',text='Address')
        self.employee_table.heading('dob',text='DOB')
        self.employee_table.heading('doj',text='DOJ')
        self.employee_table.heading('married',text='Married Status')
        
        self.employee_table['show']='headings'

        self.employee_table.column("dep",width=100)
        self.employee_table.column("name",width=100)
        self.employee_table.column("designation",width=100)
        self.employee_table.column("phone",width=100)
        self.employee_table.column("gender",width=100)
        self.employee_table.column("pms",width=100)
        self.employee_table.column("aadhar",width=100)
        self.employee_table.column("dob",width=100)
        self.employee_table.column("doj",width=100)
        self.employee_table.column("married",width=100)
        self.employee_table.column("ctc",width=100)
        self.employee_table.column("email",width=100)
        self.employee_table.column("address",width=100)

        

        
        self.employee_table.pack(fill=BOTH,expand=1)


     #function declaration


    def add_data(self):
            if self.var_dep.get()=="" or self.var.email.get()=="":
                    messagebox.showerror('Error','All fields are required')
            else:
                try:
                    conn=mysql.connector.connect(host='localhost',username='root',password="",databse='mydata2')
                    my_cursor=conn.cursor()
                    my_cursor.execute('INSERT INTO emp2(Department,Name,Designition,Email,Address,Phone,Gender,PMS,Aadhar,dob,doj,CTC) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                                                                            self.varchar_name.get(),
                                                                                                            self.varchar_dep.get(),
                                                                                                            self.varchar_Designition.get(),
                                                                                                            self.varchar_Email.get(),
                                                                                                            self.varchar_address.get(),
                                                                                                            self.varchar_married.get(),
                                                                                                            self.varchar_dob.get(),
                                                                                                            self.varchar_doj .get(),
                                                                                                            self.varchar_aadhar.get(),
                                                                                                            self.varchar_gender.get(),
                                                                                                            self.varchar_phone.get(),
                                                                                                            self.varchar_ctc.get(),
                                                                                                            self.varchar_pms.get()
                                                                                                         ))


                    
                    messagebox.showerror('Success','Employee has been added!',parent=self.root) 
                except Exception  as es:
                        messagebox.showerror('Error',f'due To:{str(es)}',parent=self.root)                                                                                    
                conn.commit()
                conn.close()









       # txt_search=ttk.Entry(search_frame,width=22,font=("arial",11,"bold"))  
       # txt_search.grid(row=0,column=2,padx=5)            



if __name__=="__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()