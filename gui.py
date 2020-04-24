from tkinter import *
from colours import *

window = Tk()
window.geometry("600x400")
window.title("Welcome")
window.configure(bg='black')

canvas = Canvas(window, width=600, height=400)
canvas.pack()
canvas.create_line(300,0,300,400)

def callWhite():
    changeColour()
    print("white was called")
    return [0,1]

def callBlack():
    changeColour()
    print("black was called")
    return [1,0]

def changeColour():
    colour = getRGB()
    whiteB.configure(highlightbackground=from_rgb(colour), relief=FLAT)
    blackB.configure(highlightbackground=from_rgb(colour), fg="black")

whiteB = Button(window, text="White", font= ('cornerstone', 20, 'bold'), width=15, height=5, command = callWhite)
whiteB.place(x=28, y=150)

blackB = Button(window, text="Black", font= ('cornerstone', 20, 'bold'), width=15, height=5, command = callBlack, fg="Black")
blackB.place(x=328, y=150)


window.mainloop()
