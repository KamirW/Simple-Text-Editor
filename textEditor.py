from tkinter import *
import tkinter.filedialog

# Creating the window
root = Tk("Text Editor")
root.title("Simple Text Editor")

# Creating a text widget & attaching it to the window
text = Text(root)
text.grid()


def saveAs():
    global text

    t = text.get("1.0", "end-1c")
    saveLocation = tkinter.filedialog.asksaveasfile()

    # Creating a writable file 
    file1 = open(saveLocation, "w+")
    file1.write(t)
    file1.close()

# Creating a save button
button = Button(root, text="Save", command=saveAs)
button.grid()

### FONT CHANGING ###
def fontHelvetica():
    global text

    text.config(font="Helvetica")

def fontCourier():
    global text

    text.config(font="Courier")

font = Menubutton(root, text="Font")
font.grid()
font_menu = Menu(font, tearoff=0)
helvetica = IntVar()
courier = IntVar()

font_menu.add_checkbutton(label="Courier", variable=courier, command=fontCourier)
font_menu.add_checkbutton(label="Helvetica", variable=helvetica, command=fontHelvetica)

font["menu"] = font_menu


root.mainloop()