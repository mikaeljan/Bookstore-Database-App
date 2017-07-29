import tkinter
import back_end_script
window = tkinter.Tk()

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

title_text = tkinter.StringVar()
e1 = tkinter.Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text = tkinter.StringVar()
e1 = tkinter.Entry(window, textvariable=author_text)
e1.grid(row=0, column=3)

year_text = tkinter.StringVar()
e1 = tkinter.Entry(window, textvariable=year_text)
e1.grid(row=1, column=1)

isbn_text = tkinter.StringVar()
e1 = tkinter.Entry(window, textvariable=isbn_text)
e1.grid(row=1, column=3)

list1 = tkinter.Listbox(window,width=35, height=6)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

scrollbar1 = tkinter.Scrollbar(window)
scrollbar1.grid(row=2, column=2, rowspan=6)

list1.config(yscrollcommand=scrollbar1.set)
scrollbar1.config(command=list1.yview)

# Buttons
view_button = tkinter.Button(window, text='View All', width=12)
view_button.grid(row=2, column=3)

search_button = tkinter.Button(window, text='Search entry', width=12)
search_button.grid(row=3, column=3)

add_button = tkinter.Button(window, text='Add entry', width=12)
add_button.grid(row=4, column=3)

update_button = tkinter.Button(window, text='Update entry', width=12)
update_button.grid(row=5, column=3)

delete_button = tkinter.Button(window, text='Delete Entry', width=12)
delete_button.grid(row=6, column=3)

close_button = tkinter.Button(window, text='Close', width=12)
close_button.grid(row=7, column=3)


window.mainloop()