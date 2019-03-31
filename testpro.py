import mysql.connector
import re
from tkinter import *
import tkinter.messagebox
import smtplib

from imdb import IMDb

conn= mysql.connector.connect(host="localhost" ,user="root",passwd="12345",database="tvseries")
mydb=conn.cursor()

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

        self.eadminpass = Entry(master,show ='*')
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

            
            imd = IMDb('http')
            tm1=self.mov1
            tm2=self.mov2
            tm3=self.mov3
            tm4=self.mov4
            sm1=imd.search_movie(tm1)[0]
            sm2=imd.search_movie(tm2)[0]
            sm3=imd.search_movie(tm3)[0]
            sm4=imd.search_movie(tm4)[0]
            print(sm1)
            print(sm2)
            print(sm3)
            print(sm4)
            movid1 = sm1.movieID
            movid2 = sm2.movieID
            movid3 = sm3.movieID
            movid4 = sm4.movieID

            imd.get_movie(movid1)
            imd.get_movie(movid2)
            imd.get_movie(movid3)
            imd.get_movie(movid4)

            imd.update(sm1,'episodes')
            imd.update(sm2,'episodes')
            imd.update(sm3,'episodes')
            imd.update(sm4,'episodes')
            xa=sorted(sm1['episodes'].keys())
            xb=sorted(sm2['episodes'].keys())
            xc=sorted(sm3['episodes'].keys())
            xd=sorted(sm4['episodes'].keys())
            ja=max(xa)
            jb=max(xb)
            jc=max(xc)
            jd=max(xd)
            sea1=sm1['episodes'][ja]
            sea2=sm2['episodes'][jb]
            sea3=sm3['episodes'][jc]
            sea4=sm4['episodes'][jd]
            la=len(sea1)
            lb=len(sea2)
            lc=len(sea3)
            ld=len(sea4)

            e1=sm1['episodes'][ja][la]
            e2=sm2['episodes'][jb][lb]
            e3=sm3['episodes'][jc][lc]
            e4=sm4['episodes'][jd][ld]
    

            self.data1=e1['long imdb canonical title']
            self.data2=e2['long imdb canonical title']
            self.data3=e3['long imdb canonical title']
            self.data4=e4['long imdb canonical title']
            self.spl1=self.data1.split('#')
            self.spl2=self.data2.split('#')
            self.spl3=self.data3.split('#')
            self.spl4=self.data4.split('#')
            
            print(self.spl1)
            print(self.spl2)
            print(self.spl3)
            print(self.spl4)


            self.subject = 'TV series reminder'
            self.msg =('Hi \n\nThere is latest tv series upates ,\n Status: \n'+str(self.spl1[0])+'  '+str(self.spl1[1])+ ': \n\n'
                         + str(self.spl2[0])+'  '+str(self.spl2[1])+ ':\n\n'
                         + str(self.spl3[0])+ '  '+str(self.spl3[1])+ ':  \n\n'
                         + str(self.spl4[0])+ '  '+str(self.spl4[1])+': \n\n')

            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(self.s1,self.s2)
            message='Subject: {}\n\n{}'.format(self.subject,self.msg)
            server.sendmail(self.s1,self.s3,message)
            server.quit()
            tkinter.messagebox.showinfo(' send','message successfully send.  ')
            print("Success:Email send!")
         
              

root = Tk()

a=myapplication(root)

root.mainloop()





