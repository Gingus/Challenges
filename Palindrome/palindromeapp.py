import pathlib
import tkinter as tk
# import tkinter.ttk as ttk
import pygubu

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "Palindrome.ui"


class PalindromeApp:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.mainwindow = builder.get_object('frame', master)
        
        self.resultLabelOutputOutput = None
        self.entry_value = None
        self.check_button_pressed = False
        builder.import_variables(self, ['resultLabelOutputOutput', 'entry_value', 'check_button_pressed'])
        
        builder.connect_callbacks(self)
        

    def check_val(self, entry_value, check_button_pressed, resultLabelOutput):
        """Compares val against rev_val"""
        self.entry_value = entry_value
        self.check_button_pressed = check_button_pressed
        self.resultLabelOutput = resultLabelOutput
        palindrome = False
        rev_entry_value = entry_value[::-1]
        if entry_value == rev_entry_value:
            palindrome = True
        else:
            pass

        if palindrome is True:
            resultLabelOutput == "Yep" + entry_value + ", that one is a palindrome!"
        else:
            resultLabelOutput == "Nope" + entry_value + ", is not a palindrome!"
        exit()

    def button_press(self, check_button_pressed):
        """_summary_
        """
        self.check_button_pressed = check_button_pressed
        ### See Video Affect > pictureaffectsapp.py
        # for the on/off code for button code
# asked = ask()
# # print(asked)
# check_val(asked)
# # print(check_val)
    
    def run(self):
        self.mainwindow.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    app = PalindromeApp(root)
    app.run()

