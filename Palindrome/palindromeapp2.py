import os
import tkinter as tk
# import tkinter.ttk as ttk
import pygubu
import sys

try:
    import tkinter as tk
    from tkinter import messagebox
except:
    import Tkinter as tk
    import tkMessageBox as messagebox

# PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
# PROJECT_UI = os.path.join(PROJECT_PATH, "Palindrome.ui")

sys.path.append(os.path.join(os.path.dirname(__file__), '../'))


class PalindromeApp2:
    """something"""
    def __init__(self):
        # self.master = master
        self.master = tk.Tk()
        self.builder = builder = pygubu.Builder()
        fpath = os.path.join(os.path.dirname(__file__), "Palindrome.ui")
        builder.add_from_file(fpath)
        mainwindow = builder.get_object('mainwindow', self.master)
        builder.connect_callbacks(self)
        self.check_button_pressed = False
        self.entryBoxVar = None
        builder.import_variables(self, ['label1', 'check_button', 'entryBox'])

        self.label_update = self.builder.get_object(self, 'label1').label_update()
        self.entryBoxVar = self.builder.get_object(self, 'entryBoxVar').entryBoxVar()
        self.master.mainloop()

    def reset_check_button(self):
        """Resets all button states"""
        self.check_button_pressed = False

    def check_val(self):
        """Compares val against rev_val"""
        palindrome = False
        val = self.entryBoxVar
        rev_val = self.entryBoxVar[::-1]
        if val == rev_val:
            palindrome = True
        else:
            self.reset_check_button()
            pass

        if palindrome:
            self.label_update = "Yep", val, ", that one is a palindrome!"
        else:
            self.label_update = "Nope", val, ", is not a palindrome!"
        print(palindrome)
        exit()

    def check_pressed(self):
        """When check_button_pressed is True,
        the entryBoxVar is checked
        """
        if not self.check_button_pressed:
            print("check_button_pressed = ", self.check_button_pressed)
        else:
            print(self.check_button_pressed)
    
    def quit(self):
        """To make destroy the root window and shut off the camera feed"""
        self.check_button_pressed = False
        print(self.check_button_pressed)
        # root.quit()
        self.master.quit()

    # def run(self):
    #     self.mainwindow.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    # app = PalindromeApp2(root)
    app = PalindromeApp2()
    app.quit()

