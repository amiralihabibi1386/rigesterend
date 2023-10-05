import os
import tkinter
from tkinter import *
import singup
from tkinter import ttk
from tkinter import messagebox







win=Tk()
win.title("Log in")
win.geometry("%dx%d+%d+%d"%(460,400,500,70))
win.configure(bg="#8ECDDD")
win.iconbitmap(r'C:\Users\ParsArgham\PycharmProjects\RGISTER\icon\register_login_signup_icon_219991.ico')
load = PhotoImage(file=r"C:\Users\ParsArgham\PycharmProjects\RGISTER\photo\photo_2023-09-24_17-22-57.png")
Label(win, image=load).pack()

users=[]

def sing_up1(e):

    singup.showmsg()


def onclicklogin(e):
    result=login()
    if result:
        os.system(f"register.py")
    else:
        messagebox.showwarning("","خطایی در یوزر یا پسوورد رخ داده است")


def login():
    for item in singup.users:
        if item["user"]==txt_user.get() and item["password"]==txt_password.get():
            return True
    return False

def activeframe():
    frame.place(x=205,y=8)

def forget(e):
    win.destroy()



#frame
frame= Frame(win,width=248,height=385,bg="#F0F0F0")
frame.place(x=205,y=8)
frame.place_forget()




#txt
txt_user=Entry(frame,width=21,border=0,bg="#F0F0F0",font=20)
txt_user.place(x=15,y=100)
Frame(frame,width=200,height=1,bg="blue").place(x=10,y=130)

txt_password=Entry(frame,width=21,border=0,bg="#F0F0F0",font=20)
txt_password.place(x=15,y=170)
Frame(frame,width=200,height=1,bg="blue").place(x=10,y=200)



#lbl
lbl_user=Label(frame,text="User",foreground="#3085C3")
lbl_user.place(x=15,y=75)

lbl_password=Label(frame,text="Password",foreground="#3085C3")
lbl_password.place(x=15,y=145)


lbl_frame=Label(frame,text="Welcome to login !",foreground="#3085C3",font=30)
lbl_frame.place(x=10,y=10)

lbl_1=Label(win,text="if you have already register click ",bg="#8ECDDD")
lbl_1.place(x=10,y=50)

lbl_1=Label(win,text="on login and if you haven't",bg="#8ECDDD")
lbl_1.place(x=10,y=70)

lbl_1=Label(win,text="registered click on singup  you ",bg="#8ECDDD")
lbl_1.place(x=10,y=90)

lbl_1=Label(win,text="after login go to register  page",bg="#8ECDDD")
lbl_1.place(x=10,y=110)

lbl_1=Label(win,text="and enter your information",bg="#8ECDDD")
lbl_1.place(x=10,y=130)

lbl_1=Label(win,text="Welcome !",bg="#8ECDDD",font=30)
lbl_1.place(x=10,y=10)

lbl_1=Label(frame,text="Click to register!",bg="#F0F0F0",)
lbl_1.place(x=10,y=300)

lbl_2=Label(frame,text="Login",bg="#F0F0F0",foreground="blue")
lbl_2.bind("<Button-1>",sing_up1)
lbl_2.place(x=103,y=300)




#btn

btn_login=Button(frame,text="log in",width=25,bg="blue",foreground="white",relief="ridge",border=0)
btn_login.bind("<Button-1>",onclicklogin)
btn_login.place(x=15,y=250)

btn_login2=Button(win,text="Log in",command=activeframe,width=20,bg="#EBE4D1",relief="ridge",border=0,)
btn_login2.place(x=10,y=260)



btn_exit=Button(win,text="Exit",width=20,foreground="red",bg="#EBE4D1",relief="ridge",border=0,)
btn_exit.bind("<Button-1>",forget)
btn_exit.place(x=10,y=320)






win.mainloop()