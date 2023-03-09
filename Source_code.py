import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk #PIL -> Pillow
from tkinter import messagebox
import random
import mysql.connector
import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os.path
from os import path


#connecting to mysql
mydb = mysql.connector.connect(
host="localhost",
user="root",
passwd="user",
database="cqap")
mycursor = mydb.cursor()



 ##tab1
root = Tk()
root.title("CQA-1")
root.configure(bg="white")
root.geometry("2000x1000")
tc=ttk.Notebook(root)
34. tc.pack(pady=0,padx=0)
35. page0 = Frame(tc,width=1280,height=720)
36. page1 = Frame(tc,width=1280,height=720 )
37. page2 = Frame(tc,width=1280,height=720 )
38. page3 = Frame(tc,width=1280,height=720 )
39. page4 = Frame(tc,width=1280,height=720 )
40. page5 = Frame(tc,width=1280,height=720 )
41. page0.pack(expand = 1,fill="both")
42. page1.pack(expand = 1,fill="both")
43. page2.pack(expand = 1,fill="both")
44. page3.pack(expand = 1,fill="both")
45. page5.pack(expand = 1,fill="both")
46. tc.add(page0 , text='WELCOME')
tc.add(page1 , text='REGISTER')
tc.add(page2 , text='GENERAL')
tc.add(page3 , text='RESULT-DAY3')

tc.add(page4 , text='RESULT-DAY5')
tc.add(page5 , text='RESULT-DAY5')
tc.hide(1)
tc.hide(2)
tc.hide(3)
tc.hide(4)
tc.hide(5)


canvas = tk.Canvas(page0, width=1280, height=720)
canvas.grid()
back=Image.open("welcome.jpeg")
resize=back.resize((800,690),Image.ANTIALIAS)
new=ImageTk.PhotoImage(resize)
canvas.create_image(400,360,image=new)
back1=Image.open("logo.png")
resize=back1.resize((400,450),Image.ANTIALIAS)
new1=ImageTk.PhotoImage(resize)

canvas.create_image(1100,160,image=new1)

noaccount=tk.Label(page0,fg="black",text="OR",bg="white",font="CaviarDreams 20 bold ").place(x=1080,y=550)

user=tk.Label(page0,fg="black",text=" User ID :",font="CaviarDreams 10 bold ").place(x=860,y=400)
user1_e=tk.Entry(page0,width=45,font="CaviarDreams 10 bold ",bg="white",borderwidth=3)
user1_e.place(x=950,y=400)

pwd=tk.Label(page0,fg="black",text="   Enter Password: ",font="CaviarDreams 10bold").place(x=810,y=440)
pwd1_e=tk.Entry(page0,width=45,font="CaviarDreams 10 bold ",bg="white",borderwidth=3,show="*")
pwd1_e.place(x=950,y=440)
###############################################################################

global t1 
t1=user1_e.get() 
def select1():
  tc.select(1)
  tc.hide(0) 
def select2():
  tc.select(2)
  tc.hide(1)
  tc.hide(0)
  def day_no_check():
    global day_count
    if path.exists(filename)==False:
      day_count='Welcome to day 1'
    else:
      global pre_stats_rows pre_stats_rows=[]
      with open(filename, 'r') as file:
        reader = csv.reader(file) 
        for row in reader:
          pre_stats_rows.append(row) 
        if len(pre_stats_rows)==4:
          day_count='Welcome to day 2' 
          elif len(pre_stats_rows)==8:
            day_count='Welcome to day 3'
          elif len(pre_stats_rows)==12:
             day_count='Welcome to day 4' 
          elif len(pre_stats_rows)==16:
             day_count='Welcome to day 5'
          else:
              day_count= 'Day Count Limit Reached'
          gnqu=tk.Label(page2,fg="red",text=day_count,bg="white",font="Georgia 15 bold italic").place(x=560,y=15)

day_no_check() 

##login
def login():
  global t1
  t1=user1_e.get()
  global t2
  t2=pwd1_e.get()
  global filename
  filename = t1+"_"+"daily_stats.csv"
  if t1=="" or t2=="":
    messagebox.showinfo('Error',"Please fill all fields") 
    return


  def username_check():
    mycursor.execute("select username from users")
    tab=mycursor.fetchall()
    u=[]
    for i in tab:
      u.append(i[0]) 
    for z in u:
      if z==t1:
        return True
     else:
        messagebox.showinfo('Error',"Incorrect UserID")
  
  
  
  pwd_check=True
  if username_check()==True:
    mycursor.execute("select pwd from users where username = '" + t1 + "' ") ##gives form 't1'
    tab1=mycursor.fetchall()
    for j in tab1:
      if j[0]==t2: 
        select2()
     else:
      pwd_check=False
   if pwd_check==False: 
    messagebox.showinfo('Error',"Incorrect password")
  
  

### button from login to question
##need to add if condition to check if user id matches database
  weltoque_but1=Image.open("login.png")
  resize=weltoque_but1.resize((120,50),Image.ANTIALIAS)
  ne47=ImageTk.PhotoImage(resize)
  welqnext_but1=tk.Button(page0,bg="white",image=ne47,command=login,borderwidth=0)
  welqnext_but1.place(x=1050,y=474) 161.

  #own create button
  myimgnext_but1=Image.open("register.png")
  resize=myimgnext_but1.resize((120,50),Image.ANTIALIAS)
  ne44=ImageTk.PhotoImage(resize)
  next_but1=tk.Button(page0,bg="white",image=ne44,command=select1,borderwidth=0)
  next_but1.place(x=1050,y=600)
  
  
  
########################################################################################################################


def variables():
  global n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15,n16,n17,n18,n19,n20,lpg1,lpg2,n19,n20
  n1=name_e.get()
  n2=username_e.get()
  n3=pwd_e.get()
  n4=cpwd_e.get()
  n5=varg.get()
  n6=ph_e.get()
  n7=email_e.get()
  n8=age_e.get()
  n9=address_e.get('1.0',END)
  n10=pr1_e.get()
  n11=pr1e_e.get()
  n12=pr2_e.get()
  n13=pr2e_e.get()
  n14=pr3_e.get()
  n15=pr3e_e.get()
  n16=md_e.get()
  n17=click.get()
  n18=allr_e.get()
  n19=vart.get()
  n20=sptr_e.get()
  lpg1=[n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15,n16,n17,n18,n19,n20]
  lpg2=[n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15,n17,n19]
  def exists_id():
    mycursor.execute("select username from users") tab=mycursor.fetchall()
    u=[]
    for i in tab:
      u.append(i[0]) if n2 in u:
      return True
    else:
      return False
  def exists_email():
    global n7
    mycursor.execute("select email from users")
    tab=mycursor.fetchall()
    u=[]
    for i in tab:
      u.append(i[0]) 
      if n7 in u:
        return True 
      else:
        return False
    
  def check(email):
    import re
    regex = '^[a-z0-9]+[.]?[a-z0-9]+[@]\w+[.]\w{2,3}$' 
    if(re.search(regex,email)):
      return True
    else:
      return False
  def validate():
    
