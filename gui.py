from tkinter import *
from colours import *
from fileOp import *

window = Tk()
window.geometry("600x400")
window.title("Welcome")
window.configure(bg='black')

canvas = Canvas(window, width=600, height=400)
canvas.pack()
canvas.create_line(300,0,300,400)

def callWhite():
    colour = changeColour()
    writeResultToFile(getFileColours(colour), "white")

def callBlack():
    colour = changeColour()
    writeResultToFile(getFileColours(colour), "black")

def changeColour():
    colour = getRGB()
    whiteB.configure(highlightbackground=from_rgb(colour), relief=FLAT)
    blackB.configure(highlightbackground=from_rgb(colour), fg="black")
    return colour

whiteB = Button(window, text="White", font= ('cornerstone', 20, 'bold'), width=15, height=5, command = callWhite)
whiteB.place(x=28, y=150)

blackB = Button(window, text="Black", font= ('cornerstone', 20, 'bold'), width=15, height=5, command = callBlack, fg="Black")
blackB.place(x=328, y=150)


window.mainloop()
