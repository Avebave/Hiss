import customtkinter
import random
import time

def button_callback():
    print("button pressed")

app = customtkinter.CTk()
app.title("my app")
app.geometry("800x600")




button = customtkinter.CTkButton(app, text="my button", command=button_callback)
button.grid(row=1, column=0, padx=20, pady=20)

#with open("hiss.py") as file:
#    exec(file.read())

app.mainloop()
