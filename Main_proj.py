from tkinter import *
import itertools
import tkinter.messagebox
import mysql.connector as sql

def start():
    global sat
    sat=Tk()
    sat.geometry('360x350')
    sat.title('start')
    a=Label(sat,text='           DIGITAL VOTING',width='20',font=('impact',20),background='blue',foreground='yellow')
    a.place(x=40,y=25)
    b1=tkinter.Button(sat,text='Login',bg='blue',fg='yellow',font=("impact",13),command=redirect_login)
    b1.place(x=40,y=120,width=285)
    b2=tkinter.Button(sat,text='Sign Up',bg='blue',fg='yellow',font=("impact",13),command=sign)
    b2.place(x=40,y=180,width=285)
    b3=tkinter.Button(sat,text='Exit',bg='blue',fg='yellow',font=("impact",13),command=exito)
    b3.place(x=40,y=240,width=285)
    mainloop()

def exito():
    m=tkinter.messagebox.askquestion('Exit','Are you sure?')
    if m=='yes':
        sat.destroy()
        
def redirect_login():
    sat.destroy()
    login()

def backtostart():
    try:
        sign.destroy()
    except:
        log.destroy()
    start()

def login():
    global log
    obj=sql.connect(host='localhost',user='root',passwd='Aaryan16',database='vote')
    cursor=obj.cursor()
    log=Tk()
    log.geometry('525x400')
    log.title('Login')
    l1=tkinter.Label(log,text='LOGIN',width='25',font=('impact',20),background='green',foreground='white')
    l1.place(x=100,y=25)
    def check():
        first=v1.get()
        last=v2.get()
        userid=v3.get()
        f=first.lower()
        l=last.lower()
        qs='select * from student where first="{}" and last="{}" and id={}'.format(f,l,userid)
        cursor.execute(qs)
        result=cursor.fetchall()
        if cursor.rowcount==1:
            tkinter.messagebox.showinfo('Successfull','Welcome user')
            log.destroy()
            mainpage()
        else:
            tkinter.messagebox.showwarning('Unsucessfull','Try again')
    l2=Label(log,text='First Name',width=20,font=('Bahnschrift SemiBold',11))
    l2.place(x=100,y=100)
    v1=StringVar() 
    t1=Entry(log,textvariable=v1)
    t1.place(x=300,y=100)
    l3=Label(log,text='Last Name',width=20,font=('Bahnschrift SemiBold',11))
    l3.place(x=100,y=150)
    v2=StringVar()
    t2=Entry(log,textvariable=v2)
    t2.place(x=300,y=150)
    l4=Label(log,text='User ID',width=20,font=('Bahnschrift SemiBold',11))
    l4.place(x=100,y=200)
    v3=IntVar()
    t3=Entry(log,textvariable=v3,show='*')
    t3.place(x=300,y=200)
    h1=tkinter.Button(log,text="Submit",width=20,bg='green',fg='white',font=('Bahnschrift SemiBold',11),command=check)
    h1.place(x=170,y=270)
    h2=tkinter.Button(log,text='Back',bg='green',fg='white',font=('Bahnschrift SemiBold',11),command=backtostart)
    h2.place(x=390,y=340,width=100)
    mainloop()

def redirect_mainpage():
    register.destroy()
    mainpage()

    
def reg():
    global register
    obj=sql.connect(host='localhost',user='root',passwd='Aaryan16',database='vote')
    cursor=obj.cursor()
    register=Tk()
    register.geometry('700x450')
    register.title('Registration')
    def save():
        name=v1.get()
        userid=v2.get()
        gender=v3.get()
        course=v4.get()
        post=v5.get()
        qs='insert into registr values("{}","{}","{}","{}","{}")'.format(name,userid,gender,course,post)
        cursor.execute(qs)
        obj.commit()
        if cursor.rowcount>0:
            tkinter.messagebox.showinfo('User info','Data Saved')
            redirect_mainpage()
        else:
             tkinter.messagebox.showinfo('User info','Cannot add to Database')
    l1=Label(register,text='     REGISTRATION FORM',width=18,font=('impact',22),background='green',foreground='white')
    l1.place(x=220,y=30)
    l2=Label(register,text='Full Name',width=20,font=('Bahnschrift SemiBold',12))
    l2.place(x=180,y=90)
    v1=StringVar()
    t1=Entry(register,textvariable=v1)
    t1.place(x=400,y=90,width=150)
    l3=Label(register,text="User id",width=20, font= ("Bahnschrift SemiBold", 12))
    l3.place(x=180,y=130)
    v2=StringVar()
    t2=Entry(register,textvariable=v2)
    t2.place(x=400,y=130,width=150)
    l4=Label(register,text="Gender",width=20,font=("Bahnschrift SemiBold", 12))
    l4.place(x=180,y=170)
    v3=StringVar()
    v3.set(None)
    r1=Radiobutton(register,text="Male",variable=v3,value="male")
    r1.place(x=400,y=170)
    r2=Radiobutton(register,text="Female",variable =v3,value="female")
    r2.place(x=490,y=170)
    l5=Label(register,text ="Course", width=20, font=("Bahnschrift SemiBold",12))
    l5.place(x=180,y=210)
    list1=['','Physics','Chemsitry','Engineering','Molecular Biology','Mathematics', 'Medical','Computer Science','Economics','Literature','Arts & Media']
    v4=StringVar()
    droplist=OptionMenu(register,v4,*list1)
    v4.set("Select your Course")
    droplist.place(x=400,y=210,width=150)
    l6=Label(register,text ="Post", width=20, font=("Bahnschrift SemiBold",12))
    l6.place(x=180,y=250)
    list21=['','President','Vice-President','Speaker','Treasurer','Cultural Secretary','Sports Secretary']
    v5=StringVar()
    droplis=OptionMenu(register,v5,*list21)
    v5.set("Select your Post")
    droplis.place(x=400,y=250,width=150)
    h1=tkinter.Button(register,text="Submit",command=save,bg='red',fg='white',font=('Bahnschrift SemiBold',13))
    h1.place(x=300,y=300,width=150)
    h2=tkinter.Button(register,text='Back',command=redirect_mainpage,bg='red',fg='white',font=('Bahnschrift SemiBold',12))
    h2.place(x=540,y=390,width=120)
    register.mainloop()


def sign():
    global sign
    sat.destroy()
    obj=sql.connect(host='localhost',user='root',passwd='Aaryan16',database='vote')
    cursor=obj.cursor()
    sign=Tk()
    sign.geometry('600x400')
    sign.title('SIGN UP')
    def stud():
        first=v1.get()
        last=v2.get()
        course=v3.get()
        id=v4.get()
        dob=v5.get()
        qs='insert into student values("{}","{}","{}","{}","{}")'.format(first,last,course,id,dob)
        cursor.execute(qs)
        obj.commit()
        if cursor.rowcount>0:
            tkinter.messagebox.showinfo('User info','Data Saved')
            login()
        else:
             tkinter.messagebox.showinfo('User info','Cannot add to Database')
    l1=tkinter.Label(sign,text='SIGN UP',width=10,background='yellow',foreground='red',font=('impact',22))
    l1.place(x=235,y=10)
    l2=Label(sign,text='First Name',width=20,font=('Bahnschrift SemiBold',11))
    l2.place(x=100,y=80)
    v1=StringVar()
    t1=Entry(sign,textvariable=v1)
    t1.place(x=320,y=80,width=150)
    l3=Label(sign,text="Last Name",width=20, font= ('Bahnschrift SemiBold',11))
    l3.place(x=100,y=120)
    v2=StringVar()
    t2=Entry(sign,textvariable=v2)
    t2.place(x=320,y=120,width=150)
    l3=Label(sign,text ="Course", width=20, font=('Bahnschrift SemiBold',11))
    l3.place(x=100,y=160)
    list1=['Physics','Chemsitry','Engineering','Molecular Biology','Mathematics', 'Medical','Computer Science','Economics','Literature','Arts & Media']
    v3=StringVar()
    droplist=OptionMenu(sign,v3,*list1)
    v3.set("Select your Course")
    droplist.place(x=320,y=160,width=150)
    l4=Label(sign,text ="Student ID", width=20, font=('Bahnschrift SemiBold',11))
    l4.place(x=100,y=200)
    v4=StringVar()
    t3=Entry(sign,textvariable=v4)
    t3.place(x=320,y=200,width=150)
    l5=Label(sign,text='Year of Birth',width=20,font=('Bahnschrift SemiBold',11))
    l5.place(x=100,y=240)
    v5=StringVar()
    t4=Entry(sign,textvariable=v5)
    t4.place(x=320,y=240,width=150)
    h1=tkinter.Button(sign,text="Submit",width=20,background="red",foreground="white",font=('Bahnschrift SemiBold',10),command=stud)
    h1.place(x=240,y=290)
    h2=tkinter.Button(sign,text='Back',bg='red',fg='white',font=('Bahnschrift SemiBold',10),command=backtostart)
    h2.place(x=470,y=350,width=100)
    sign.mainloop()

def direct_login():
    back=tkinter.messagebox.askquestion('Log Out','Are you sure?',icon='warning')
    if back=='yes':
        main.destroy()
        start()
    
def cdirect():
    try:
        root.destroy()
    except:
        rot.destroy()
    vote()
     
def exit():
    result=tkinter.messagebox.askquestion('Exit','Are you sure?',icon='warning')
    if result=='yes':
        main.destroy()


    
from tkinter.ttk import *
def listt():
    global root
    root=Tk()
    root.geometry('1005x500')
    root.title("View data of Voters")
    tree=Treeview(root)
    tree["columns"] = (1,2,3,4,5)
    tree.column(1, width = 100)
    tree.column(2, width= 100)
    tree.column(3,width=100)
    tree.column(4,width=100)
    tree.column(5,width=100)
    tree.heading(1,text="FIRST NAME")
    tree.heading(2,text="LAST NAME")
    tree.heading(3,text="COURSE")
    tree.heading(4,text="STUDENT ID")
    tree.heading(5,text='DOB')
    def view():
         obj=sql.connect(host='localhost',user='root',passwd='Aaryan16',database='vote')
         cursor=obj.cursor()
         cursor.execute("select * from student")
         n1=cursor.fetchall()
         for i in n1:
             tree.insert("",'end',values=(i))
             obj.close()
             tree.place(x=100,y=130,width=800)
    def clear():
        for i in tree.get_children():
            tree.delete(i)
    def filter():
        obj=sql.connect(host='localhost',user='root',passwd='Aaryan16',database='vote')
        cursor=obj.cursor()
        a=v.get()
        qs='select * from student where course="{}"'.format(a)
        cursor.execute(qs)
        n1=cursor.fetchall()
        for i in n1:
            tree.insert("",'end',values=(i))
            obj.close()
            tree.place(x=100,y=130,width=800)    
    b1=tkinter.Button(root, text="View", command=view,bg='blue',fg='white',font=('Bahnschrift SemiBold',12))
    b1.place(x=780,y=60,width=120)
    b2=tkinter.Button(root,text="Clear", command=clear,bg='blue',fg='white',font=('Bahnschrift SemiBold',12))
    b2.place(x=100,y=400,width=120)
    b3=tkinter.Button(root,text='Back',command=cdirect,bg='blue',fg='white',font=('Bahnschrift SemiBold',12))
    b3.place(x=780,y=400,width=120)
    l1=tkinter.Label(root,text="Course",width=20,bg='blue',fg='white',font=('Bahnschrift SemiBold',12))
    l1.place(x=100,y=60,width=60)
    list1=['Physics','Chemsitry','Engineering','Molecular Biology','Mathematics', 'Medical','Computer Science','Economics','Literature','Arts & Media']
    v=StringVar()
    droplist=OptionMenu(root,v,*list1)
    v.set("Select Course to Filter")
    droplist.place(x=180,y=60,width=200)
    b4=tkinter.Button(root,text='Filter',command=filter,bg='blue',fg='white',font=('Bahnschrift SemiBold',12))
    b4.place(x=420,y=60,width=120)
    root.mainloop()

def can():
    global rot
    rot=Tk()
    rot.geometry('970x500')
    rot.title("View data of Candidates")
    tree=Treeview(rot)
    tree["columns"] = (1,2,3,4,5)
    tree.column(1, width = 130)
    tree.column(2, width= 100)
    tree.column(3,width=100)
    tree.column(4,width=130)
    tree.column(5,width=160)
    tree.heading(1,text="NAME")
    tree.heading(2,text="STUDENT ID")
    tree.heading(3,text="GENDER")
    tree.heading(4,text="COURSE")
    tree.heading(5,text='POST')
    def canview():
         obj=sql.connect(host='localhost',user='root',passwd='Aaryan16',database='vote')
         cursor=obj.cursor()
         cursor.execute("select * from registr")
         n2=cursor.fetchall()
         for i in n2:
             tree.insert("",'end',values=(i))
             obj.close()
             tree.place(x=80,y=120,width=800)
    def canclear():
        for i in tree.get_children():
            tree.delete(i)
    def canfilter():
        obj=sql.connect(host='localhost',user='root',passwd='Aaryan16',database='vote')
        cursor=obj.cursor()
        a=v1.get()
        qs='select * from registr where post="{}"'.format(a)
        cursor.execute(qs)
        n2=cursor.fetchall()
        for i in n2:
            tree.insert("",'end',values=(i))
            obj.close()
            tree.place(x=80,y=120)    
    b0=tkinter.Button(rot, text="View", command=canview,bg='blue',fg='white',font=('Bahnschrift SemiBold',12))
    b0.place(x=780,y=50,width=100)
    b11=tkinter.Button(rot,text="Clear", command=canclear,bg='blue',fg='white',font=('Bahnschrift SemiBold',12))
    b11.place(x=80,y=405,width=100)
    b33=tkinter.Button(rot,text='Back',command=cdirect,bg='blue',fg='white',font=('Bahnschrift SemiBold',12))
    b33.place(x=780,y=405,width=100)
    l=tkinter.Label(rot,text="Post",width=20,bg='blue',fg='white',font=('Bahnschrift SemiBold',12))
    l.place(x=80,y=50,width=70)
    list2=['President','Vice-President','Speaker','Treasurer','Cultural Secretary','Sports Secretary']
    v1=StringVar()
    droplist=OptionMenu(rot,v1,*list2)
    v1.set("Select Post to Filter")
    droplist.place(x=170,y=50,width=150)
    b44=tkinter.Button(rot,text='Filter',command=canfilter,bg='blue',fg='white',font=('Bahnschrift SemiBold',12))
    b44.place(x=350,y=50,width=100)
    mainloop()

def v_to_main():
    vo.destroy()
    mainpage()

def votes():
    global vo
    vo=Tk()
    vo.title("Voting")
    vo.geometry('500x500')
    def confirm():
        B=tkinter.messagebox.askquestion('confirm','Are you sure?')
        if B=='yes':
            count()
    def count():
        obj=sql.connect(host='localhost',user='root',passwd='Aaryan16',database='vote')
        cursor=obj.cursor()
        pres=a1.get()
        vice=a2.get()
        spea=a3.get()
        trea=a4.get()
        cult=a5.get()
        sport=a6.get()
        if pres=="President" or vice=='Vice-President' or spea=='Speaker' or trea=='Treasurer' or cult=='Cultural Secretary' or sport=='Sports Secretary':
            tkinter.messagebox.showwarning('Retry','Choose a Value')
        else:
            qs="insert into votes values('{}','{}','{}','{}','{}','{}')".format(pres,vice,spea,trea,cult,sport)      
            cursor.execute(qs)
            obj.commit()
            if cursor.rowcount>0:
                tkinter.messagebox.showinfo('Success','Vote added')
                vo.destroy()
                
                
            else:
                tkinter.messagebox.showwarning('failed','Try again')
        
    obj=sql.connect(host='localhost',user='root',passwd='Aaryan16',database='vote')
    cursor=obj.cursor()
    cursor.execute('select name from registr where post="President"')
    n=cursor.fetchall()
    lis1=['']
    for x in n:
        lis1.append(x[0])
        print(lis1)
        
    L1=Label(vo,text='Choose President',width=20,font=('Bahnschrift SemiBold',11))
    L1.place(x=55,y=100,width=150)
    a1=StringVar()
    droplist=OptionMenu(vo,a1,*lis1)
    a1.set('President')
    droplist.place(x=305,y=100,width=150)
    cursor.execute('select name from registr where post="Vice-President"')
    n1=cursor.fetchall()
    lis2=['']
    for x in n1:
        lis2.append(x[0])
    L2=Label(vo,text='Choose Vice-President',width=20,font=('Bahnschrift SemiBold',11))
    L2.place(x=55,y=130,width=160)
    a2=StringVar()
    doplist=OptionMenu(vo,a2,*lis2)
    a2.set('Vice-President')
    doplist.place(x=305,y=130,width=150)
    cursor.execute('select name from registr where post="Speaker"')
    n2=cursor.fetchall()
    lis3=['']
    for x in n2:
        lis3.append(x[0])
    L3=Label(vo,text='Choose Speaker',width=20,font=('Bahnschrift SemiBold',11))
    L3.place(x=55,y=160,width=160)
    a3=StringVar()
    drplist=OptionMenu(vo,a3,*lis3)
    a3.set('Speaker')
    drplist.place(x=305,y=160,width=150)
    cursor.execute('select name from registr where post="Treasurer"')
    n3=cursor.fetchall()
    lis4=['']
    for x in n3:
        lis4.append(x[0])
    L4=Label(vo,text='Choose Tresurer',width=20,font=('Bahnschrift SemiBold',11))
    L4.place(x=55,y=190,width=180)
    a4=StringVar()
    drolist=OptionMenu(vo,a4,*lis4)
    a4.set('Treasurer')
    drolist.place(x=305,y=190,width=150)
    cursor.execute('select name from registr where post="Cultural Secretary"')
    n4=cursor.fetchall()
    lis5=['']
    for x in n4:
        lis5.append(x[0])
    L5=Label(vo,text='Choose Cultural Secretary',width=20,font=('Bahnschrift SemiBold',11))
    L5.place(x=55,y=220,width=180)
    a5=StringVar()
    droplst=OptionMenu(vo,a5,*lis5)
    a5.set('Culural Secretary')
    droplst.place(x=305,y=220,width=150)
    cursor.execute('select name from registr where post="Sports Secretary"')
    n5=cursor.fetchall()
    lis6=['']
    for x in n5:
        lis6.append(x[0])
    L6=Label(vo,text='Choose Sports Secretary',width=20,font=('Bahnschrift SemiBold',11))
    L6.place(x=55,y=250,width=170)
    a6=StringVar()
    droplis=OptionMenu(vo,a6,*lis6)
    a6.set('Sports Secretary')
    droplis.place(x=305,y=250,width=150)
    b1=tkinter.Button(vo,text='Vote',font=('impact',14),foreground='white',bg='red',command=confirm)
    b1.place(x=190,y=300,width=120)
    L7=Label(vo,text=' Choose your Candidate',font=('impact',30),background='blue',foreground='white')
    L7.place(x=55,y=20,width=400)
    b2=tkinter.Button(vo,text='Back to Main',font=('impact',11),fg='white',bg='red',command=v_to_main)
    b2.place(x=340,y=430,width=120)
    mainloop()

def pr():
    global listpre
    obj=sql.connect(host='localhost',user='root',passwd='Aaryan16',database='vote')
    cursor=obj.cursor()
    cursor.execute('select name from registr where post="President"')
    m=cursor.fetchall()
    listpre=[]
    re=[]
    for x in m:
        listpre.append(x[0])
    for i in listpre:
        qs="select count(*) from votes where president='{}'".format(i)
        cursor.execute(qs)
        a=cursor.fetchone()
        for t in a: 
            re.append(t)
    for l in range(0,len(re)):
      s="insert into pres values('{}',{})".format(listpre[l],re[l])
      cursor.execute(s)
      obj.commit()    

def vic():
    global listvpre
    obj=sql.connect(host='localhost',user='root',passwd='Aaryan16',database='vote')
    cursor=obj.cursor()
    cursor.execute('select name from registr where post="Vice-President"')
    m=cursor.fetchall()
    listvpre=[]
    rev=[]
    for x in m:
        listvpre.append(x[0])
    for i in listvpre:
        qs="select count(*) from votes where vice_president='{}'".format(i)
        cursor.execute(qs)
        a=cursor.fetchone()
        for t in a: 
            rev.append(t)
    for l in range(0,len(rev)):
      s="insert into vice values('{}',{})".format(listvpre[l],rev[l])
      cursor.execute(s)
      obj.commit()   

def spea():
    global listsp
    obj=sql.connect(host='localhost',user='root',passwd='Aaryan16',database='vote')
    cursor=obj.cursor()
    cursor.execute('select name from registr where post="Speaker"')
    m=cursor.fetchall()
    listsp=[]
    resp=[]
    for x in m:
        listsp.append(x[0])
    for i in listsp:
        qs="select count(*) from votes where speaker='{}'".format(i)
        cursor.execute(qs)
        a=cursor.fetchone()
        for t in a: 
            resp.append(t)
    for l in range(0,len(resp)):
      s="insert into spea values('{}',{})".format(listsp[l],resp[l])
      cursor.execute(s)
      obj.commit()     
def trea():
    global listrea
    obj=sql.connect(host='localhost',user='root',passwd='Aaryan16',database='vote')
    cursor=obj.cursor()
    cursor.execute('select name from registr where post="Treasurer"')
    m=cursor.fetchall()
    listrea=[]
    rea=[]
    for x in m:
        listrea.append(x[0])
    for i in listrea:
        qs="select count(*) from votes where treasurer='{}'".format(i)
        cursor.execute(qs)
        a=cursor.fetchone()
        for t in a: 
            rea.append(t)
    for l in range(0,len(rea)):
      s="insert into trea values('{}',{})".format(listrea[l],rea[l])
      cursor.execute(s)
      obj.commit() 
      
def cultu():
    global listlt
    obj=sql.connect(host='localhost',user='root',passwd='Aaryan16',database='vote')
    cursor=obj.cursor()
    cursor.execute('select name from registr where post="Cultural Secretary"')
    m=cursor.fetchall()
    listlt=[]
    realt=[]
    for x in m:
        listlt.append(x[0])
    for i in listlt:
        qs="select count(*) from votes where cultural_sec='{}'".format(i)
        cursor.execute(qs)
        a=cursor.fetchone()
        for t in a: 
            realt.append(t)
    for l in range(0,len(realt)):
      s="insert into cult values('{}',{})".format(listlt[l],realt[l])
      cursor.execute(s)
      obj.commit() 

def spo():
    global listspo
    obj=sql.connect(host='localhost',user='root',passwd='Aaryan16',database='vote')
    cursor=obj.cursor()
    cursor.execute('select name from registr where post="Sports Secretary"')
    m=cursor.fetchall()
    listspo=[]
    rspo=[]
    for x in m:
        listspo.append(x[0])
    for i in listspo:
        qs="select count(*) from votes where sports_sec='{}'".format(i)
        cursor.execute(qs)
        a=cursor.fetchone()
        for t in a: 
            rspo.append(t)
    for l in range(0,len(rspo)):
      s="insert into sport values('{}',{})".format(listspo[l],rspo[l])
      cursor.execute(s)
      obj.commit() 

def final():
    global f
    f=Tk()
    pr()
    vic()
    spea()
    trea()
    cultu()
    spo()
    f.geometry('1000x640')
    f.title('Results')
    obj=sql.connect(host='localhost',user='root',passwd='Aaryan16',database='vote')
    cursor=obj.cursor()
    l1=Label(f,text="     R E S U L T S      ",background='green',foreground='white',font=('impact',20))
    l1.place(x=410,y=25)
    tree=Treeview(f)
    tree['columns']=(0,1)
    tree.column(0,width=200)
    tree.column(1,width=100)
    tree.heading(0,text="CANDIDATE")
    tree.heading(1,text="VOTES")
    def clean():
        for i in tree.get_children():
            tree.delete(i)
    def tbl_tre(postp):        
            cursor.execute('select distinct name,count from {} order by count desc'.format(postp))
            n1=cursor.fetchall()
            for z in n1:
                tree.insert("",'end',values=(z))
            cursor.execute('select name,max(count) from {}'.format(postp))
            mvz=cursor.fetchall()
            zim=[]
            for m in mvz:
                for z in m:
                    zim.append(z)
                    print(zim)
            qm=zim[0]
            qn=zim[1]
            LL=Label(f,text="Congratulations! {} has won with {} votes.".format(qm,qn),background='blue',foreground='white',font=('Bahnschrift SemiBold',18))
            LL.place(x=50,y=470,width=600) 
            tree.place(x=80,y=100,width=650,height=330)
     
    def finish():
        g=tkinter.messagebox.askquestion('leave','Are you sure')
        if g=='yes':
            f.destroy()
    
    b1=tkinter.Button(f,text='President',bg='blue',fg='white',command= lambda: tbl_tre('pres'),font=('Bahnschrift SemiBold',12))
    b1.place(x=800,y=100,width=155)
    b2=tkinter.Button(f,text='Vice President',bg='blue',fg='white',command= lambda: tbl_tre('vice'),font=('Bahnschrift SemiBold',12))
    b2.place(x=800,y=160,width=155)
    b3=tkinter.Button(f,text='Speaker',bg='blue',fg='white',command=lambda: tbl_tre('spea'),font=('Bahnschrift SemiBold',12))
    b3.place(x=800,y=220,width=155)
    b4=tkinter.Button(f,text='Treasurer',bg='blue',fg='white',command=lambda: tbl_tre('trea'),font=('Bahnschrift SemiBold',12))
    b4.place(x=800,y=280,width=155)
    b5=tkinter.Button(f,text='Cultural Secretary',bg='blue',fg='white',command= lambda: tbl_tre('cult'),font=('Bahnschrift SemiBold',12))
    b5.place(x=800,y=340,width=155)
    b6=tkinter.Button(f,text='Sports Secretary',bg='blue',fg='white',command=lambda: tbl_tre('sport'),font=('Bahnschrift SemiBold',12))
    b6.place(x=800,y=400,width=155)
    b6=tkinter.Button(f,text='Clear',bg='blue',fg='white',command=clean,font=('Bahnschrift SemiBold',12))
    b6.place(x=800,y=560,width=155)
    b7=tkinter.Button(f,text='Exit',bg='blue',fg='white',command=finish,font=('Bahnschrift SemiBold',12))
    b7.place(x=50,y=560,width=170)
    mainloop()
              
def res():
    global result
    result=Tk()
    result.geometry('400x200')
    def submit():
        a=v1.get()
        b=v2.get()
        if a=='Admin'and b=='60295358':
            tkinter.messagebox.showinfo('logged in','Welcome Admin!')
            result.destroy()
            final()
        else:
            tkinter.messagebox.showwarning('failed','Try Again')
    l1=Label(result,text="Username",font=('Bahnschrift SemiBold',12))
    l1.place(x=80,y=30)
    v1=StringVar()
    t1=Entry(result,textvariable=v1)
    t1.place(x=200,y=30)
    l2=tkinter.Label(result,text="Password",font=('Bahnschrift SemiBold',12))
    l2.place(x=80,y=60)
    v2=StringVar()
    t2=Entry(result,textvariable=v2,show='*')
    t2.place(x=200,y=60)
    b1=tkinter.Button(result,text='Login',command=submit,bg='red',fg='white',font=('Bahnschrift SemiBold',12))
    b1.place(x=140,y=120,width=120)
    mainloop()

def redirect_votes():
    v.destroy()
    votes()
    
def redirect_list():
    v.destroy()
    listt()
 
def redirect_can():
    v.destroy()
    can()

def direct_loginn():
    v.destroy()
    mainpage()

    
def vote():
    global v
    v=Tk()
    v.title('Voting')
    v.geometry('340x330')
    b1=tkinter.Button(v,text='Vote for candidate',command=redirect_votes,bg='blue',fg='white',font=('Bahnschrift SemiBold',12))
    b1.place(x=75,y=45,width=190)
    b2=tkinter.Button(v,text='Voters list',command=redirect_list,bg='blue',fg='white',font=('Bahnschrift SemiBold',12))
    b2.place(x=75,y=110,width=190)
    b3=tkinter.Button(v,text='Candidate list',command=redirect_can,bg='blue',fg='white',font=('Bahnschrift SemiBold',12))
    b3.place(x=75,y=175,width=190)
    b4=tkinter.Button(v,text='Back to Main page',command=direct_loginn,bg='blue',fg='white',font=('Bahnschrift SemiBold',12))
    b4.place(x=75,y=240,width=190)
    mainloop()

def voter():
    main.destroy()
    vote()

def regr():
    main.destroy()
    reg()

def resr():
    main.destroy()
    res()

def mainpage():
    global main
    main=Tk()
    main.title('Main')
    main.geometry('330x400')
    b1=tkinter.Button(main,text='Vote',command=voter,bg='blue',fg='white',font=('Bahnschrift SemiBold',12))
    b1.place(x=75,y=45,width=178)
    b2=tkinter.Button(main,text='Become a candidate',command=regr,bg='blue',fg='white',font=('Bahnschrift SemiBold',12))
    b2.place(x=75,y=110,width=180)
    b3=tkinter.Button(main,text='Results',command=resr,bg='blue',fg='white',font=('Bahnschrift SemiBold',12))
    b3.place(x=75,y=175,width=180)
    b4=tkinter.Button(main,text='Log out',command=direct_login,bg='blue',fg='white',font=('Bahnschrift SemiBold',12))
    b4.place(x=75,y=240,width=180)
    b5=tkinter.Button(main,text='Exit',command=exit,bg='blue',fg='white',font=('Bahnschrift SemiBold',12))
    b5.place(x=75,y=305,width=180)
    mainloop()
start()

