from tkinter import *
from tkinter import messagebox
window = Tk()

window.geometry('500x500')
window.title('Interest caculater')

label = Label(window, text = 'amount inserted')
label.place(x = 200, y = 50)

entry = Entry(window)
entry.place(x = 200, y = 80)

label2 = Label(text='length in time')
label2.place(x = 200, y= 120)


entry1 = Entry(window)
entry1.place(x = 200, y = 150)


label3 = Label(text='rate')
label3.place(x = 200, y= 190)


entry3 = Entry(window)
entry3.place(x = 200, y = 220)
def display () :
    amount = float(entry.get())
    time = float(entry1.get())
    rate = float(entry3.get())

    global total

    total = amount + ((amount * time * rate ) / 100)

    message = messagebox.showinfo('You will get', ('simple intrest ' + str(total) + '$'))

button = Button(text = 'Calculate', command=display)
button.place(x = 230, y = 300)
window.mainloop()