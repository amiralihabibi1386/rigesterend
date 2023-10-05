from tkinter import *
from tkinter import messagebox


users=[]

def showmsg():

        win=Tk()
        win.title("Sing up")
        win.geometry("%dx%d+%d+%d"%(460,400,500,70))
        win.configure(bg="#8ECDDD")
        win.iconbitmap(r'C:\Users\ParsArgham\PycharmProjects\RGISTER\icon\register_login_signup_icon_219991.ico')


        def singup(e):
            b=False
            for item in users:
                if item["user"]==txt_user.get():
                    messagebox.showinfo("","تکراری")
                    b=True
                    break
            if b==False:
                if txt_password.get()==txt_repassword.get():
                    dic={"user":txt_user.get(),"password":txt_password.get()}
                    users.append(dic)
                    win.destroy()
                else:
                    messagebox.showwarning("Error","Please check the password")

        #frame
        frame1 = Frame(win, width=248, height=385,bg="#F0F0F0")
        frame1.place(x=205, y=8)

        ##txt
        txt_user = Entry(frame1, width=21,border=0,bg="#F0F0F0",font=20)
        txt_user.place(x=15, y=100)
        Frame(frame1, width=200, height=1, bg="blue").place(x=10, y=130)

        txt_password = Entry(frame1, width=21, border=0,bg="#F0F0F0",font=20)
        txt_password.place(x=15, y=170)
        Frame(frame1, width=200, height=1, bg="blue").place(x=10, y=200)

        txt_repassword=Entry(frame1,width=21,border=0,bg="#F0F0F0",font=20)
        txt_repassword.place(x=15,y=240)
        Frame(frame1, width=200, height=1, bg="blue").place(x=10, y=270)

        #lbl
        lbl_user = Label(frame1, text="User", foreground="#3085C3")
        lbl_user.place(x=15, y=75)

        lbl_password = Label(frame1, text="Password", foreground="#3085C3")
        lbl_password.place(x=15, y=145)

        lbl_repassword = Label(frame1, text="Repassword", foreground="#3085C3")
        lbl_repassword.place(x=15, y=215)

        lbl_frame = Label(frame1, text="Welcome to login !", foreground="#3085C3", font=30)
        lbl_frame.place(x=10, y=10)

        lbl_1 = Label(win, text="if you have already register click ", bg="#8ECDDD")
        lbl_1.place(x=10, y=50)

        lbl_1 = Label(win, text="on login and if you haven't", bg="#8ECDDD")
        lbl_1.place(x=10, y=70)

        lbl_1 = Label(win, text="registered click on singup  you ", bg="#8ECDDD")
        lbl_1.place(x=10, y=90)

        lbl_1 = Label(win, text="after login go to register  page", bg="#8ECDDD")
        lbl_1.place(x=10, y=110)

        lbl_1 = Label(win, text="and enter your information", bg="#8ECDDD")
        lbl_1.place(x=10, y=130)

        lbl_1 = Label(win, text="Welcome !", bg="#8ECDDD", font=30)
        lbl_1.place(x=10, y=10)

        #btn
        btn_singup=Button(frame1,text="sing up",width=25,bg="blue",foreground="white",relief="ridge",border=0)
        btn_singup.bind("<Button-1>",singup)
        btn_singup.place(x=15,y=320)











        win.mainloop()