# Credit Card Generator with Python

The main.py file creates separately a CC number, CVC code and a date starting from 2023 by using the random library and randint function.The imported Pandas library reads an xlsx file containing up to 200 randomly generated titles, names and surnames, which then a randomly generated number by using randint between 1 and the length of the Excel file will be the index of the chosen line in the file.

An image, designed in Canvas, of the front and back of an exemplary Visa card is displayed by the Tkinter library. The image (cart.png) is imported and read by the PIL library. The randomly generated numbers are placed accordingly with Tkinter.

A new image of a randomly generated credit card is displayed every time we run the main code. Here's an example:



<img width="497" alt="Screenshot 2023-04-28 at 13 30 02" src="https://user-images.githubusercontent.com/126245553/235136285-7ffdbe4b-b69c-4d29-844b-9a8a48ec5740.png">
