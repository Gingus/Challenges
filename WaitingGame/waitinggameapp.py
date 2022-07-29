import pathlib
import tkinter as tk
import tkinter.ttk as ttk
import pygubu

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "waitingGame.ui"


class WaitinggameApp:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.mainwindow = builder.get_object('frame1', master)
        
        self.DisplayMessageOutput = None
        self.resultString = None
        builder.import_variables(self, ['DisplayMessageOutput', 'resultString'])
        
        builder.connect_callbacks(self)
    
    def run(self):
        self.mainwindow.mainloop()

    def start_stop_pressed(self):
        pass


if __name__ == '__main__':
    root = tk.Tk()
    app = WaitinggameApp(root)
    app.run()

