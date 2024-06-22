from tkinter import *
import ctypes as ct

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

def translate():
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

root = Tk()
root.geometry("720x480")
root.resizable(False, False)
root.title("E-leet")
root.configure(bg="#242424")
dark_title_bar(root)

main_label = Label(root, font=("Arial", 18, 'bold'), text="Insert the words you want to translate: ",
                   bg="#242424", fg='white')
main_label.pack()

main_entry = Entry(root, font=("Helvetica", 18), width=35)
main_entry.pack(padx=10, pady=10)

submit_button = Button(root, font=('Arial', 14, 'bold'), text='Submit', width=14,
                       bg="green",
                       fg='white',
                       activebackground='darkgreen',
                       activeforeground='white',
                       command=translate)
submit_button.pack()

result_label = Label(root, font=('Helvetica', 24), bg='#242424', fg="white", wraplength=585)
result_label.pack()

root.mainloop()