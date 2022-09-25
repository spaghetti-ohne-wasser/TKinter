#!/usr/bin/python3
from tkinter import *
from tkinter import ttk
from platform import system

if system() == "Windows":
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)

class MainWindow(Tk):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        
        self.resizable(width=False, height=False)
        self.title(string="Palindrom-Prüfer")
        self.configure(background="#323333")

        
        ttk.Label(master=self, text="Palindrom-Prüfer", background="#323333", foreground="#8e9397", font=("Microsoft Sans Serif", 16)).grid(row=0, column=0, padx=10, pady=10, sticky="W")

        self.text_field = Text(master=self, background="#222222", foreground="white")
        self.palindrom_label = ttk.Label(master=self, background="#323333", font=("Microsoft Sans Serif", 16))

        Button(master=self, text="Prüfung auf Palindromität", background="#4caf50", foreground="#fffffd", activebackground="#4caf50", activeforeground="#fffffd", command=self.palindrom).grid(row=2, column=0, sticky="W", padx=10, pady=10)

        self.text_field.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        self.palindrom_label.grid(row=2, column=1, sticky="W")
    
    def palindrom(self) -> None:
        text: str = self.text_field.get(index1=0.1, index2=END).strip().lower()
        if (text[::-1] == text):
            self.palindrom_label["foreground"] = "#4caf50"
            self.palindrom_label["text"] = "Es ist ein Palindrom!"
        else:
            self.palindrom_label["foreground"] = "#af504c"
            self.palindrom_label["text"] = "Tut mir leid, das ist kein Palindrom."

    
if __name__ == "__main__":
    try:
        MainWindow = MainWindow()
        MainWindow.mainloop()
    except KeyboardInterrupt:
        MainWindow.quit()
