from tkinter import *

main = Tk()
main.geometry('500x500')
window = Frame(main)
window.master.title('stickman')
button = Button(text='Start')
button.pack(side='top')
window.pack()
window.mainloop()
