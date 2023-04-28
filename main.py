# generate your credit card info

import random
import pandas as pd
from tkinter import *
from PIL import Image, ImageTk

df = pd.read_excel('random_gen.xlsx')


def card_number_generator():
    card_number = ''

    for chiffre in range(19):
        if chiffre == 4 or chiffre == 9 or chiffre == 14:
            card_number += ' '
        else:
            card_number += str(random.randint(0, 9))

    return card_number


def cvc_generator():  # 3 digit number generator
    cvc = ''
    for i in range(3):
        cvc += str(random.randint(0, 9))
    return cvc


def name_select():  # selects a random name from the Excel file
    index = random.randint(1, len(df))
    space = ' '
    return df['Title'].iloc[index] + space + df['First Name'].iloc[index] + space + df['Surname'].iloc[index]


def date_generator():
    year = 23 + random.randint(0, 6)

    number_month = random.randint(1, 12)
    if number_month < 10:
        month = '0' + str(number_month)
    else:
        month = str(number_month)

    return month + '/' + str(year)


#  configuring tkinter
window = Tk()
window.geometry('500x500')
window.title("Credit Card Generator")

image = Image.open("cart.png")
resize = image.resize((500, 500), Image.LANCZOS)
photo = ImageTk.PhotoImage(resize)

canvas = Canvas(window, width=image.size[0], height=image.size[1])
canvas.create_image(0, 0, anchor=NW, image=photo)

# placement of card credentials
canvas.create_text(250, 155, text=card_number_generator(), fill="gray88", font=('Credit Card', '15'))
canvas.create_text(240, 185, text=date_generator(), fill="gray77", font=('Credit Card', '8'))
canvas.create_text(210, 200, text=name_select(), fill="gray88", font=('Kredit', '14'))
canvas.create_text(348, 360, text=cvc_generator(), fill="black", font=('Helvetica', '15'))
canvas.pack()

window.mainloop()
