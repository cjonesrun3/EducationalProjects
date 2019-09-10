from tkinter import *
from tkinter import messagebox

def not_waiting_for_button():
    messagebox.showerror('message', 'I launched when the script was loaded')

def waits_for_button():
    messagebox.showinfo('message', 'I waited until the button was pushed')

def waits_with_arguments(message):
    messagebox.showinfo('message', message)

root = Tk()

# no_wait_button will run as soon as the script loads because the parenthesis have been left in place.
no_wait_button = Button(text='No Waiting', command=not_waiting_for_button())

waiting_button = Button(text='Waiting', command=waits_for_button)  # No parenthesis stops function call

waiting_for_button_with_arguments = Button(text='Waiting with arguments', command=lambda: waits_with_arguments('word'))

no_wait_button.grid(column=0, row=0)
waiting_button.grid(column=0, row=1)
waiting_for_button_with_arguments.grid(column=0, row=2)

root.mainloop()