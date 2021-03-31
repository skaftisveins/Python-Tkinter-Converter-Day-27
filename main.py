from tkinter import *


def button_convert():
    """Convert input text string to float, round it and change into centimeters
    """
    inches = float(input.get())
    centimeters = round(inches * 2.54, 2)
    result_label.config(text=f"{centimeters}")


window = Tk()
window.title("Tkinter Converter")
window.minsize(width=300, height=150)
window.config(padx=40, pady=40)

input = Entry(width=10)
input.grid(column=1, row=0)

inch_label = Label(text="Inches")
inch_label.grid(column=2, row=0)
inch_label.config(padx=10)

info_label = Label(text="is equal to: ")
info_label.grid(column=0, row=1)
info_label.config(padx=10)

result_label = Label(text="0", font=("bold"))
result_label.grid(column=1, row=1)
result_label.config(padx=10)

cm_label = Label(text="Cm")
cm_label.grid(column=2, row=1)
cm_label.config(padx=10)

button = Button(text="Calculate", command=button_convert)
button.grid(column=1, row=2)

window.mainloop()
