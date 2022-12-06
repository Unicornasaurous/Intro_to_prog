from tkinter import *
from datachecker import dataChecker

class app():
    root = Tk()
    root.geometry("300x150")
    root.title("Kilometer Converter")

    def main(self):
        Label(self.root, text="Kilometers", font=30).pack()
        self.km = Entry(self.root)
        self.km.pack()
        Button(self.root, text="Enter", command=self.displayKilometers).pack()
        self.answer = Label(self.root, text="Miles: ", font=30)
        self.answer.pack()
        self.root.mainloop()

    def displayKilometers(self):
        if hasattr(self, "hint"):
            self.hint.destroy()
        else:
            pass
        data = self.km.get()
        if dataChecker(data, "num"):
            miles = self.convertKilometers(data)
            self.answer.config(text=f"Miles: {miles}")
        else:
            self.answer.config(text="Miles: ")
            self.hint = Label(self.root, text="Please enter a number")
            self.hint.pack()

    def convertKilometers(self, kilos):
        return str(format(float(kilos) * 0.6214, ",.2f"))

    
app().main()

