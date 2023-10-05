import os
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


win=Tk()

win.title("REGISTER")
win.geometry("%dx%d+%d+%d"%(900,600,200,70))
win.configure(bg="#8ECDDD")
win.iconbitmap(r'C:\Users\ParsArgham\PycharmProjects\RGISTER\icon\register_login_signup_icon_219991.ico')
load1 = PhotoImage(file=r"C:\Users\ParsArgham\PycharmProjects\RGISTER\photo1\photo_2023-09-24_17-22-53.png")
Label(win, image= load1).pack()
users=[]

#def
def onclickregister(e):
    if  btn_rgister.cget("state")==NORMAL:
        try:
            dic={"name":txt_name.get(),"lastname":txt_lastname.get(),"age":int(txt_age.get()),"number":int(txt_number.get()),"email":txt_email.get(),"password":txt_password.get(),"natiol_code":int(txt_natiol.get())}
            if exist(dic)==False:
                load()
                register(dic)
                insert(dic)
                txt_name.focus_set()
                txtnamevar.set("")
                txtlastnamevar.set("")
                txtagevar.set("")
                txtnumbervar.set("")
                txtemailvar.set("")
                txtpassword.set("")
                txtnatiolvar.set("")


            else:
                messagebox.showwarning("Rep","فرد تکراری میاشد")
        except:
            messagebox.showwarning("Error","خطایی رخ داده است")



#def
def register(vlue):
    users.append(vlue)


def insert(value):
    tbl_search.insert('',"end",values=[value["name"],value["lastname"],str(value["age"]),str(value["number"]),value["email"],value["password"],int(value["natiol_code"])])

def activebtn(e):
    if txt_name.get()=="":
        btn_rgister.configure(state=DISABLED)
    else:
       btn_rgister.configure(state=NORMAL)



def getselection(e):
    selection=tbl_search.selection()
    if selection!=():
        s=tbl_search.item(selection)["values"]
        txtnamevar.set(s[0])
        txtlastnamevar.set(s[1])
        txtagevar.set(s[2])
        txtnumbervar.set(s[3])
        txtemailvar.set(s[4])
        txtpassword.set(s[5])
        txtnatiolvar.set(s[6])

def onclicksearch(e):
    search1=txt_search.get()
    result=search(search1)
    clear()
    for item in result:
        insert(item)

def search(value):
    resultlist = []
    for item in users:
        if item["name"] == txt_search.get() or item["lastname"] == txt_search.get() or str(item["age"]) == txt_search.get() or str(item["number"])==txt_search or item["email"]==txt_search or item["password"]==txt_search or str(item["natiol_code"])==txt_search:
            resultlist.append(item)
    return resultlist

def clear():
    for item in tbl_search.get_children():
        sel=str(item,)
        tbl_search.delete(sel)


def load_and_clear(value):
    for item in tbl_search.get_children():
        sel=str(item,)
        tbl_search.delete(sel)
    for item in  value:
        tbl_search.insert('',"end",values=[value["name"],value["lastname"],str(value["age"]),str(value["number"]),value["email"],value["password"],str(value["natiol_code"])])


def exist(value):
    for item in users:
       if item["name"]==value["name"] and item["lastname"]==value["lastname"] and item["age"]==value["age"] and item["number"]==value["number"] and item["email"]==value["email"] and item["password"]==value["password"] and item["natiol_code"]==value["natiol_code"]:
            return True
    return False

def onclickdelet(e):
    dialog= messagebox.askyesno("","ایا از حذف کاربر اطمینان دارید؟")

    if dialog==True:
        dic={"name":txt_name.get(),"lastname":txt_lastname.get(),"age":int(txt_age.get()),"number":txt_number.get(),"email":txt_email.get(),"password":txt_password.get(),"natiol_code":txt_natiol.get()}
        delet(dic)
        remove_tbl()
def delet(value):
    for item in users:
        if item["name"]==value["name"] and item["lastname"]==value["lastname"] and item["age"]==value["age"] and item["number"]==value["number"] and item["email"]==value["email"] and item["password"]==value["password"] and item["natiol_code"]==value["natiol_code"]:
            users.remove(value)

def remove_tbl():
    selection = tbl_search.selection()
    if selection != ():
         tbl_search.delete(selection)





def onclickupdate(e):
    select=tbl_search.selection()
    if select!=():
        select_item=tbl_search.item(select)["values"]
        dic={"name":select_item[0],"lastname":select_item[1],"age":int(select_item[2]),"number":int(select_item[3]),"email":select_item[4],"password":select_item[5],"natiol_code":int(select_item[6])}
        index1=update(dic)
        p=users[index1]
        tbl_search.item(select,values=[p["name"],p["lastname"],p["age"],p["number"],p["email"],p["password"],p["natiol_code"]])


def update(value):
    index=users.index(value)
    users[index]={"name":txt_name.get(),"lastname":txt_lastname.get(),"age":int(txt_age.get()),"number":int(txt_number.get()),"email":txt_email.get(),"password":txt_password.get(),"natiol_code":int(txt_natiol.get())}
    return index

def load():
    clear()
    for item in users:
        insert(item)




def test3(e):
    win.destroy()


#var
txtnamevar=StringVar()
txtlastnamevar=StringVar()
txtagevar=StringVar()
txtsearchvar=StringVar()
txtnumbervar=StringVar()
txtemailvar=StringVar()
txtpassword=StringVar()
txtnatiolvar=StringVar()



#txt
txt_name=Entry(win,width=30,textvariable=txtnamevar,border=0)
txt_name.bind("<KeyRelease>",activebtn)
txt_name.place(x=100,y=60)

txt_lastname=Entry(win,width=30,textvariable=txtlastnamevar,border=0)
txt_lastname.place(x=100,y=120)

txt_age=Entry(win,width=30,textvariable=txtagevar,border=0)

txt_age.place(x=100,y=180)

txt_number=Entry(win,width=30,textvariable=txtnumbervar,border=0)

txt_number.place(x=100,y=240)

txt_email=Entry(win,width=30,textvariable=txtemailvar,border=0)

txt_email.place(x=100,y=300)

txt_password=Entry(win,width=30,textvariable=txtpassword,border=0)

txt_password.place(x=100,y=360)


txt_natiol=Entry(win,width=30,textvariable=txtnatiolvar,border=0)

txt_natiol.place(x=100,y=420)

txt_search=Entry(win,width=20)
txt_search.place(x=700,y=30)

#lbl
lbl_name=Label(win,text="Name :",bg="#8ECDDD",font=30)
lbl_name.place(x=1,y=60)

lbl_lastname=Label(win,text="Last name :",bg="#8ECDDD",font=30)
lbl_lastname.place(x=1,y=120)

lbl_age=Label(win,text="Age :",bg="#8ECDDD",font=30)
lbl_age.place(x=1,y=180)

lbl_number=Label(win,text="Number :",bg="#8ECDDD",font=30)
lbl_number.place(x=1,y=240)

lbl_email=Label(win,text="email :",bg="#8ECDDD",font=30)
lbl_email.place(x=1,y=300)

lbl_password=Label(win,text="password :",bg="#8ECDDD",font=30)
lbl_password.place(x=1,y=360)

lbl_search=Label(win,text="Search",bg="#8ECDDD",)
lbl_search.place(x=650,y=30)

lbl_natiol=Label(win,text="natiol :",bg="#8ECDDD",font=30)
lbl_natiol.place(x=1,y=420)

#BTN
btn_rgister=Button(win,text="Rgister",width=25,border=0,bg="#8ECDDD")
btn_rgister.configure(state=DISABLED)
btn_rgister.bind("<Button-1>",onclickregister)
btn_rgister.place(x=100,y=470)

btn_search=Button(win,text="Search",width=5,bg="#8ECDDD")
btn_search.bind("<Button-1>",onclicksearch)
btn_search.place(x=830,y=30)

btn_delet=Button(win,text="delet",width=25,border=0,bg="#8ECDDD")
btn_delet.bind("<Button-1>",onclickdelet)
btn_delet.place(x=100,y=510)

btn_update=Button(win,text="Update",width=25,border=0,bg="#8ECDDD")
btn_update.bind("<Button-1>",onclickupdate)
btn_update.place(x=100,y=550)

#tbl
column=("c1","c2","c3")
tbl_search=ttk.Treeview(win,columns=("c1","c2","c3","c4","c5","c6","c7"),show="headings",height=24,)


tbl_search.heading("c1", text="name")
tbl_search.column("c1",width=80)
tbl_search.heading("c2", text="lastname")
tbl_search.column("c2",width=80)
tbl_search.heading("c3", text="age")
tbl_search.column("c3",width=80)
tbl_search.heading("c4", text="number")
tbl_search.column("c4",width=80)
tbl_search.heading("c5", text="email")
tbl_search.column("c5",width=80)
tbl_search.heading("c6", text="password")
tbl_search.column("c6",width=80)
tbl_search.heading("c7", text="natiol_code")
tbl_search.column("c7",width=80)

tbl_search.bind("<Button-1>",getselection)

tbl_search.place(x=320,y=60)



#menu
menu1 = Menu(win)

menubar = Menu(win,tearoff=0)

menubar.add_command(label="Exit",command=test3,foreground="red")
menu1.add_cascade(label="Menu",menu=menubar)

win.config(menu=menu1)


























win.mainloop()