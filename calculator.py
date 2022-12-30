import tkinter

# Creating the window
window = tkinter.Tk()
window.title("Calculator")
window.iconbitmap("icon.ico")
window.geometry("375x500")
window.resizable(width=False, height=False)
window.configure(bg="#FFE7B4")

# Creating the widgets frame
widgets_frame = tkinter.Frame(window, bg="#FFE7B4")
widgets_frame.pack()

# Creating the calculator functions
expression = ""
input_text = tkinter.StringVar(value="0")
evaluated = False

def enter(arg : str):
    '''Creates an expression from the calculator inputs'''
    global expression
    global input_text
    global evaluated
    if evaluated and arg in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "(", ")"]:
        expression = arg
        input_text.set(expression)
    else:
        expression += arg
        input_text.set(expression)
    
    evaluated = False

def evaluate():
    '''Evaluates the expression entered'''
    global expression
    global input_text
    global evaluated
    try:    
        expression = str(eval(expression))
        input_text.set(expression)
    except Exception as error:
        expression = ""
        input_text.set(str(type(error).__name__))
    evaluated = True

def erase():
    "Erases the last input"
    global expression
    global input_text
    if len(expression) > 1:
        expression = expression[:-1]
        input_text.set(expression)
    else:
        expression = ""
        input_text.set(value="0")

def clear():
    '''Clears all inputs'''
    global expression
    global input_text
    expression = ""
    input_text.set(value="0")

# Creating the widgets
input_widget = tkinter.Entry(widgets_frame, relief="sunken", bd=2, bg="#FFFAF1",
                             textvariable=input_text, justify="right", font=("arial", 18, "bold"))
input_widget.grid(row=0, column=0, columnspan=4, ipadx=34, ipady=18, pady=20)

one = tkinter.Button(widgets_frame, relief="raised", bg="#FFF3DA",
                     text="1", font=("arial", 18), width=5, height=2, command=lambda : enter("1"))
one.grid(row=1, column=0)

two = tkinter.Button(widgets_frame, relief="raised", bg="#FFF3DA",
                     text="2", font=("arial", 18), width=5, height=2, command=lambda : enter("2"))
two.grid(row=1, column=1)

three = tkinter.Button(widgets_frame, relief="raised", bg="#FFF3DA",
                       text="3", font=("arial", 18), width=5, height=2, command=lambda : enter("3"))
three.grid(row=1, column=2)

add = tkinter.Button(widgets_frame, relief="raised", bg="#FFF3DA",
                     text="+", font=("arial", 18), width=5, height=2, command=lambda : enter("+"))
add.grid(row=1, column=3)

four = tkinter.Button(widgets_frame, relief="raised", bg="#FFF3DA",
                      text="4", font=("arial", 18), width=5, height=2, command=lambda : enter("4"))
four.grid(row=2, column=0)

five = tkinter.Button(widgets_frame, relief="raised", bg="#FFF3DA",
                      text="5", font=("arial", 18), width=5, height=2, command=lambda : enter("5"))
five.grid(row=2, column=1)

six = tkinter.Button(widgets_frame, relief="raised", bg="#FFF3DA",
                     text="6", font=("arial", 18), width=5, height=2, command=lambda : enter("6"))
six.grid(row=2, column=2)

subtract = tkinter.Button(widgets_frame, relief="raised", bg="#FFF3DA",
                          text="-", font=("arial", 18), width=5, height=2, command=lambda : enter("-"))
subtract.grid(row=2, column=3)

seven = tkinter.Button(widgets_frame, relief="raised", bg="#FFF3DA",
                       text="7", font=("arial", 18), width=5, height=2, command=lambda : enter("7"))
seven.grid(row=3, column=0)

eight = tkinter.Button(widgets_frame, relief="raised", bg="#FFF3DA",
                       text="8", font=("arial", 18), width=5, height=2, command=lambda : enter("8"))
eight.grid(row=3, column=1)

nine = tkinter.Button(widgets_frame, relief="raised", bg="#FFF3DA",
                      text="9", font=("arial", 18), width=5, height=2, command=lambda : enter("9"))
nine.grid(row=3, column=2)

multiply = tkinter.Button(widgets_frame, relief="raised", bg="#FFF3DA",
                          text="x", font=("arial", 18), width=5, height=2, command=lambda : enter("*"))
multiply.grid(row=3, column=3)

zero = tkinter.Button(widgets_frame, relief="raised", bg="#FFF3DA",
                      text="0", font=("arial", 18), width=5, height=2, command=lambda : enter("0"))
zero.grid(row=4, column=0)

open_bracket = tkinter.Button(widgets_frame, relief="raised", bg="#FFF3DA",
                         text="(", font=("arial", 18), width=5, height=2, command=lambda : enter("("))
open_bracket.grid(row=4, column=1)

closed_bracket = tkinter.Button(widgets_frame, relief="raised", bg="#FFF3DA",
                   text=")", font=("arial", 18), width=5, height=2, command=lambda : enter(")"))
closed_bracket.grid(row=4, column=2)

divide = tkinter.Button(widgets_frame, relief="raised", bg="#FFF3DA",
                        text="/", font=("arial", 18), width=5, height=2, command=lambda : enter("/"))
divide.grid(row=4, column=3)

c = tkinter.Button(widgets_frame, relief="raised", bg="#FFF3DA",
                       text="C", font=("arial", 18), width=5, height=2, command=clear)
c.grid(row=5, column=0)

decimal = tkinter.Button(widgets_frame, relief="raised", bg="#FFF3DA",
                         text=".", font=("arial", 18), width=5, height=2, command=lambda : enter("."))
decimal.grid(row=5, column=1)

delete = tkinter.Button(widgets_frame, relief="raised", bg="#FFF3DA",
                   text="Del", font=("arial", 18), width=5, height=2, command=erase)
delete.grid(row=5, column=2)

equal = tkinter.Button(widgets_frame, relief="raised", bg="#FFF3DA",
                       text="=", font=("arial", 18), width=5, height=2, command=evaluate)
equal.grid(row=5, column=3)

window.mainloop()