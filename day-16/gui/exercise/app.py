# imports
import tkinter
from tkinter.filedialog import askopenfilename


def show_file_content(file_content: list) -> None:
    """Insert file content into text area line by line

    Args:
        file_content (list): List of lines - content of the file
    """

    # get all children - can specify instance types
    # labels = [w for w in root.winfo_children() if isinstance(w, tkinter.Label)]

    # get input text
    # input_text = input.get()

    # clear previous content of text area
    #   .END -> constant -> represents the point immediately after the last char
    text_area.delete(1.0, tkinter.END)

    # use enumerate to count line numbers
    for i, line in enumerate(file_content, start=1):
        # insert line content into text area
        text_area.insert(tkinter.END, f"{i}. {line}")


def pick_file() -> None:
    """Pick file using file dialog from user menu"""

    # get full path to the file
    filename = askopenfilename()

    # if something was picked
    if filename:
        # open file in read mode
        with open(filename, mode="r") as file:
            # get file content - list
            file_content = file.readlines()

        # show file content
        show_file_content(file_content)


# root
root = tkinter.Tk(className="File viewer")

# create a Text widget to display the file content
# add wrapping just in case line is longer than window size
text_area = tkinter.Text(root, wrap="word")
text_area.grid(row=2, column=1)

# create menu bar
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
# create menu item, do not allow menu detachment
file_menu = tkinter.Menu(menu_bar, tearoff=0)
# add cascade item
menu_bar.add_cascade(label="File", menu=file_menu)
# add Open option to File cascade
file_menu.add_command(label="Open", command=pick_file)

if __name__ == "__main__":
    root.mainloop()
