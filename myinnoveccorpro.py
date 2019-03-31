import mysql.connector
from tkinter import *
import tkinter.messagebox
import smtplib

conn= mysql.connector.connect(host="localhost" ,user="root",passwd="12345",database="tvseries")
mydb=conn.cursor()

print(conn)
class myapplication:

    def __init__(self,master):
        self.master = master

        master.title('Movie Series Reminder')
        self.master.geometry('420x660')

        self.loghead = Label(master,text = 'For User input',font ='arial 15 bold',fg ='green')
        self.loghead.place(x=160,y=20)

        self.usermail = Label(master,text ='User email :')
        self.usermail.place(x =80,y=80)
        self.movie1 = Label(master,text ='first movie :')
        self.movie1.place(x=80,y=120)

        self.movie2 = Label(master,text ='second movie :')
        self.movie2.place(x=80,y=160)

        self.movie3 = Label(master,text ='third movie :')
        self.movie3.place(x=80,y=200)

        self.movie4 = Label(master,text ='fourth movie :')
        self.movie4.place(x=80,y=240)

        self.loghead1 = Label(master,text = 'For Admin input',font ='arial 15 bold',fg ='green')
        self.loghead1.place(x=160,y=340)

        self.adminmail = Label(master,text ='admin email :')
        self.adminmail.place(x=50,y=380)
        self.adminpass = Label(master,text ='admin email password :')
        self.adminpass.place(x=40,y=420)

        
        self.mailto = Label(master,text ='send email to:')
        self.mailto.place(x=40,y=480)

        self.emailto = Entry(master)
        self.emailto.place(x=170,y=480)

        self.eadminmail = Entry(master)
        self.eadminmail.place(x=170,y=380)

        self.eadminpass = Entry(master)
        self.eadminpass.place(x=170,y=420)

        self.eusermail = Entry(master)
        self.eusermail.place(x=170,y=80)

        self.emovie1 =Entry(master)
        self.emovie1.place(x =170,y=120)

        self.emovie2 =Entry(master)
        self.emovie2.place(x =170,y=160)

        self.emovie3 =Entry(master)
        self.emovie3.place(x =170,y=200)

        self.emovie4 =Entry(master)
        self.emovie4.place(x =170,y=240)

        self.savedata = Button(master, text='Save Data', height=1, width=15, bg='light green',
                                command=self.save_data)
        self.savedata.place(x=170, y=280)

        self.sendmail = Button(master, text='Send mail', height=1, width=15, bg='light green',
                                command=self.mail_send)
        self.sendmail.place(x=170, y=520)

        
        


    def save_data(self):
        
            self.v1 = self.eusermail.get()
            self.v2 = self.emovie1.get()
            self.v3 = self.emovie2.get()
            self.v4 = self.emovie3.get()
            self.v5 = self.emovie4.get()
            

            if self.v1=='' or self.v2=='' or self.v3==' ' or self.v4=='' or self.v5=='' :
                tkinter.messagebox.showinfo('Warning','Please fill all the entries.  ')

            else:

                sql2 = 'insert into userinput (email,movie1,movie2,movie3,movie4) values(%s,%s,%s,%s,%s);'
                mydb.execute(sql2, (self.v1, self.v2, self.v3, self.v4, self.v5))
                
                conn.commit()

                tkinter.messagebox.showinfo('submitted', str(self.v1) + ' info successfully submitted')

    def mail_send(self):

            self.s1 = self.eadminmail.get()
            self.s2 = self.eadminpass.get()
            self.s3 = self.emailto.get()

            s='select movie1,movie2,movie3,movie4 from userinput where email like %s;'
            mydb.execute(s,(self.s3,))
            self.r=mydb.fetchall();

            for self.i in self.r:
                self.mov1=self.i[0]
                self.mov2=self.i[1]
                self.mov3=self.i[2]
                self.mov4=self.i[3]

            self.subject = 'TV series reminder'
            self.msg =( 'hi latest tv series upates ,\n' +str(self.mov1)+ ':  new session starts on 02 december 2018 \n        ends on 18 march 2019 \n\n'
                         + str(self.mov2)+ ':  new session starts on 12 october 2019 \n        ends on 11 april 2020 \n\n'
                         + str(self.mov3)+ ':  new session starts on 27 december 2018 \n        ends on 14 august 2020 \n\n'
                         + str(self.mov4)+ ':  new session starts on 22 july 2019 \n         ends on 18 may 2020 \n\n')

 


            try:
               self.server = self.smtplib.SMTP('smtp.gmail.com:587')
               self.server.ehlo()
               self.server.starttls()
               self.server.login('ahad.jnv@gmail.com','khan#200')
               self.message='Subject: {}\n\n{}'.format(self.subject,self.msg)
               self.server.sendmail('ahad.jnv@gmail.com','ahadkhan.jmi@gmail.com',self.message)
               self.server.quit()
               print("Success:Email send!")
        except:
              
              print("Email failed to send!")

               

root = Tk()

a=myapplication(root)

root.mainloop()





