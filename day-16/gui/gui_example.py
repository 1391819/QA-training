# imports
import tkinter

# declare root of our GUI - window object
root = tkinter.Tk()

# label
label = tkinter.Label(root, text="Hello World!")

# place label on the window
# will place object wherever it can in the window
# label.pack()

# if we want to place it in a specific position
# takes in a row and a column
label.grid(row=1, column=1)


if __name__ == "__main__":
    # run GUI - main event loop
    root.mainloop()
