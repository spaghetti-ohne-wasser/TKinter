#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox
from platform import system

if system() == "Windows":
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)

resultAreaBackground: str = "#282828"
resultAreaForeground: str = "white"
buttonBackground: str = "#141414"
buttonActiveBackground: str = "#191919"
buttonActiveForeground: str = "white"

class MainWindow(Tk):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.resizable(width=False, height=False)
        self.title(string="Calculator")
        self.config(background="#191919")
        
        self.placeWidgets()



    def placeWidgets(self) -> None:
        # resultArea
        self.resultArea = Entry(master=self, background=resultAreaBackground, foreground=resultAreaForeground, font=("Montserrat", 32), width=24, highlightbackground=resultAreaBackground)
        self.resultArea.grid(row=0, column=0, columnspan=4, padx=0, pady=0)

        for placeHolder in range(0, 3):
            # placeHolder Buttons
            Button(master=self, background=buttonBackground, foreground="white", font=("Arial", 60), width=3, highlightbackground=resultAreaBackground, activebackground=buttonActiveBackground, activeforeground=buttonActiveForeground).grid(row=1, column=placeHolder)
        # DEL Button
        Button(master=self, text="DEL", background=buttonBackground, foreground="white", font=("Arial", 60), width=3, highlightbackground=resultAreaBackground, activebackground=buttonActiveBackground, activeforeground=buttonActiveForeground, command=self.clearResultArea).grid(row=1, column=3, padx=0, pady=0)
        # Buttons  7-9
        Button(master=self, text="7", background=buttonBackground, foreground="white", font=("Arial", 60), width=3, highlightbackground=resultAreaBackground, activebackground=buttonActiveBackground, activeforeground=buttonActiveForeground, command=lambda: self.addInput("7")).grid(row=2, column=0, padx=0, pady=0)
        Button(master=self, text="8", background=buttonBackground, foreground="white", font=("Arial", 60), width=3, highlightbackground=resultAreaBackground, activebackground=buttonActiveBackground, activeforeground=buttonActiveForeground, command=lambda: self.addInput("8")).grid(row=2, column=1, padx=0, pady=0)
        Button(master=self, text="9", background=buttonBackground, foreground="white", font=("Arial", 60), width=3, highlightbackground=resultAreaBackground, activebackground=buttonActiveBackground, activeforeground=buttonActiveForeground, command=lambda: self.addInput("9")).grid(row=2, column=2, padx=0, pady=0)
        # Buttons 4-6
        Button(master=self, text="4", background=buttonBackground, foreground="white", font=("Arial", 60), width=3, highlightbackground=resultAreaBackground, activebackground=buttonActiveBackground, activeforeground=buttonActiveForeground, command=lambda: self.addInput("4")).grid(row=3, column=0, padx=0, pady=0)
        Button(master=self, text="5", background=buttonBackground, foreground="white", font=("Arial", 60), width=3, highlightbackground=resultAreaBackground, activebackground=buttonActiveBackground, activeforeground=buttonActiveForeground, command=lambda: self.addInput("5")).grid(row=3, column=1, padx=0, pady=0)
        Button(master=self, text="6", background=buttonBackground, foreground="white", font=("Arial", 60), width=3, highlightbackground=resultAreaBackground, activebackground=buttonActiveBackground, activeforeground=buttonActiveForeground, command=lambda: self.addInput("6")).grid(row=3, column=2, padx=0, pady=0)
        # Buttons 1-3
        Button(master=self, text="1", background=buttonBackground, foreground="white", font=("Arial", 60), width=3, highlightbackground=resultAreaBackground, activebackground=buttonActiveBackground, activeforeground=buttonActiveForeground, command=lambda: self.addInput("1")).grid(row=4, column=0, padx=0, pady=0)
        Button(master=self, text="2", background=buttonBackground, foreground="white", font=("Arial", 60), width=3, highlightbackground=resultAreaBackground, activebackground=buttonActiveBackground, activeforeground=buttonActiveForeground, command=lambda: self.addInput("2")).grid(row=4, column=1, padx=0, pady=0)
        Button(master=self, text="3", background=buttonBackground, foreground="white", font=("Arial", 60), width=3, highlightbackground=resultAreaBackground, activebackground=buttonActiveBackground, activeforeground=buttonActiveForeground, command=lambda: self.addInput("3")).grid(row=4, column=2, padx=0, pady=0)
        # Buttons 0, . , =
        Button(master=self, text="0", background=buttonBackground, foreground="white", font=("Arial", 60), width=3, highlightbackground=resultAreaBackground, activebackground=buttonActiveBackground, activeforeground=buttonActiveForeground, command=lambda: self.addInput("0")).grid(row=5, column=0, padx=0, pady=0)
        Button(master=self, text=".", background=buttonBackground, foreground="white", font=("Arial", 60), width=3, highlightbackground=resultAreaBackground, activebackground=buttonActiveBackground, activeforeground=buttonActiveForeground, command=lambda: self.addInput(".")).grid(row=5, column=1, padx=0, pady=0)
        Button(master=self, text="=", background=buttonBackground, foreground="white", font=("Arial", 60), width=3, highlightbackground=resultAreaBackground, activebackground=buttonActiveBackground, activeforeground=buttonActiveForeground, command=self.calculateResult).grid(row=5, column=2, padx=0, pady=0)
        # Buttons /, x, +, -
        Button(master=self, text="/", background=buttonBackground, foreground="white", font=("Arial", 60), width=3, highlightbackground=resultAreaBackground, activebackground=buttonActiveBackground, activeforeground=buttonActiveForeground, command=lambda: self.addInput("/")).grid(row=2, column=3, padx=0, pady=0)
        Button(master=self, text="x", background=buttonBackground, foreground="white", font=("Arial", 60), width=3, highlightbackground=resultAreaBackground, activebackground=buttonActiveBackground, activeforeground=buttonActiveForeground, command=lambda: self.addInput("*")).grid(row=3, column=3, padx=0, pady=0)
        Button(master=self, text="+", background=buttonBackground, foreground="white", font=("Arial", 60), width=3, highlightbackground=resultAreaBackground, activebackground=buttonActiveBackground, activeforeground=buttonActiveForeground, command=lambda: self.addInput("+")).grid(row=4, column=3, padx=0, pady=0)
        Button(master=self, text="-", background=buttonBackground, foreground="white", font=("Arial", 60), width=3, highlightbackground=resultAreaBackground, activebackground=buttonActiveBackground, activeforeground=buttonActiveForeground, command=lambda: self.addInput("-")).grid(row=5, column=3, padx=0, pady=0)


    def clearResultArea(self) -> None:
        self.resultArea.delete(first=0, last=END)

    def addInput(self, input: str) -> None:
        oldInput: str = self.resultArea.get()
        newInput: str = oldInput + input
        self.clearResultArea()
        self.resultArea.insert(index=0, string=newInput)

    def calculateResult(self) -> None:
        try:
            result: any = eval(self.resultArea.get())
            self.clearResultArea()
            self.resultArea.insert(index=0, string=str(result))
        except Exception as error:
            messagebox.showerror(title="Error", message=f"{error}\nInvalid input: {self.resultArea.get()}")
                   
if __name__ == "__main__":
    try:
        MainWindow = MainWindow()
        MainWindow.mainloop()
    except KeyboardInterrupt:
        MainWindow.quit()    
