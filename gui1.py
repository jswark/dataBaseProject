from tkinter import *

def change():
    but2['text'] = 'Changed Second Button'
    but2['bg'] = '#000000'
    but2['fg'] = 'red'


def print_log():
    line = entry.get()
    print(f"FROM Entry: {line}")
    # entry
    entry.insert(END, "Our new line")
    entry.delete(0, END)



root = Tk()
root.title = 'Main'

# # buttons
# but1 = Button(text='Push me!', width=15, height=3)
# but2 = Button(text='Print entry', width=15, height=3, command=print_log)
# but1.config(command=change)
# # Labels
# l1 = Label(text='Gui for LAba', font='Arial 32')
# l2 = Label(text='AWEQWewqeqwe', font=('Arial', 32, 'bold'))
# l2.config(bg='#afaffa')
#
# # Entry
# entry = Entry(width=20)
#
#
# but1.pack(side=LEFT)
# but2.pack(side=LEFT)
#
# l1.pack(side=BOTTOM)
# l2.pack(side=TOP)
# entry.pack()
# # entry.pack_forget()
#
# # Radio and Check buttons
# radio = IntVar()
# radio.set(0)
# r1 = Radiobutton(text='First', variable=radio, value=0)
# r2 = Radiobutton(text='Second', variable=radio, value=1)
# r3 = Radiobutton(text='Third', variable=radio, value=2)
# ch1 = Checkbutton(text='Check1')
# ch2 = Checkbutton(text='Check2')
#
# r1.pack()
# r2.pack()
# r3.pack()
# ch1.pack()
# ch2.pack()


# listbox & scroolbar
lbox = Listbox(width=15, height=4) #selectmode=EXTENDED)
scrool = Scrollbar(command=lbox.yview)
lbox.config(yscrollcommand=scrool.set)

for i in ['one', 'two', 'tree', 'four', 'five', 'six', 'seven']:
    lbox.insert(0, i)
lbox.pack(side=LEFT)
scrool.pack(side=LEFT, fill=Y)

# combobox
from tkinter.ttk import Combobox
combo = Combobox(values=['one', 'two', 'tree', 'four', 'five', 'six', 'seven'])
combo.pack()

def lbox_selected(event):
    selected = lbox.get(ACTIVE)
    print(selected)
    combo.delete(0,END)
    combo.insert(0, selected)

lbox.bind('<Button-1>', lbox_selected)

def my_decorator(a):
    def print_a():
        print(a)
    return print_a

f2=my_decorator(2)
f5=my_decorator(5)
f8=my_decorator(6)
f2()
f5()
f8()


root.mainloop()
