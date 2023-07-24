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
        root, text="".join(char for char in string if char not in "aeiouAEIOU")
    )
    # place label
    label.grid(row=2, column=1)


# declare root of our GUI - window object
root = tkinter.Tk(className="Vowel Remover")

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
