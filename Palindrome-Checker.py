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
        self.title(string="Palindrome Checker")
        self.configure(background="#323333")


        ttk.Label(master=self, text="Palindrome Checker", background="#323333", foreground="#8e9397", font=("Microsoft Sans Serif", 16)).grid(row=0, column=0, padx=10, pady=10, sticky="W")

        self.text_field = Text(master=self, background="#222222", foreground="white")
        self.palindrome_label = ttk.Label(master=self, background="#323333", font=("Microsoft Sans Serif", 16))

        Button(master=self, text="Check for palindrome-ness", background="#4caf50", foreground="#fffffd", activebackground="#4caf50", activeforeground="#fffffd", command=self.palindrome).grid(row=2, column=0, sticky="W", padx=10, pady=10)

        self.text_field.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        self.palindrome_label.grid(row=2, column=1, sticky="W")

    def palindrome(self) -> None:
        text: str = self.text_field.get(index1=0.1, index2=END).strip().lower()
        if (not bool(text)):
            self.palindrome_label["foreground"] = "#c4a747"
            self.palindrome_label["text"] = "Enter some alpha-numeric characters."
        elif (text[::-1] == text):
            self.palindrome_label["foreground"] = "#4caf50"
            self.palindrome_label["text"] = "It's a palindrome!"
        else:
            self.palindrome_label["foreground"] = "#af504c"
            self.palindrome_label["text"] = "Sorry, that's not a palindrome."

if __name__ == "__main__":
    try:
        MainWindow = MainWindow()
        MainWindow.mainloop()
    except KeyboardInterrupt:
        MainWindow.quit()    
