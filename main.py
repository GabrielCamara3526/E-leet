from tkinter import *

root = Tk()
root.geometry("720x480")
root.resizable(False, False)
root.title("E-leet")

main_label = Label(root, font=("Arial", 18, 'bold'), text="Insert the words you want to translate: ")
main_label.pack()

main_entry = Entry(root, font=("Helvetica", 18), width=35)
main_entry.pack(padx=10, pady=10)

submit_button = Button(root, font=('Arial', 14, 'bold'), text='Submit', width=14, bg="green", fg='white')
submit_button.pack()

root.mainloop()