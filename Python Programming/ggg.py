from tkinter import *
root=Tk()
root.geometry("600x400")
root.title("CODEX CODER")
scvalue=StringVar()
scvalue.set("")
screen = Entry(root,textvar=scvalue,font="lucida 40 bold")
screen.pack()
f= Frame(root,bg="grey")
b=Button(f,text="9", font="lucida 35 bold")
b.pack()
f.pack()
c=Button(f,text="8", font="lucida 35 bold")
c.pack()
f.pack()
d=Button(f,text="7", font="lucida 35 bold")
d.pack()
f.pack()
e=Button(f,text="+", font="lucida 35 bold")
e.pack()
f.pack()
root.mainloop()




