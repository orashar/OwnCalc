############################################################################################################
#####                                        Coded By - ORASHAR                                        #####
#####                                         Date - 18/06/19                                          #####
############################################################################################################


from tkinter import *
import math

def insertButton():

    # creating buttons one by one
    bac = Button(root, text='AC', command=lambda: event('AC'), width=8).grid(row=1, column=0, columnspan=1, sticky=N+E+W+S)
    bdel = Button(root, text='DEL', command=lambda: event('DEL'), width=8).grid(row=1, column=1, columnspan=1, sticky=N+E+W+S)
    broot = Button(root, text='√', command=lambda: event('√'), width=8).grid(row=1, column=2, columnspan=1, sticky=N+E+W+S)
    bdiv = Button(root, text='/', command=lambda: event('/'), width=8).grid(row=1, column=3, columnspan=1, sticky=N+E+W+S)
    b7 = Button(root, text='7', command=lambda: event(7), width=8).grid(row=2, column=0, columnspan=1, sticky=N+E+W+S)
    b8 = Button(root, text='8', command=lambda: event(8), width=8).grid(row=2, column=1, columnspan=1, sticky=N+E+W+S)
    b9 = Button(root, text='9', command=lambda: event(9), width=8).grid(row=2, column=2, columnspan=1, sticky=N+E+W+S)
    bmul = Button(root, text='*', command=lambda: event('*'), width=8).grid(row=2, column=3, columnspan=1, sticky=N+E+W+S)
    b4 = Button(root, text='4', command=lambda: event(4), width=8).grid(row=3, column=0, columnspan=1, sticky=N+E+W+S)
    b5 = Button(root, text='5', command=lambda: event(5), width=8).grid(row=3, column=1, columnspan=1, sticky=N+E+W+S)
    b6 = Button(root, text='6', command=lambda: event(6), width=8).grid(row=3, column=2, columnspan=1, sticky=N+E+W+S)
    bsub = Button(root, text='-', command=lambda: event('-'), width=8).grid(row=3, column=3, columnspan=1, sticky=N+E+W+S)
    b1 = Button(root, text='1', command= lambda: event(1), width=8).grid(row=4, column=0, columnspan=1, sticky=N+E+W+S)
    b2 = Button(root, text='2', command=lambda: event(2), width=8).grid(row=4, column=1, columnspan=1, sticky=N+E+W+S)
    b3 = Button(root, text='3', command=lambda: event(3), width=8).grid(row=4, column=2, columnspan=1, sticky=N+E+W+S)
    bsum = Button(root, text='+', command=lambda: event('+'), width=8).grid(row=4, column=3, columnspan=1, sticky=N+E+W+S)
    b0 = Button(root, text='0', command=lambda: event(0), width=8).grid(row=5, column=0, columnspan=1, sticky=N+E+W+S)
    bdot = Button(root, text='.', command=lambda: event('.'), width=8).grid(row=5, column=1, columnspan=1, sticky=N+E+W+S)
    beql = Button(root, text='=', command=equal, width=8).grid(row=5, column=2, columnspan=1, sticky=N+E+W+S)
    bans = Button(root, text='ANS', command= lambda: event('ANS'), width=8).grid(row=5, column=3, sticky=N+E+W+S)

# runs the code whenever a button is clicked
def event(b):
    global query

    if b in (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, '+', '-', '*', '/', '.'):
        query += str(b)
        display(query)
    elif b == 'AC':
        allClear()
    elif b == 'DEL':
        delete(query)
    elif b == '√':
        sroot(query)

    # evaluates the answer also retains the answer for further use
    elif b == 'ANS':
        equal()
        query = result.get()

# displays the value in the entry bar
def display(query):
    result.set(query)

# clears the entry bar
def allClear():
    result.set('')

# deletes the last entered value
def delete(last):
    global query

    query = query[:-1]
    display(query)

# calculates the square root
def sroot(query):
    total = math.sqrt(int(query))
    result.set(total)

# evaluates the entered equation
def equal():
    global query

    total = str(eval(query))
    result.set(total)
    query = ''


# start the main app
if __name__ == '__main__':
    root = Tk()
    root.title("Calculator")
    root.geometry("368x178")

    # fill the blank space in the window
    for row in range(6):
        for column in range(4):
            root.grid_columnconfigure(column, weight=1)
            root.grid_columnconfigure(column, weight=1)
            root.grid_rowconfigure(row, weight=1)
            root.grid_rowconfigure(row, weight=1)

    result = ''
    query = ''
    result = StringVar()
    entry = Entry(root, textvariable=result).grid(columnspan=4)
    #insert all the buttons
    insertButton()

    # run the root window
    mainloop()
