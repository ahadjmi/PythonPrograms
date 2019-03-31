
from tkinter import *
import tkinter.messagebox
import sqlite3

conn = sqlite3.connect('store.db')
c = conn.cursor()

class store:

    def __init__(self,master):
        self.master = master
        master.title('Touheed Store')

#===============login page===============================================================================================================

        self.loghead = Label(master,text = ' Admin Login ',font ='arial 15 bold',fg ='green')
        self.loghead.place(x=160,y=20)

        self.user = Label(master,text ='Username :')
        self.user.place(x =100,y=80)
        self.password = Label(master,text ='Password :')
        self.password.place(x=100,y=120)

        self.euser = Entry(master)
        self.euser.place(x=170,y=80)

        self.epassword =Entry(master,show ='*')
        self.epassword.place(x =170,y=120)

        self.check = Checkbutton(master,text = 'remember me',fg ='blue')
        self.check.place(x=170,y=150)

        self.blogin=Button(master,text ='login' ,height =1,width=8,bg ='light blue', command = self.login)
        self.blogin.place(x=200,y=200)

        self.changepass = Button(master, text='Change password', height=1, width=15, bg='light green', command=self.change_pass)
        self.changepass.place(x=170, y=280)

        self.createacc = Button(master, text='Create Account', height=1, width=15, bg='light green',
                                 command=self.create_acc)
        self.createacc.place(x=170, y=340)

        self.forgetpass = Button(master, text='Forget password', height=1, width=15, bg='light green',
                                command=self.forget_pass)
        self.forgetpass.place(x=170, y=400)

        self.master.geometry('420x500')
        self.master.resizable(FALSE,FALSE)

    def login(self):

        try:
            self.fuser = self.euser.get()
            self.fpass = self.epassword.get()

            sql ='select username,password from user where username like ?'

            cursor = c.execute(sql,(self.fuser,))

            for self.i in cursor:
                self.username=self.i[0]
                self.passwrd =self.i[1]


            if self.fuser == self.username and self.fpass == self.passwrd:
                self.mainpage = Toplevel(self.master)
                self.mainpage.geometry('1550x750')
                self.lheadmain=Label(self.mainpage,text='Welcome to Touheed Kirana Store',font='arial 17',fg='green')
                self.lheadmain.place(x=500,y=30)



            else:
                tkinter.messagebox.showinfo('Invalid', 'Invalid password \nPlease enter correct password.   ')

        except AttributeError:
            tkinter.messagebox.showinfo('Invalid','Invalid username and password \nPlease enter correct username.  ')




    def change_pass(self):
        self.cpasspage = Toplevel(self.master)
        self.cpasspage.geometry('500x600')

        self.chead = Label(self.cpasspage,text = 'Change password',fg ='green',font ='courier 15 bold')
        self.chead.place(x=150,y=30)

        self.cpuser = Label(self.cpasspage, text='Username :')
        self.cpuser.place(x=140, y=80)
        self.cppassword = Label(self.cpasspage, text='Password :')
        self.cppassword.place(x=140, y=120)

        self.ecpuser = Entry(self.cpasspage)
        self.ecpuser.place(x=210, y=80)

        self.ecppass = Entry(self.cpasspage, show='*')
        self.ecppass.place(x=210, y=120)

        self.bcpsubmit=Button(self.cpasspage,text='Submit',height=1,width=10,bg='orange',command=self.cpsubmit)
        self.bcpsubmit.place(x=210,y=170)

    def cpsubmit(self):

        try:

            self.x1=self.ecpuser.get()
            self.x2=self.ecppass.get()

            s='select username,password from user where username like ?'
            r=c.execute(s,(self.x1,))

            for self.i in r:
                self.u1=self.i[0]
                self.p1=self.i[1]

            if self.x1==self.u1 and self.x2==self.p1:

                self.lnewpass = Label(self.cpasspage,text='        New password : ')
                self.lnewpass.place(x=90,y=280)

                self.lnewcpass = Label(self.cpasspage, text='  Confirm password : ')
                self.lnewcpass.place(x=90, y=320)

                self.enewpass = Entry(self.cpasspage,show='*')
                self.enewpass.place(x=210,y=280)

                self.enewcpass =Entry(self.cpasspage,show='*')
                self.enewcpass.place(x=210,y=320)

                self.bchange = Button(self.cpasspage,text='Change password',height =1,width =15,bg='light green',command=self.change)
                self.bchange.place(x=180,y=370)

            else:
                tkinter.messagebox.showinfo('Invalid','Invalid Password.    ')

        except AttributeError:
            tkinter.messagebox.showinfo('Invalid','Invalid Username.    ')

            self.cpasspage.destroy()

    def change(self):

        self.p2=self.enewpass.get()
        self.p3=self.enewcpass.get()

        if self.p2==self.p3:

            sq='update user set password=? where username like ?;'
            c.execute(sq,(self.p2,self.x1))
            conn.commit()
            tkinter.messagebox.showinfo('Successful','Password successfully changed.     ')
            self.cpasspage.destroy()

        else:
            tkinter.messagebox.showinfo('Incorrect','Incorrect Format of password.   \nPlease enter correct format.    ')




    def create_acc(self):


        self.caccpage = Toplevel(self.master)
        self.caccpage.geometry('500x600')

        self.cahead = Label(self.caccpage, text='Create Account', fg='red', font='courier 15 bold')
        self.cahead.place(x=150, y=30)

    #=======Create Label====================================================================================================

        self.lfname =Label(self.caccpage,text ='                First name :')
        self.lfname.place(x=130,y=90)

        self.llname = Label(self.caccpage, text='                Last name :')
        self.llname.place(x=130, y=140)

        self.lmobile = Label(self.caccpage, text='       Mobile number :')
        self.lmobile.place(x=130, y=190)

        self.lemail = Label(self.caccpage, text='                    Email id :')
        self.lemail.place(x=130, y=240)

        self.luser = Label(self.caccpage, text='                 username :')
        self.luser.place(x=130, y=290)

        self.lpass = Label(self.caccpage, text='                  password :')
        self.lpass.place(x=130, y=340)

        self.lcpass = Label(self.caccpage, text=' Confirm password :')
        self.lcpass.place(x=130, y=390)

    #=========Create Entry===================================================================================================

        self.efname = Entry(self.caccpage)
        self.efname.place(x=250,y=90)

        self.elname = Entry(self.caccpage)
        self.elname.place(x=250, y=140)

        self.emobile = Entry(self.caccpage)
        self.emobile.place(x=250, y=190)

        self.eemail = Entry(self.caccpage)
        self.eemail.place(x=250, y=240)

        self.euser = Entry(self.caccpage)
        self.euser.place(x=250, y=290)

        self.epass = Entry(self.caccpage,show='*')
        self.epass.place(x=250, y=340)

        self.ecpass = Entry(self.caccpage,show='*')
        self.ecpass.place(x=250, y=390)

        self.bsubmit =Button(self.caccpage,text ='submit',height =1,width =12,bg='light blue',command=self.submit_button)
        self.bsubmit.place(x=190,y=470)


    def forget_pass(self):

        self.forgetpage = Toplevel(self.master)
        self.forgetpage.geometry('500x600')

        self.cahead = Label(self.forgetpage, text='Forget password', fg='green', font='courier 15 bold')
        self.cahead.place(x=150, y=40)

        self.lforuser=Label(self.forgetpage,text='             Username : ')
        self.lforuser.place(x=100,y=120)

        self.lforpass = Label(self.forgetpage, text='   Mobile number : ')
        self.lforpass.place(x=100, y=160)

        self.eforuser =Entry(self.forgetpage)
        self.eforuser.place(x=210,y=120)

        self.eformobile = Entry(self.forgetpage)
        self.eformobile.place(x=210, y=160)

        self.bforget=Button(self.forgetpage,text='Submit',bg='orange',height=1,width=10,command=self.view_pass)
        self.bforget.place(x=210,y=210)

    def view_pass(self):
        try:
            self.vu = self.eforuser.get()
            self.vm = int(self.eformobile.get())

            sq1='select password,mobile,fname from user where username like ?;'
            r1=c.execute(sq1,(self.vu,))

            for self.j in r1:
                self.z1 = self.j[0]
                self.mo = self.j[1]
                self.z3 = self.j[2]

            print(self.j[2])

            if self.vm == self.mo:

                tkinter.messagebox.showinfo('password',' Dear ' +str(self.z3) + ' \nYour password is ' + str(self.z1))

            else:
                tkinter.messagebox.showinfo('Warning','Mobile number does not exist.   \nPlease enter correct number')


        except AttributeError:
            tkinter.messagebox.showinfo('Warning','  Username does not exist.      ')


    def submit_button(self):

        try:
            self.v1 = self.efname.get()
            self.v2 = self.elname.get()
            self.v3 = self.emobile.get()
            self.v4 = self.eemail.get()
            self.v5 = self.euser.get()
            self.v6 = self.epass.get()
            self.v7 = self.ecpass.get()

            if self.v1=='' or self.v2=='' or self.v3==' ' or self.v4=='' or self.v5=='' or self.v6=='' or self.v7=='':
                tkinter.messagebox.showinfo('Warning','Please fill all the entries.  ')

            else:

                if self.v6 == self.v7:

                    sql2 = 'insert into user (fname,lname,mobile,email,username,password) values(?,?,?,?,?,?);'
                    c.execute(sql2, (self.v1, self.v2, self.v3, self.v4, self.v5, self.v6))
                    conn.commit()

                    tkinter.messagebox.showinfo('submitted', str(self.v1) + ' info successfully submitted')

                else:
                    tkinter.messagebox.showinfo('Incorrect', 'Password not matched \nPlease enter correct format. ')


        except sqlite3.IntegrityError as e:
            tkinter.messagebox.showinfo('Already exist','username already exist   \nplease try another username.  ')




root = Tk()

a = store(root)

root.mainloop()
