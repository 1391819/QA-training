# imports
import tkinter


def strip_vowels():
    global label
    # destroy any existing labels on the screen
    label.destroy()
    # get text from input
    s = input.get()
    # create new label
    label = tkinter.Label(
        root, text="".join(char for char in s if char not in "aeiouAEIOU")
    )
    # place label
    label.grid(row=2, column=1)


# declare root of our GUI - window object
root = tkinter.Tk(className="Vowel Remover")

w = 800  # width for the Tk root
h = 650  # height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth()  # width of the screen
hs = root.winfo_screenheight()  # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)

# set the dimensions of the screen
# and where it is placed
root.geometry("%dx%d+%d+%d" % (w, h, x, y))

# label
label = tkinter.Label(root, text="")

# textbox
input = tkinter.Entry(root)
input.grid(row=1, column=1)

# submit button
submit = tkinter.Button(root, text="Strip vowels", command=strip_vowels)
submit.grid(row=1, column=2)

if __name__ == "__main__":
    # run GUI - main event loop
    root.mainloop()
