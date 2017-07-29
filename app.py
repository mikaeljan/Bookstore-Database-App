import tkinter
import back_end_script

window = tkinter.Tk()

# Get index number from selected row from listbox
def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)

    e1.delete(0, tkinter.END)
    e1.insert(tkinter.END, selected_tuple[1])

    e2.delete(0, tkinter.END)
    e2.insert(tkinter.END, selected_tuple[1])

    e3.delete(0, tkinter.END)
    e3.insert(tkinter.END, selected_tuple[1])

    e4.delete(0, tkinter.END)
    e4.insert(tkinter.END, selected_tuple[1])
    return selected_tuple


def view_command():
    list1.delete(0, tkinter.END)
    for row in back_end_script.view():
        list1.insert(tkinter.END, row)


def search_command():
    list1.delete(0, tkinter.END)
    for row in back_end_script.search(title_text.get(),
                                      author_text.get(),
                                      year_text.get(),
                                      isbn_text.get()):
        list1.insert(tkinter.END, row)


def add_command():
    back_end_script.insert(title_text.get(),
                           author_text.get(),
                           year_text.get(),
                           isbn_text.get())
    list1.delete(0, tkinter.END)

    list1.insert(tkinter.END, (title_text.get(),
                 author_text.get(),
                 year_text.get(),
                 isbn_text.get()))


def delete_command():
    back_end_script.delete(selected_tuple[0])


def update_command():
    back_end_script.update(selected_tuple[0],
                           title_text.get(),
                           author_text.get(),
                           year_text.get(),
                           isbn_text.get()
                           )

# Labels for the window box

l1 = tkinter.Label(window, text='Title')
l1.grid(row=0,
        column=0)

l2 = tkinter.Label(window, text='Author')
l2.grid(row=0,
        column=2)

l3 = tkinter.Label(window, text='Year')
l3.grid(row=1,
        column=0)

l4 = tkinter.Label(window, text='ISBN')
l4.grid(row=1,
        column=2)

# Entry fields for the window box

title_text = tkinter.StringVar()
e1 = tkinter.Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text = tkinter.StringVar()
e2 = tkinter.Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text = tkinter.StringVar()
e3 = tkinter.Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text = tkinter.StringVar()
e4 = tkinter.Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

# List box + scrollbar for the window box

list1 = tkinter.Listbox(window,width=35, height=6)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

scrollbar1 = tkinter.Scrollbar(window)
scrollbar1.grid(row=2, column=2, rowspan=6)

list1.config(yscrollcommand=scrollbar1.set)
scrollbar1.config(command=list1.yview)

list1.bind("<<ListboxSelect>>", get_selected_row)


# Buttons

view_button = tkinter.Button(window,
                             text='View All',
                             width=12,
                             command=view_command)

view_button.grid(row=2, column=3)

search_button = tkinter.Button(window,
                               text='Search entry',
                               width=12,
                               command=search_command)

search_button.grid(row=3, column=3)

add_button = tkinter.Button(window,
                            text='Add entry',
                            width=12,
                            command=add_command)

add_button.grid(row=4, column=3)

update_button = tkinter.Button(window,
                               text='Update entry',
                               width=12,
                               command=update_command)

update_button.grid(row=5, column=3)

delete_button = tkinter.Button(window,
                               text='Delete Entry',
                               width=12,
                               command=delete_command)

delete_button.grid(row=6, column=3)

close_button = tkinter.Button(window,
                              text='Close',
                              width=12,
                              command=window.destroy)

close_button.grid(row=7, column=3)


window.mainloop()