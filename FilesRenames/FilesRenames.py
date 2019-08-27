from tkinter import *
from os import *

class Prog(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.setUI()

	def set_print(self):
		
		self.parent.title("Программка *")

    def setUI(self):

        self.parent.title("Программка") # заголовок формы
		
		button_1_lab = Label(self, text="Кнопка: ") 
        button_1_lab.grid(row=0, column=0, padx=6) 

		#Кнопки
		button_1 = Button(self, text="Кнопка", width=10, command=lambda: self.set_print)
		button_1.grid(row=0, column=1)

def main():
    root = Tk()
    root.geometry('300x400+30+30')
    app = Prog(root)
    root.mainloop()


if __name__ == '__main__':
    main()