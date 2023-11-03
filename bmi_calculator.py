from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(width=250, height=200)

#label
weight_label = Label(text="Enter your Weight (kg)")
weight_label.config(pady=5)
weight_label.pack()

#entry
weight_entry = Entry(width=15)
weight_entry.pack()

#label
height_label = Label(text="Enter your Height (cm)")
height_label.config(pady=5)
height_label.pack()

#entry
height_entry = Entry(width=15)
height_entry.pack()

#ValueError

def button_clicked():
    try:
        if weight_entry.get() == "" or height_entry.get() == "":
            result.config(text="Enter both weight and height!")
        else:
            answer = float(weight_entry.get()) / (float(height_entry.get())/100 * float(height_entry.get())/100)
            if answer <= 18.5:
                result.config(text = f"Your BMI is {answer:.2f}. You are underweight.")
            elif answer > 18.5 and answer <= 24.9:
                result.config(text = f"Your BMI is {answer:.2f}. You are healthy.")
            elif answer > 24.9 and answer <= 29.9:
                result.config(text = f"Your BMI is {answer:.2f}. You are overweight.")
            elif answer > 29.9 and answer <= 34.9:
                result.config(text = f"Your BMI is {answer:.2f}. You are obese class 1.")
            elif answer > 34.9 and answer <= 39.9:
                result.config(text = f"Your BMI is {answer:.2f}. You are obese class 2.")
            elif answer > 39.9:
                result.config(text = f"Your BMI is {answer:.2f}. You are obese class 3.")
    except ValueError:
        result.config(text="Enter a valid number!")

#button
button = Button(text="Calculate",command=button_clicked)
button.config(pady=2)
button.pack()

#label
result = Label(window, text="")
result.pack()

window.mainloop()