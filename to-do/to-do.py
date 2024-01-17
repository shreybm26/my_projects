import tkinter
from tkinter import *

root=Tk()
root.title("To-Do")
root.geometry("400x650+400+100")
root.resizable(False,False)
icon=PhotoImage(file="randoms\codsoft\img\_task.png")
root.iconphoto(False,icon)

tsklst=[]
tskdone=[]

def addtsk():
    task=task_entry.get()
    task_entry.delete(0,END)

    if task:
        with open("tasklist.txt","a") as taskfile:
            taskfile.write(f"\n{task}")
        tsklst.append(task)
        listbox.insert(END,task)

def opentsk():
    try:
        global tsklst
        with open("tasklist.txt","r") as taskfile:
            tasks=taskfile.readlines()
        for tsk in tasks:
            if tsk!="\n":
                tsklst.append(tsk)
                listbox.insert(END, tsk)
    except:
        file=open('tasklist.txt','w')
        file.close()

def deltsk():
    global tsklst
    global tskdone
    task=str(listbox.get(ANCHOR))
    if task in tsklst:
        tsklst.remove(task)
        tskdone.append(task)
        with open("tasklist.txt",'w') as taskfile: 
            for task in tsklst:
                taskfile.write(task+"\n")
        listbox.delete(ANCHOR)

def completed():
    root2=Tk()
    root2.title("Completed Tasks")
    root2.geometry("400x650+400+100")
    root2.resizable(False,False)

    txt_output=Text(root2, bg="#32405b", width=400, height=50, fg="white", font="arial 12")
    txt_output.pack()
    txt_output.insert(END, "You have completed the following tasks: \n\n")

    for item in tskdone:
        txt_output.insert(END, item + "\n")

    root2.mainloop()


#-------------LAYOUT----------------

topimg=PhotoImage(file="randoms\codsoft\img\_topbar.png")
Label(root, image=topimg).pack()

dockimg=PhotoImage(file="randoms\codsoft\img\dock.png")
Label(root,image=dockimg, bg="#32405b").place(x=30,y=25)

noteimg=PhotoImage(file="randoms\codsoft\img\_task.png")
Label(root,image=noteimg, bg="#32405b").place(x=340,y=25)

heading=Label(root,text="YOUR TASKS", font="arial 20 bold", fg="white", bg="#32405b").place(x=100,y=20)

#--------------MAIN-----------------

frame=Frame(root, width=400,height=50,bg="white").place(x=0,y=180)

task=StringVar()
task_entry=Entry(frame,width=19,font="cambria 20", bd=0)
task_entry.place(x=0,y=185)
task_entry.focus()

btn=Button(frame, text="ADD", font="arial 20 bold", width=6, bg="#5a95ff", fg="#fff", bd=0,command=addtsk)
btn.place(x=300,y=180)

frame2=Frame(root,bd=3,width=700,height=280,bg="#32405b")
frame2.pack(pady=(160,0))

listbox=Listbox(frame2,font="arial 12",width=40,height=16,bg="#32405b",fg="white",cursor="hand2", selectbackground="#5a95ff")
listbox.pack(side=LEFT,fill=BOTH, padx=2)
scrollbar=Scrollbar(frame2)
scrollbar.pack(side=RIGHT,fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

opentsk()

#--------------DELETE------------
delico=PhotoImage(file="randoms\codsoft\img\delete.png")
Button(root,image=delico,bd=0,command=deltsk).pack(side=BOTTOM,pady=13)

#------------MENU TO SEE COMPLETED TASKS-----------
my_menu=Menu(root)
root.config(menu=my_menu)
options_menu=Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Completed tasks", command=completed)



root.mainloop()
