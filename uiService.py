from tkinter import *
from tkinter import ttk

from sqlalchemy import MetaData
from sqlalchemy import text
from sqlalchemy_utils import drop_database

import sqlService
import pymysql

def delete_row():
    selectedItem = tab.focus()
    selectedItem = list(tab.item(selectedItem)['values'])

    table = meta.tables[choose.get()]

    columns = list(table.columns.keys())
    delete_string = ""

    for i in range(0, len(columns)):
        delete_string += columns[i] + "='" + str(selectedItem[i]) + "' AND "

    delete_string = delete_string[0:len(delete_string) - 4]
    print(delete_string)

    query = table.delete().where(text(delete_string))
    result = conn.execute(query)

    on_select()

def clear_db():
    table = meta.tables[choose.get()]
    query = table.delete()
    result = conn.execute(query)
    on_select()

def add_row():
    def add_query():
        add_list = []

        keys = entries.keys()
        for col in keys:
            add_list.append(str(entries[col].get()))

        query = table.insert().values(tuple(add_list))
        result = conn.execute(query)

        on_select()
        add.destroy()

    add = Tk()
    add.title("Add")
    table = meta.tables[choose.get()]

    entries = {}
    table_cols = table.columns.keys()

    red = 0
    for col in table_cols:
        label = Label(add, text=col, width=20)
        label.grid(row=red, column=0)

        entries[col] = Entry(add, width=30)
        entries[col].grid(row=red, column=1)

        red += 1

    add_b = Button(add, text="Add", command=add_query, width=10)
    add_b.grid(row=red, column=0, columnspan=2, pady=5)

def edit_row():
    def edit_query():

        edit_values = []
        edit_where = ""

        for i in range(0, len(col)):
            edit_values.append(str(entries[col[i]].get()))
            edit_where += col[i] + "='" + str(selectedItem[i]) + "' AND "

        edit_where = edit_where[0:len(edit_where) - 4]

        query = table.update().where(text(edit_where)).values(tuple(edit_values))
        result = conn.execute(query)

        on_select()
        edit.destroy()

    edit = Tk()
    edit.title("Edit")

    selectedItem = tab.focus()
    selectedItem = list(tab.item(selectedItem)['values'])

    table = meta.tables[choose.get()]
    col = list(table.columns.keys())

    entries = {}

    for i in range(0, len(col)):
        label = Label(edit, text=col[i], width=20)
        label.grid(row=i, column=0)

        entries[col[i]] = Entry(edit, width=30)
        entries[col[i]].insert(0, str(selectedItem[i]))
        entries[col[i]].grid(row=i, column=1)

    edit_b = Button(edit, text="Save Editing", command=edit_query, width=10)
    edit_b.grid(row=len(col), column=0, columnspan=2, pady=5)

def del_button():
    re_button.destroy()
    on_select()

def delete_db():
    for tbl in reversed(meta.sorted_tables):
        engine.execute(tbl.delete())
    drop_database(engine.url)

def find_in():
    def show_find_query():
        query = f'''
        select *
        from {tabs}
        where {entries[0].get()}='{entries[1].get()}'
        '''

        result = conn.execute(query)
        iid_counter = 0
        for item in tab.get_children():
            tab.delete(item)

        for row in result:
            row = list(row)
            tab.insert(parent='', index='end', text="", iid=iid_counter, values=row)
            iid_counter += 1

        global re_button
        re_button = Button(option_frame, text="Return", command=del_button, width=10)
        re_button.pack(side=LEFT)

        find.destroy()

    find = Tk()
    find.title("Find")

    selectedItem = tab.focus()
    selectedItem = list(tab.item(selectedItem)['values'])

    tabs = meta.tables[choose.get()]
    entries = {}

    label = Label(find, text='field name', width=20)
    label.grid(row=0, column=0)
    entries[0] = Entry(find, width=30)
    entries[0].grid(row=0, column=1)

    label = Label(find, text='find', width=20)
    label.grid(row=1, column=0)
    entries[1] = Entry(find, width=30)
    entries[1].grid(row=1, column=1)

    edit_b = Button(find, text="Show", command=show_find_query, width=10)
    edit_b.grid(row=2, column=0, columnspan=2, pady=5)

def on_select(event=None):
    for item in tab.get_children():
        tab.delete(item)

    table = meta.tables[choose.get()]

    tab.heading("#0", text="")
    tab.column("#0", anchor=W, width=0)

    tab['columns'] = list(table.columns.keys())

    for col in list(table.columns.keys()):
        tab.column(col)
    for col in list(table.columns.keys()):
        tab.heading(col, text=col, anchor=W)

    iid_counter = 0
    result = conn.execute(table.select())
    for row in result:
        row = list(row)
        tab.insert(parent='', index='end', text="", iid=iid_counter, values=row)
        iid_counter += 1


## create db
engine = sqlService.create_db()
sqlService.add_Table()

pymysql.install_as_MySQLdb()

conn = engine.connect()
meta = MetaData(bind=conn)
meta.reflect()

## ui config
window = Tk()
window.title("Pockemons")
window.geometry("1300x500")

choose = StringVar()
choose.set(list(meta.tables.keys())[0])

option_frame = Frame(window)

option = OptionMenu(option_frame, choose, *list(meta.tables.keys()), command=on_select)
option.pack(side=LEFT)

## main buttons
add_button = Button(option_frame, text="Add", command=add_row, width=10)
add_button.pack(side=LEFT)

edit_button = Button(option_frame, text="Edit", command=edit_row, width=10)
edit_button.pack(side=LEFT)

delete_button = Button(option_frame, text="Delete", command=delete_row, width=10)
delete_button.pack(side=LEFT)

add_button = Button(option_frame, text="Clear all", command=clear_db, width=10)
add_button.pack(side=LEFT)

add_button = Button(option_frame, text="Find in", command=find_in, width=10)
add_button.pack(side=LEFT)

option_frame.pack(side=TOP)

## frame
tree_frame = Frame(window)

tab = ttk.Treeview(tree_frame)
tree_scroll_y = Scrollbar(window, orient=VERTICAL)
tree_scroll_x = Scrollbar(window, orient=HORIZONTAL)

tab.config(yscrollcommand=tree_scroll_y.set, xscrollcommand=tree_scroll_x.set)
tree_scroll_y.config(command=tab.yview)
tree_scroll_x.config(command=tab.xview)

tree_scroll_y.pack(side=RIGHT, fill=Y)
tree_scroll_x.pack(side=BOTTOM, fill=X)
tab.pack(fill=BOTH, expand=1)

tree_frame.pack(side=TOP, fill=BOTH, expand=1)

## app
on_select()
window.mainloop()

## delete db
delete_db()