from tkinter import *
from tkinter import ttk


win=Tk()
win.title("register")
win.geometry("%dx%d+%d+%d"%(550,400,460,100))
win.configure(bg="lightgreen")
users=[]

def onclickregister(e):
    dic={"name":txt_name.get(),"lastname":txt_lastname.get(),"age":int(txt_age.get())}
    register(dic)



def register(value):
    users.append(value)
    print(users)


def getselection()


txtnamevar=StringVar
txtlastnamevar=StringVar
txtagevar=StringVar


coulmn=("c1","c2","c3")
tbl_search=ttk.Treeview(win,columns=("c1","c2","c3"),show="headings")

tbl_search.heading("c1", text="name",)
tbl_search.column("c1",width=80)
tbl_search.heading("c2", text="lastname")
tbl_search.column("c2",width=80)
tbl_search.heading("c3", text="age")
tbl_search.column("c3",width=80)

tbl_search.bind("<Button-1>",getselection)

tbl_search.place(x=250,y=50)




#txt
txt_name=Entry(win,width=30)
txt_name.place(x=50,y=50)

txt_lastname=Entry(win,width=30)
txt_lastname.place(x=50,y=100)

txt_age=Entry(win,width=30)
txt_age.place(x=50,y=150)










#btn
btn_register=Button(win,text="Register",width=25)
btn_register.bind("<Button-1>",onclickregister)
btn_register.place(x=50,y=200)














win.mainloop()