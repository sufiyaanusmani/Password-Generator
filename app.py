import tkinter as tk
import random
import clipboard

def generateRandomString(length):
  characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
  password = ""
  for i in range(length):
    password += random.choice(characters)
  return password

def generatePassword():
    length = slider1.get()
    password = generateRandomString(length)
    label3.config(text='Password Generated')
    label5.config(text='Text copied to clipboard')
    entry.insert(0, password)
    clipboard.copy(password)


# Create the window object
window = tk.Tk()

# Set the window title
window.title('Password Generator')


label1 = tk.Label(window, text="Password Generator", font=('Ubuntu', 20), fg='red')
label1.anchor = 'center'
label1.pack()

label2 = tk.Label(window, text="Enter length of password", anchor='w', justify='left', width=50, pady=20, padx=40, font=('Ubuntu', 12))
label2.pack()

slider1 = tk.Scale(window, from_=0, to=100, length=300,tickinterval=10, orient=tk.HORIZONTAL, activebackground = 'red', troughcolor = 'white')
slider1.pack()

button = tk.Button(window, text="Generate Password", command=generatePassword)
button.pack()

label3 = tk.Label(window, text="")
label3.pack()

label4 = tk.Label(window, text="", font=('Ubuntu', 10))
label4.pack()

entry = tk.Entry(window, text='', width=60)
entry.pack()

label5 = tk.Label(window, text="")
label5.pack()

label6 = tk.Label(window, text="Created by Sufiyaan Usmani", font=('Ubuntu', 10))
label6.pack()

# Write your code here
window.geometry('400x300')
window.minsize(400, 300)
window.maxsize(400, 300)
# window.eval('tk::PlaceWindow . center')
# Keep the window open until we close it
window.mainloop()
