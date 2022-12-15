from tkinter import *
from tkinter import filedialog, messagebox
import os

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("CSVapp")
        self.resizable(True, True)
        self.geometry('600x600')
        dir_button = Button(self, text="Choose Directory")
        dir_button.grid(row=0, column=0, sticky=NW)
        dir_button['command'] = self.choose_dir
        self.dir_label = Label(self, text='')
        self.dir_label.grid(row=0, column=1, sticky=NW)
        menubar = Menu(self)
        command_menu = Menu(menubar, tearoff=0)
        command_menu.add_command(label="Rename All", command=self.rename_all)
        menubar.add_cascade(label="Actions", menu=command_menu)
        self.config(menu=menubar)
        self.option_var = StringVar(self)
        
    def choose_dir(self):
        directory = filedialog.askdirectory()
        self.dir_label.config(text=directory)

    def rename_all(self):
        self.rename_label = Label(self, text='Rename all files to:')
        self.rename_label.grid(row=1, column=0)
        self.string_entry = Entry(self)
        self.string_entry.grid(row=1, column=1)
        self.append_label = Label(self, text='Append this number to first file:')
        self.append_label.grid(row=2, column=0)
        self.append_entry = Entry(self)
        self.append_entry.grid(row=2, column=1)
        self.increment_label = Label(self, text='Increment by:')
        self.increment_label.grid(row=3, column=0)
        self.numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.num_menu = OptionMenu(self, self.option_var, *self.numbers)
        self.num_menu.grid(row=3, column=1)
        rename_button = Button(self, text='Rename All')
        rename_button.grid(row=4, column=0)
        rename_button['command'] = self.rename_now
        help_button_1 = Button(self, text="Help")
        help_button_1.grid(row=4, column=1)
        help_button_1['command'] = self.help_message_1
        self.option_var.set('1')

    def rename_now(self):
        filename = self.string_entry.get()
        filepath = self.dir_label['text']
        os.chdir(filepath)
        num1 = int(self.append_entry.get())
        num2 = int(self.option_var.get())
        for file in os.listdir(filepath):
            file = filepath + '/' + file
            new_name = filepath + '/' + filename + str(num1) + '.csv'
            if '.csv' in file:
                os.rename(file, new_name)
                num1 += num2

    def help_message_1(self):
        messagebox.showinfo("About this command", "This feature will change the names of all csv files within the target directory. \n The new file name will be: \n Name + Number >> Name + Number + Increment for all other files \n Example: String1, String2, String3 (with increment of 1)")


if __name__ == '__main__':
    app = App()
    app.mainloop()
