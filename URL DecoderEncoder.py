#!/usr/bin/python3
from tkinter import *
from tkinter import ttk
from platform import system
from urllib.parse import quote, unquote

if system() == "Windows":
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)

class MainWindow(Tk):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.configure(background="#337ab7")
        self.title(string="URL Decoder/Encoder")
        self.resizable(width=False, height=False)
        
        ttk.Label(master=self, text="URL Encode/Decode", background="#337ab7", font=("Helvetica", 18)).grid(row=0, column=0, sticky="W", pady=10, padx=10)
        
        self.input_field = Text(master=self, height=15)
        self.output_field = Text(master=self, height=15)

        ttk.Button(master=self, text="Encode url", command=self.encode).grid(row=2, column=0, padx=15 ,pady=15 ,sticky="W")
        ttk.Button(master=self, text="Decode url", command=self.decode).grid(row=2, column=1, sticky="W")

        self.input_field.grid(row=1, column=0, columnspan=2, padx=15)
        self.output_field.grid(row=3, column=0, columnspan=2, pady=10)
    
    def encode(self) -> None:
        text: str = self.input_field.get(index1=0.1, index2=END)
        self.output_field.delete(index1=0.1, index2=END)
        self.output_field.insert(index=0.1, chars=quote(text, safe=""))

    def decode(self) -> None:
        text: str = self.input_field.get(index1=0.1, index2=END)
        self.output_field.delete(index1=0.1, index2=END)
        self.output_field.insert(index=0.1, chars=unquote(text))

if __name__ == "__main__":
    try:
        MainWindow = MainWindow()
        MainWindow.mainloop()
    except KeyboardInterrupt:
        MainWindow.quit()
