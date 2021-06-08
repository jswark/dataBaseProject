from tkinter import *
import tkinter.ttk as ttk


def App():

    class LogginFrame(Frame):
        def __init__(self, parent=None):
            super().__init__(parent)

            # Make login and password entry lines
            self.login = ttk.Combobox(self,
                                      values=('Lol', 'Alex', 'Bob'), width=70, justify='center')
            self.login.set('Alex')
            self.password = Entry(self, width=70, show="*")
            self.submit = Button(self, bg="red", fg="blue",
                           text="Login ot DB")

            # Pack all widgets
            self.login.pack()
            self.password.pack()
            self.submit.pack()

        def set_changer(self, view):
            self.submit.bind('<ButtonRelease-1>', FrameChanger(self, view))


    class Table:
        def __init__(self, parent, headings=tuple(), rows=tuple()):
            table = ttk.Treeview(parent, show="headings", selectmode="browse")
            table["columns"]=headings
            table["displaycolumns"]=headings

            for head in headings:
                table.heading(head, text=head, anchor=CENTER)
                table.column(head, anchor=CENTER)

            for row in rows:
                table.insert('', END, values=tuple(row))

            scrolltable = Scrollbar(parent, command=table.yview)
            table.configure(yscrollcommand=scrolltable.set)
            scrolltable.pack(side=RIGHT, fill=Y)
            table.pack(expand=YES, fill=BOTH)
            table.bind("<<TreeviewSelect>>", self.print_selection)
            self.table = table
            self.parent = parent

        def pack(self, *args, **kwargs):
            self.table.pack(*args, **kwargs)

        def print_selection(self, event):
            for selection in self.table.selection():
                item = self.table.item(selection)
                print(item["values"])

    class ViewFrame(Frame):
        def __init__(self, parent=None):
            super().__init__(parent)
            self.top_f = Frame(self)
            table_frame = Frame(self.top_f)
            right_frame = Frame(self.top_f)
            self.bottom_frame = Frame(self)

            table = Table(table_frame, headings=('aaa', 'bbb', 'ccc'), rows=((123, 456, 789), ('abc', 'def', 'ghk')))
            table.pack(expand=YES, fill=BOTH)



            b1 = Button(right_frame, bg="red", fg="blue",
                                   text="Change State!!!")
            b2 = Button(right_frame, bg="red", fg="blue",
                                   text="right Bottom button")
            b1.pack()
            b2.pack()

            table_frame.pack(expand=YES, fill=BOTH, side=LEFT)
            right_frame.pack(expand=YES, fill=BOTH, side=LEFT)

            self.b3 = Button(self.bottom_frame, bg="red", fg="blue",
                                   text="Bottom button")
            self.b3.pack(side=LEFT)
            self.top_f.pack()
            self.bottom_frame.pack()

        def set_changer(self, view):
            self.b3.bind('<ButtonRelease-1>', FrameChanger(self, view))


    def FrameChanger(forget, show):
        def changer(event):
            forget.pack_forget()
            show.pack()
        return changer

    root = Tk()
    loggin_f = LogginFrame(root)
    loggin_f.pack()

    view_f = ViewFrame(root)

    loggin_f.set_changer(view_f)
    view_f.set_changer(loggin_f)
    root.mainloop()

App()





# import tkinter as tk
# import tkinter.ttk as ttk
#
#
# class Table(tk.Frame):
#     def __init__(self, parent=None, headings=tuple(), rows=tuple()):
#         super().__init__(parent)
#
#         table = ttk.Treeview(self, show="headings", selectmode="browse")
#         table["columns"]=headings
#         table["displaycolumns"]=headings
#
#         for head in headings:
#             table.heading(head, text=head, anchor=tk.CENTER)
#             table.column(head, anchor=tk.CENTER)
#
#         for row in rows:
#             table.insert('', tk.END, values=tuple(row))
#
#         scrolltable = tk.Scrollbar(self, command=table.yview)
#         table.configure(yscrollcommand=scrolltable.set)
#         scrolltable.pack(side=tk.RIGHT, fill=tk.Y)
#         table.pack(expand=tk.YES, fill=tk.BOTH)
#         table.bind("<<TreeviewSelect>>", self.print_selection)
#         self.table = table
#
#     def print_selection(self, event):
#         for selection in self.table.selection():
#             item = self.table.item(selection)
#             print(item["values"])
#
#             # last_name, first_name, email = item["values"][0:3]
#             # text = "Выбор: {}, {} <{}>"
#             # print(text.format(last_name, first_name, email))
#
# root = tk.Tk()
# table = Table(root, headings=('aaa', 'bbb', 'ccc'), rows=((123, 456, 789), ('abc', 'def', 'ghk')))
# table.pack(expand=tk.YES, fill=tk.BOTH)
# root.mainloop()
