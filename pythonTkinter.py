from tkinter import *

def printSomething():
    print("hello")
def foreverLoop():
    print("This is a test run")
root = Tk()

# Creating the menus...

mainMenu = Menu(root)
root.config(menu = mainMenu)
FileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "File", menu = FileMenu)
FileMenu.add_command(label = "Print", command = printSomething)

#creating the buttons in different frames

controlFrame = Frame(root, bg = "blue")
foreverLoopButton = Button(controlFrame, text = "Forever", command = foreverLoop)
foreverLoopButton.pack(side = LEFT, padx = 2, pady=2)

insertButton = Button(controlFrame, text = "Print", command = printSomething)
insertButton.pack(side = LEFT, padx = 2, pady = 2)

controlFrame.pack(side = TOP, fill = X)                      #just change the side to TOP,BOTTOM,RIGHT and check



root.mainloop()


# Stupid program.... can't help it