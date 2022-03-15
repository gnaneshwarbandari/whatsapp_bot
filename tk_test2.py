from tkinter import *
from tkinter import filedialog
from wa import process
root = Tk()
root.title("WhatsApp Tool")
root.geometry('600x420')
canvas = Canvas(root, width = 200, height = 80)      
canvas.pack()
img = PhotoImage(file="smartinternz.png")      
canvas.create_image(0,10, anchor=NW, image=img)   

contact = ""
message = ""
attach = ""

def browsefunc():
    filename = filedialog.askopenfilename(filetypes=(("excel files","*.xlsx"),("All files","*.*")))
    cont.insert(END, filename) 
    print(filename)
    global contact
    contact = filename

def browsefunc1():
    filename1 = filedialog.askopenfilename(filetypes=(("All files","*.*"),("jpg files","*.jpg")))
    cont1.insert(END, filename1)
    print(filename1)
    global attach
    attach = filename1

def button_command():
    text = entry.get(1.0, "end-1c")
    print(text)
    message = text
    process(contact, attach, message)
    return None

File_In = Label(root, text="Contacts Excel File")
File_In.place(x=270, y=80)
File_In.pack()

cont = Entry(root, width=30)
cont.place(x=200, y=110)
cont.pack()

c1 = Button(root,text="Open",command=browsefunc)
c1.place(x=400, y=105)
c1.pack()

File_In1 = Label(root, text="Attachment")
File_In1.place(x=290, y=140)
File_In1.pack()

cont1 = Entry(root, width=30)
cont1.place(x=200, y=170)
cont1.pack()

c11 = Button(root,text="Open",command=browsefunc1)
c11.place(x=400, y=165)
c11.pack()

Message = Label(root, text="Message")
Message.place(x=290, y=200)
Message.pack()

entry = Text(root, width=30, height=5)
entry.place(x=200, y=230)
entry.pack()

n1 = Button(root, text="Submit", command = button_command)
n1.place(x=300, y=320)
n1.pack()

root.mainloop()
