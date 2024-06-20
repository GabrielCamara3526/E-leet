from tkinter import *
import ctypes as ct

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

root = Tk()
root.geometry("720x480")
root.resizable(False, False)
root.title("E-leet")
root.configure(bg="#242424")
dark_title_bar(root)

main_label = Label(root, font=("Arial", 18, 'bold'), text="Insert the words you want to translate: ", bg="#242424", fg='white')
main_label.pack()

main_entry = Entry(root, font=("Helvetica", 18), width=35)
main_entry.pack(padx=10, pady=10)

submit_button = Button(root, font=('Arial', 14, 'bold'), text='Submit', width=14, bg="green", fg='white')
submit_button.pack()

root.mainloop()