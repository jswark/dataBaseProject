from tkinter import *
from tkinter import ttk

from sqlalchemy import create_engine

from sqlalchemy import MetaData, Table
from sqlalchemy import text
import pymysql

pymysql.install_as_MySQLdb()

engine = create_engine('postgresql://jswark:12345@localhost/pockemons', echo=True)
conn = engine.connect()
meta = MetaData(bind=conn)
meta.reflect()


################################################################################################
################################################################################################
################################################################################################

def delete_row():
    selectedItem = tab.focus()
    selectedItem = list(tab.item(selectedItem)['values'])

    tablica = meta.tables[odabir.get()]

    stupci = list(tablica.columns.keys())
    delete_string = ""

    for i in range(0, len(stupci)):
        if (stupci[i] == "jmbag" or stupci[i] == "jmbagStudent"):
            selectedItem[i] = str(selectedItem[i]).zfill(10)
        elif (stupci[i] == "jmbg" or stupci[i] == "jmbgNastavnik"):
            selectedItem[i] = str(selectedItem[i]).zfill(13)
        elif (stupci[i] == "oib" or stupci[i] == "oibUstanova"):
            selectedItem[i] = str(selectedItem[i]).zfill(11)
        else:
            delete_string += stupci[i] + "='" + str(selectedItem[i]) + "' AND "

    # Brise zadnji AND
    delete_string = delete_string[0:len(delete_string) - 4]
    print(delete_string)

    query = tablica.delete().where(text(delete_string))
    result = conn.execute(query)

    on_select()


# --------------------------------------------------------------------
def add_row():
    #####################################
    def add_query():
        add_list = []

        keys = entries.keys()
        for stupac in keys:
            if (stupac == "jmbag" or stupac == "jmbagStudent"):
                add_list.append(str(entries[stupac].get()).zfill(10))
            elif (stupac == "jmbg" or stupac == "jmbgNastavnik"):
                add_list.append(str(entries[stupac].get()).zfill(13))
            elif (stupac == "oib" or stupac == "oibUstanova"):
                add_list.append(str(entries[stupac].get()).zfill(11))
            else:
                add_list.append(str(entries[stupac].get()))

        query = tablica.insert().values(tuple(add_list))
        result = conn.execute(query)

        on_select()
        add.destroy()

    #####################################

    add = Tk()
    add.title("Add")
    tablica = meta.tables[odabir.get()]

    entries = {}
    stupciTablice = tablica.columns.keys()

    red = 0
    for stupac in stupciTablice:
        label = Label(add, text=stupac, width=20)
        label.grid(row=red, column=0)

        entries[stupac] = Entry(add, width=30)
        entries[stupac].grid(row=red, column=1)

        red += 1

    add_b = Button(add, text="Add", command=add_query, width=10)
    add_b.grid(row=red, column=0, columnspan=2, pady=5)


# --------------------------------------------------------------------
def edit_row():
    #####################################
    def edit_query():

        edit_values = []
        edit_where = ""

        for i in range(0, len(stupci)):

            if (stupci[i] == "jmbag" or stupci[i] == "jmbagStudent"):
                edit_values.append(str(entries[stupci[i]].get()).zfill(10))
                edit_where += stupci[i] + "='" + str(selectedItem[i]).zfill(10) + "' AND "

            elif (stupci[i] == "jmbg" or stupci[i] == "jmbgNastavnik"):
                edit_values.append(str(entries[stupci[i]].get()).zfill(13))
                edit_where += stupci[i] + "='" + str(selectedItem[i]).zfill(13) + "' AND "

            elif (stupci[i] == "oib" or stupci[i] == "oibUstanova"):
                edit_values.append(str(entries[stupci[i]].get()).zfill(11))
                edit_where += stupci[i] + "='" + str(selectedItem[i]).zfill(11) + "' AND "

            else:
                edit_values.append(str(entries[stupci[i]].get()))
                edit_where += stupci[i] + "='" + str(selectedItem[i]) + "' AND "

        edit_where = edit_where[0:len(edit_where) - 4]

        query = tablica.update().where(text(edit_where)).values(tuple(edit_values))
        result = conn.execute(query)

        on_select()
        edit.destroy()

    #####################################

    edit = Tk()
    edit.title("Edit")

    selectedItem = tab.focus()
    selectedItem = list(tab.item(selectedItem)['values'])

    tablica = meta.tables[odabir.get()]
    stupci = list(tablica.columns.keys())
    delete_string = ""

    entries = {}

    for i in range(0, len(stupci)):
        if (stupci[i] == "jmbag" or stupci[i] == "jmbagStudent"):
            selectedItem[i] = str(selectedItem[i]).zfill(10)
        elif (stupci[i] == "jmbg" or stupci[i] == "jmbgNastavnik"):
            selectedItem[i] = str(selectedItem[i]).zfill(13)
        elif (stupci[i] == "oib" or stupci[i] == "oibUstanova"):
            selectedItem[i] = str(selectedItem[i]).zfill(11)

        label = Label(edit, text=stupci[i], width=20)
        label.grid(row=i, column=0)

        entries[stupci[i]] = Entry(edit, width=30)
        entries[stupci[i]].insert(0, str(selectedItem[i]))
        entries[stupci[i]].grid(row=i, column=1)

    edit_b = Button(edit, text="Save Editing", command=edit_query, width=10)
    edit_b.grid(row=len(stupci), column=0, columnspan=2, pady=5)


# --------------------------------------------------------------------
def on_select(event=None):
    for item in tab.get_children():
        tab.delete(item)

    tablica = meta.tables[odabir.get()]

    tab.heading("#0", text="")
    tab.column("#0", anchor=W, width=0)

    tab['columns'] = list(tablica.columns.keys())

    for stupac in list(tablica.columns.keys()):
        tab.column(stupac)
    for stupac in list(tablica.columns.keys()):
        tab.heading(stupac, text=stupac, anchor=W)

    iid_counter = 0
    result = conn.execute(tablica.select())
    for row in result:
        row = list(row)
        tab.insert(parent='', index='end', text="", iid=iid_counter, values=row)
        iid_counter += 1


# ----------------------------------------------------------------------------------

window = Tk()
window.title("Pockemons")
window.geometry("1300x500")

odabir = StringVar()
odabir.set(list(meta.tables.keys())[0])

option_frame = Frame(window)

option = OptionMenu(option_frame, odabir, *list(meta.tables.keys()), command=on_select)
option.pack(side=LEFT)

add_button = Button(option_frame, text="Add", command=add_row, width=10)
add_button.pack(side=LEFT)

edit_button = Button(option_frame, text="Edit", command=edit_row, width=10)
edit_button.pack(side=LEFT)

delete_button = Button(option_frame, text="Delete", command=delete_row, width=10)
delete_button.pack(side=LEFT)

option_frame.pack(side=TOP)

# ----- Frame za tablicu -----
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

on_select()

window.mainloop()