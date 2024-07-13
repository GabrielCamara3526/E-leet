from tkinter import *
import ctypes as ct
import clipboard

leet_list = {("A", "a"): "4",
             ("E", "e"): "3",
             ("O", "o"): "0",
             ("L", "l"): "1",
             ("S", "s"): "5",
             ("Z", "z"): "2"}

def dark_title_bar(window):
    """
    MORE INFO:
    https://learn.microsoft.com/en-us/windows/win32/api/dwmapi/ne-dwmapi-dwmwindowattribute
    """
    window.update()
    set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
    get_parent = ct.windll.user32.GetParent
    hwnd = get_parent(window.winfo_id())
    value = 2
    value = ct.c_int(value)
    set_window_attribute(hwnd, 20, ct.byref(value), 4)

def translate(event=None):
    translated = ""
    entry_text = main_entry.get()
    for letter in entry_text:
        for key in leet_list:
            if letter in key:
                translated += leet_list[key]
                break
        else:
            translated += letter
    result_label.configure(text=translated)

def copy_to_clipboard():
    text_to_copy = result_label.cget("text")
    clipboard.copy(text_to_copy)
    copied_message.pack(side='bottom')
    root.after(2000, copied_message.pack_forget)

def clear_result_label():
    result_label.configure(text='')

root = Tk()
root.geometry("720x480")
root.resizable(False, False)
root.title("E-leet")
root.configure(bg="#242424")
dark_title_bar(root)

main_label = Label(root, font=("Arial", 18, 'bold'), text="Insert the words you will translate: ",
                   bg="#242424", fg='white')
main_label.pack()

main_entry = Entry(root, font=("Helvetica", 18), width=35, border=0)
main_entry.pack(padx=10, pady=10)
main_entry.bind('<Return>', translate)

top_btns = Frame(root)
top_btns.pack()

submit_button = Button(top_btns, font=('Arial', 14, 'bold'), text='Submit', width=14,
                       bg="green",
                       fg='white',
                       activebackground='darkgreen',
                       activeforeground='white',
                       command=translate)
submit_button.pack(side='left')

clear_result = Button(top_btns,  font=('Arial', 14, 'bold'), text='Clear Text', width=14,
                       bg="red",
                       fg='white',
                       activebackground='darkred',
                       activeforeground='white', command=clear_result_label)
clear_result.pack(side='right')

#The result label holds 215 characters before stretching too much
result_label = Label(root, font=('Helvetica', 24), bg='#242424', fg="white", wraplength=585)
result_label.pack(pady=10)

copied_message = Label(root, font=('Arial', 14), text='Successfully Copied!', bg='#242424', fg='white')

copy_button = Button(root, font=('Arial', 14, 'bold'), text='Copy to Clipboard', 
                     bg='purple', fg='white', activebackground='darkblue', activeforeground='white',
                     border=0, command=copy_to_clipboard)

copy_button.pack(side='bottom')

root.mainloop()
