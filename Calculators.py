import tkinter as tk
import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.collections as mc
import os.path
import keyboard
import linecache


class Cursor(object):   # Thank you Stack Exchange
    def __init__(self, ax):
        self.ax = ax
        self.lx = ax.axhline(color='k')  # the horiz line
        self.ly = ax.axvline(color='k')  # the vert line

        # text location in axes coords
        self.txt = ax.text(0.7, 0.9, '', transform=ax.transAxes)

    def mouse_move(self, event):
        if not event.inaxes:
            return

        x, y = event.xdata, event.ydata
        # update the line positions
        self.lx.set_ydata(y)
        self.ly.set_xdata(x)

        self.txt.set_text('x=%1.2f, y=%1.2f' % (x, y))
        self.ax.figure.canvas.draw()


root = tk.Tk()
root.resizable(False, False)
root.configure(bg='#0A3D62')  # Change BG color
root.title('Calculators')
dev_label = tk.Label(root, text='Made by Hoswoo', font=('times', 14, 'bold'), bg='#0A3D62', fg="#55efc4",
                     anchor="w")  # Hoswoo
# setting the windows size
base_size = "520x355"
root.geometry(base_size)
# canvas = tk.Canvas(root, height=320, width=240,bg="#263D42")
# canvas.pack()

pay_var_use_equations = tk.StringVar()
product_var_use_equations = tk.StringVar()

pay_var_own_prices = tk.StringVar()
product_var_own_prices = tk.StringVar()
# Text Box
text1 = tk.Text(root, height=18, width=41, bg='#A1AAB5', font=('times', 10, 'normal'))
text1.config(state="disabled")
dev_label.grid(row=0, column=0)
text1.grid(row=1, column=0, rowspan=20, padx=3)

jim_sales_var = tk.StringVar()
josh_sales_var = tk.StringVar()
pickup_price_var = tk.StringVar()


price_var = []
# Arrays


p_label = []
lines = []
price = []
amount = []
point1 = []
point2 = []
m_AvP = []
b_AvP = []
m_PvA = []
b_PvA = []
m_var_PvA = []
b_var_PvA = []
m_var_AvP = []
b_var_AvP = []

# Needed to make this global because I'm a dunce

if os.path.exists(os.path.join(os.path.expanduser("~/Documents/hoswoo_calculator/price_per_amount.dat"))):
    os.chdir(os.path.expanduser('~/Documents/hoswoo_calculator'))
    f = open("price_per_amount.dat", "r")
    if f.mode == "r":
        price_per_amount = float(linecache.getline('price_per_amount.dat', 1))  # First line is value
        price_per_amount_units = linecache.getline('price_per_amount.dat', 2)  # Second line is the units
        print("ppa_units: ", price_per_amount_units)


def insert_text(text, showTime=True):
    text1.config(state='normal')
    time = '{:%H:%M:%S}'.format(datetime.datetime.now())
    if showTime is True:    # Show time stamp if bool is true
        text1.insert(tk.INSERT, "(" + time + ")\n")
    text1.insert(tk.INSERT, text + "\n")
    text1.see("end")
    text1.config(state='disabled')


def checkNum(n):  # Ensure input is a number
    try:
        float(n)
    except:
        return False
    return True


# Frame 1 (Get Equations)
frame1 = tk.Frame(root, borderwidth=2, pady=2, height=500, width=260, bg="#A1AAB5")
reg = root.register(checkNum)
entry_label = tk.Label(frame1, text='How many entries?', bg='#A1AAB5', fg="#2B3139", padx=5)
entry_var = tk.StringVar()
entries_entry = tk.Entry(frame1, textvariable=entry_var, font=('calibre', 8, 'normal'))
entries_entry.insert(tk.INSERT, "5")
entries_entry.config(validate="key", validatecommand=(reg, '%P'))
next_expanded = False
frame2 = tk.Frame(root, borderwidth=2, pady=2, height=350, width=260, bg="#A1AAB5")
frame3 = tk.Frame(root, borderwidth=2, pady=2, height=350, width=260, bg="#A1AAB5")
frame3.place(x=526, y=40)
# Frame 2 = units
radio_var = tk.IntVar()
units_label = tk.Label(root, text="Units", font=('calibre', 15, 'bold'), bg='#0A3D62', fg="#6ab04c",
                       width=5, anchor="w").place(x=288, y=210)
radio_g = tk.Radiobutton(frame2, text="Grams(g)", padx=5, bg='#A1AAB5', variable=radio_var, value=1).pack(anchor=tk.W)
radio_kg = tk.Radiobutton(frame2, text="Kilograms(kg)", padx=5, bg='#A1AAB5', variable=radio_var, value=2).pack(anchor=tk.W)
radio_oz = tk.Radiobutton(frame2, text="Ounces(oz)", padx=5, bg='#A1AAB5', variable=radio_var, value=3).pack(anchor=tk.W)
radio_lbs = tk.Radiobutton(frame2, text="Pounds(lb)", padx=5, bg='#A1AAB5', variable=radio_var, value=4).pack(anchor=tk.W)
radio_var.set(1)
frame2.place(x=258, y=240)


def disable_buttons():
    print("disabling radio")
    for child in frame2.winfo_children():
        if child.winfo_class() == 'Radiobutton':
            child['state'] = 'disabled'
    for child in root.winfo_children():
        if child.winfo_class() == 'Button':
            child['state'] = 'disabled'
def enable_buttons():
    print("enabling radio")
    for child in frame2.winfo_children():
        if child.winfo_class() == 'Radiobutton':
            child['state'] = 'normal'
    for child in root.winfo_children():
        if child.winfo_class() == 'Button':
            child['state'] = 'normal'


def unit_str(long=False):
    radio_var.get()
    if long is False:
        if radio_var.get() == 1:
            unit = "(g)"
        if radio_var.get() == 2:
            unit = "(kg)"
        if radio_var.get() == 3:
            unit = "(oz)"
        if radio_var.get() == 4:
            unit = "(lb)"
    else:
        if radio_var.get() == 1:
            unit = "Grams"
        if radio_var.get() == 2:
            unit = "Kilograms"
        if radio_var.get() == 3:
            unit = "Ounces"
        if radio_var.get() == 4:
            unit = "Pounds"
    return unit


def set_equations(event=None):
    global m_AvP, b_AvP, m_PvA, b_PvA, amount, price, n_entries, ppa, ppa_units

    mavpdir = os.path.join(os.path.expanduser("~/Documents/hoswoo_calculator/m_AvP_data.dat"))  # Probably the dumbest way to do this
    bavpdir = os.path.join(os.path.expanduser("~/Documents/hoswoo_calculator/b_AvP_data.dat"))
    mpvadir = os.path.join(os.path.expanduser("~/Documents/hoswoo_calculator/m_PvA_data.dat"))
    bpvadir = os.path.join(os.path.expanduser("~/Documents/hoswoo_calculator/b_PvA_data.dat"))
    pricedir = os.path.join(os.path.expanduser("~/Documents/hoswoo_calculator/prices.dat"))
    amountdir = os.path.join(os.path.expanduser("~/Documents/hoswoo_calculator/amounts.dat"))
    nentriesdir = os.path.join(os.path.expanduser("~/Documents/hoswoo_calculator/num_of_entries.dat"))
    priceperozdir = os.path.join(os.path.expanduser("~/Documents/hoswoo_calculator/price_per_amount.dat"))

    if os.path.exists(mavpdir) and os.path.exists(bavpdir) and os.path.exists(mpvadir) \
            and os.path.exists(bpvadir) and os.path.exists(nentriesdir) and os.path.exists(pricedir) \
            and os.path.exists(amountdir) and os.path.exists(priceperozdir):
        os.chdir(os.path.expanduser('~/Documents/hoswoo_calculator/'))
        f = open("m_AvP_data.dat", "r")  # Get Data
        if f.mode == "r":
            vars_series = f.read()  # Thank you stack exchange
            m_AvP = [float(item) for item in vars_series.split()]
            print("mAvP:", m_AvP)
        f = open("b_AvP_data.dat")
        if f.mode == "r":
            vars_series = f.read()
            b_AvP = [float(item) for item in vars_series.split()]
            print("bAvP:", b_AvP)
        f = open("m_PvA_data.dat")
        if f.mode == "r":
            vars_series = f.read()
            m_PvA = [float(item) for item in vars_series.split()]
            print("mPvA:", m_PvA)
        f = open("b_PvA_data.dat")
        if f.mode == "r":
            vars_series = f.read()
            b_PvA = [float(item) for item in vars_series.split()]
            print("bPvA:", b_PvA)
        f = open("amounts.dat")
        if f.mode == "r":
            vars_series = f.read()
            amount = [float(item) for item in vars_series.split()]
            print("amounts:", amount)
        f = open("prices.dat")
        if f.mode == "r":
            vars_series = f.read()
            price = [float(item) for item in vars_series.split()]
            print("prices:", price)
        f = open("num_of_entries.dat")
        if f.mode == "r":
            n_entries = int(f.read())   # This is for calculator use
            print("num of entries: ", n_entries)
        f = open("price_per_amount.dat")
        if f.mode == "r":
            ppa = float(linecache.getline('price_per_amount.dat', 1))
            ppa_units = unit_str(False)
            print("PPA:", ppa)
            print("PPA UNITS:", ppa_units)
        insert_text("Your settings have been loaded.", True)
    else:
        insert_text("You have insufficient/invalid data.\nClick get equations to set this up.\n")


set_equations()


def clear_widgets():
    for child in frame3.winfo_children():
        child.destroy()
    next_btn['state'] = 'normal'
    print(next_btn.winfo_exists())
    keyboard.remove_hotkey('ctrl+alt+h')


def make_widgets():
    global label, price_entry, amount_entry, price_per_amount_entry, price_per_amount_var
    label = []
    price_entry = []
    amount_entry = []
    graph_PvA_btn = tk.Button(frame3, text='PvA', bg="#2C3335", width=8, fg="#7ddeff", command=graph_p_vs_a)
    graph_AvP_btn = tk.Button(frame3, text='AvP', bg="#2C3335", width=8, fg="#7ddeff", command=graph_a_vs_p)
    save_btn = tk.Button(frame3, text='Save', bg="#2C3335", width=8, fg="#7ddeff", command=save_equations)

    graph_PvA_btn.grid(row=num_of_entries + 2, column=2, pady=5)
    graph_AvP_btn.grid(row=num_of_entries + 2, column=3)
    save_btn.grid(row=num_of_entries + 2, column=4)
    price_label = tk.Label(frame3, text="Price($)", font=('calibre', 10, 'bold'), bg="#A1AAB5", width=11, fg="#2B3139")
    amount_label = tk.Label(frame3, text="Amount" + unit_str(False), font=('calibre', 10, 'bold'), bg="#A1AAB5", width=11,
                            fg="#2B3139")
    point_label = tk.Label(frame3, text="P#", font=('calibre', 10, 'bold'), bg="#A1AAB5", width=4, fg="#2B3139")
    point_label.grid(row=1, column=1)
    price_label.grid(row=1, column=2)
    amount_label.grid(row=1, column=3)
    price_per_amount_var = tk.StringVar()
    price_per_amount_entry = tk.Entry(frame3, textvariable=price_per_amount_var, width=8)
    price_per_amount_entry.grid(row=2, column=4)
    price_per_amount_label = tk.Label(frame3, text="Price/" + unit_str(False), font=('calibre', 10, 'bold'), bg="#A1AAB5", height=1, fg="#2B3139")
    price_per_amount_label.grid(row=1, column=4)

    price_per_amount_entry.config(validate="key", validatecommand=(reg, '%P'))

    for i in range(0, num_of_entries):  # For loop to create all labels, entries, and variables
        price_var.append(tk.StringVar())
        lbl = tk.Label(frame3, text="P" + str(i + 1), font=('calibre', 8, 'bold'), bg="#A1AAB5", height=1,
                       fg="#2B3139", justify="right")
        label.append(lbl)  # P#
        label[i].grid(row=2 + i, column=1)
        price_entry.append(tk.Entry(frame3, width=5))
        price_entry[i].grid(row=2 + i, column=2)
        amount_entry.append(tk.Entry(frame3, width=5))
        amount_entry[i].grid(row=2 + i, column=3)

    for i in range(num_of_entries):  # Fill the lists with something
        lines.append(i)
        price.append(i)
        amount.append(i)
        point1.append(i)
        point2.append(i)
        m_var_PvA.append(i)
        b_var_PvA.append(i)
        m_var_AvP.append(i)
        b_var_AvP.append(i)
    keyboard.add_hotkey('ctrl+alt+h', set_sample_data)


def set_sample_data():
    price_entry[0].insert(tk.INSERT, "10")
    price_entry[1].insert(tk.INSERT, "45")
    price_entry[2].insert(tk.INSERT, "80")
    price_entry[3].insert(tk.INSERT, "140")
    price_entry[4].insert(tk.INSERT, "250")
    amount_entry[0].insert(tk.INSERT, "0.7")
    amount_entry[1].insert(tk.INSERT, "3.5")
    amount_entry[2].insert(tk.INSERT, "7")
    amount_entry[3].insert(tk.INSERT, "14")
    amount_entry[4].insert(tk.INSERT, "28")
    price_per_amount_entry.insert(tk.INSERT, "6.5848")


def remove_extra_data():
    if len(price) > num_of_entries: # Remove excess entries
        del price[num_of_entries + 1:len(price)]
    if len(amount) > num_of_entries:
        del amount[num_of_entries + 1:len(amount)]
    if len(m_var_PvA) > num_of_entries:
        del m_var_PvA[num_of_entries:len(m_var_PvA)]
    if len(b_var_PvA) > num_of_entries:
        del b_var_PvA[num_of_entries:len(b_var_PvA)]
    if len(m_var_AvP) > num_of_entries:
        del m_var_AvP[num_of_entries:len(m_var_AvP)]
    if len(b_var_AvP) > num_of_entries:
        del b_var_AvP[num_of_entries:len(b_var_AvP)]
    print("mvar_Pva:", m_var_PvA, "bvar_Pva: ", b_var_PvA, sep="")
    print("mvar_Avp:", m_var_AvP, "bvar_Avp:", b_AvP, sep="")
    print("price:", price, "amount:", amount, sep="")


def equation_finder(event=None): # When user clicks next/back button
    global num_of_entries, text1, price_per_amount, next_expanded, next_btn, frame3, label
    num_of_entries = int(entries_entry.get())   # This is for equation finder use only
    print("# of entries: ", entries_entry.get())
    if int(entries_entry.get()) > 30:
        insert_text("Too many entries, maximum is 30.")
    if int(entries_entry.get()) < 1:
        insert_text("You need at least 1 entry.")
    if num_of_entries <= 10:
        root.geometry("840x340")  # Make window bigger to show Equation Finder
        frame3.config(height=20, width=15)
    if 10 < num_of_entries <= 20:
        root.geometry("840x480")
        frame3.config(height=40, width=15)
    if 20 < num_of_entries <= 30:
        root.geometry("840x670")
        frame3.config(height=60)

    if not next_expanded:   # If clicking next
        next_expanded = True
        next_btn.config(text="Back")
        make_widgets()
        disable_buttons()

    else:   # If clicking back
        root.geometry(base_size)    # Go back to starting size
        next_expanded = False
        next_btn.config(text="Next")
        clear_widgets()
        enable_buttons()
# Frame 1 = get equations
next_btn = tk.Button(frame1, text='Next', bg="#2C3335", width=5, fg="#7ddeff", command=equation_finder)
get_equations_label = tk.Label(root, text="Get Equations", font=('calibre', 15, 'bold'), bg='#0A3D62', fg="#6ab04c",
                               width=12, anchor="w").place(x=372, y=210)
data_label = tk.Label(root, text="Data", font=('calibre', 15, 'bold'), bg='#0A3D62', fg="#6ab04c",
                      width=12, anchor="w").place(x=526, y=10)
entry_label.grid(column=0, row=1)
entries_entry.grid(column=0, row=2)
next_btn.grid(column=0, row=3)
frame1.place(x=378, y=235)

# Unit related stuff

def convert_to_g(x, from_unit):
    radio_var.get()
    if from_unit == 'g':     # (g)
        y = x
    if from_unit == 'kg':  # (kg)
        y = x * 1000
    if from_unit == 'oz':   # (oz)
        y = x * 28.34952
    if from_unit == 'lb':    # (lbs)
        y = x * 453.59237
    return y
def convert_to_oz(x, from_unit):
    radio_var.get()
    if from_unit == 'g':  # (g)
        y = x / 28.34952
    if from_unit == 'kg':   # (kg)
        y = x * 35.27396195
    if from_unit == 'oz':    # (oz)
        y = x
    if from_unit == 'lb':   # (lbs)
        y = x * 16
    return y
def convert_to_kg(x, from_unit):
    radio_var.get()
    if from_unit == 'g':    # (g)
        y = x / 1000
    if from_unit == 'kg':   # (kg)
        y = x
    if from_unit == 'oz':    # (oz)
        y = x * 0.02834952
    if from_unit == 'lb':   # (lb)
        y = x / 2.205
    return y
def convert_to_lb(x, from_unit):
    radio_var.get()
    if from_unit == 'g':   # (g)
        y = x / 453.59237
    if from_unit == 'kg':   # (kg)
        y = x / 0.45359237
    if from_unit == 'oz':   # (oz)
        y = x / 16
    if from_unit == 'lb':    # (lb)
        y = x
    return y

# Graphing
def graph_p_vs_a(event=None):  # graph a function
    global price_per_amount, price_per_amount_entry
    price_per_amount = float(price_per_amount_entry.get())
    insert_text("Graphing and getting the equations...\n")
    insert_text("y = Amount" + unit_str(False) + " x = Price($) \ny = (m * x) + b", False)
    fig = plt.figure(figsize=(10, 5))
    axs = plt.axes()
    fig.suptitle('Price($) versus Amount' + unit_str(False))
    axs.set_xlabel('x = Price($)')
    axs.set_ylabel('y = Amount' + unit_str(False))
    c = np.array([(1, 0, 0, 1), (1, 0, 0, 1), (1, 0, 0, 1), (1, 0, 0, 1), (1, 0, 0, 1), (1, 0, 0, 1)])
    c2 = np.array([(0, 0, 0, 1)])
    plt.plot(0, 0, marker='o', color='b')  # plot 0,0
    def own_price():
        print(price_per_amount * amount[num_of_entries - 1])    # Index is - 1 here because I manually plotted (0,0)
        x_values = [0, price_per_amount * amount[num_of_entries - 1]]
        y_values = [0, amount[num_of_entries - 1]]
        m = price_per_amount
        plt.plot(x_values, y_values, label='Your Price vs. Amount' + unit_str(False) + ': y = ' + "({:,.4f})x".format(m))
        #print(p_own_x)

    def first_point():  # Function to plug in the first point
        m = amount[0] / price[0]  # m = (y2-y1)/(x2-x1)
        b = amount[0] - m * (price[0])  # b = y - mx
        m_var_PvA[0] = m
        b_var_PvA[0] = b
        # print("y = (" + str(m) + ")x + " + str(b))
        lines = [[(0, 0), (price[0], amount[0])]]
        lc = mc.LineCollection(lines, colors=c2, linewidths=1)
        equation_str = str(0) + " to " + str(price[0]) + ": y = " + "({:,.4f})x".format(m) + " + (" + "{:,.4f})".format(b)
        x_values = [0, price[0]]
        y_values = [0, amount[0]]
        plt.plot(x_values, y_values, label=equation_str)
        insert_text(equation_str, False)
    try:
        for i in range(0, num_of_entries):  # Get all entries and set them to price[] and amount[]
            price[i] = float(price_entry[i].get())
            amount[i] = float(amount_entry[i].get())
            price_entry[i].config(validate="key", validatecommand=(reg, '%P'))
            amount_entry[i].config(validate="key", validatecommand=(reg, '%P'))
            print("P" + str(i + 1) + ": " + str(price[i]) + " A" + str(i + 1) + ": " + str(amount[i]))
    except ValueError:
        insert_text("Invalid input(s).")
    first_point()
    for i in range(0, num_of_entries - 1):
        # This for loop below does not account for P(0,0), this has to be done manually.
        plt.plot(price[i], amount[i], marker='o',color='b')  # Index starts at 0 here.
        plt.plot(price[i + 1], amount[i + 1], marker='o',color='b')  # x = price, y = amount
        m = (amount[i + 1] - amount[i]) / (price[i + 1] - price[i])  # m = (y2-y1)/(x2-x1)
        b = amount[i] - (m * price[i])  # b = (m * x)
        m_var_PvA[i + 1] = m
        b_var_PvA[i + 1] = b
        x = np.array(axs.get_xlim())  # This sets axis range based on the highest and lowest values of x
        y = m * x + b  # y = mx + b
        equation_str = str(price[i]) + " to " + str(price[i + 1]) + ": y = " + "({:,.4f})x".format(m) + " + (" + "{:,.4f})".format(b)
        insert_text(equation_str, False)
        print(equation_str)
        lines[i] = [[(price[i], amount[i]), (price[i], amount[i])]]  # This sets the lines.
        lc = mc.LineCollection(lines[i], colors=c, linewidths=2)  # Adds the lines to a collection.
        axs.add_collection(lc)  # Add collections to graph
        p1 = [price[i], amount[i]]
        p2 = [price[i + 1], amount[i + 1]]
        x_values = [p1[0], p2[0]]
        y_values = [p1[1], p2[1]]
        plt.plot(x_values, y_values, label=equation_str)
    own_price()
    # To show user how much they pay

    cursor = Cursor(axs)  # Thank you Stack Exchange
    fig.canvas.mpl_connect('motion_notify_event', cursor.mouse_move)
    plt.legend(loc="upper left")  # Show legend
    plt.show()  # Show plot


def graph_a_vs_p(event=None):  # graph a function
    global price_per_amount
    price_per_amount = float(price_per_amount_entry.get())
    insert_text("Graphing and getting the equations...")  # False indicates that we don't want a time stamp
    insert_text("x = Price($) y = Amount" + unit_str(False) + "\ny = (m * x) + b", False)
    fig = plt.figure(figsize=(10, 5))
    axs = plt.axes()
    fig.suptitle('Amount' + unit_str(False) + ' versus Price($)')
    axs.set_ylabel('y = Price($)')
    axs.set_xlabel('x = Amount' + unit_str(False))
    c = np.array([(1, 0, 0, 1), (1, 0, 0, 1), (1, 0, 0, 1), (1, 0, 0, 1), (1, 0, 0, 1), (1, 0, 0, 1)])
    c2 = np.array([(0, 0, 0, 1)])
    plt.plot(0, 0, marker='o', color='b')  # plot 0,0
    def own_amount():
        x_values = [0, amount[num_of_entries - 1]]
        y_values = [0, price_per_amount * amount[num_of_entries - 1]]
        m = price[num_of_entries - 1] / (amount[num_of_entries - 1] * price_per_amount)
        plt.plot(x_values, y_values, label='Your Amount vs Price: y = ' + "({:,.4f})x".format(m))
    def first_point():  # Function to plug in the first point
        m = price[0] / amount[0]  # m = (y2-y1)/(x2-x1)
        b = price[0] - m * (amount[0])  # b = y - mx
        m_var_AvP[0] = m
        b_var_AvP[0] = b
        # print("y = (" + str(m) + ")x + " + str(b))
        lines = [[(0, 0), (amount[0], price[0])]]
        lc = mc.LineCollection(lines, colors=c2, linewidths=1)
        equation_str = str(0) + " to " + str(amount[0]) + ": y = " + "({:,.4f})x".format(m) + \
            " + (" + "{:,.4f})".format(b)
        # p1 = (0,0), Just manually typing in 0.
        p2 = [amount[0], price[0]]
        x_values = [0, p2[0]]
        y_values = [0, p2[1]]
        plt.plot(x_values, y_values, label=equation_str)
        insert_text(equation_str, False)

    for i in range(0, num_of_entries):  # Get all entries and set them to price[]
        price[i] = float(price_entry[i].get())
        amount[i] = float(amount_entry[i].get())
        price_entry[i].config(validate="key", validatecommand=(reg, '%P'))
        amount_entry[i].config(validate="key", validatecommand=(reg, '%P'))
        print(" A" + str(i + 1) + ": " + str(amount[i]) + "P" + str(i + 1) + ": " + str(price[i]))

    first_point()
    # This for loop below does not account for P(0,0), this has to be done manually.
    for i in range(0, num_of_entries - 1):
        plt.plot(amount[i], price[i], marker='o', color='b')  # Index starts at 0 here.
        plt.plot(amount[i + 1], price[i + 1], marker='o', color='b')  # x = price, y = amount
        m = ((price[i + 1] - price[i]) / (amount[i + 1] - amount[i]))  # m = (y2-y1)/(x2-x1)
        b = price[i] - (m * amount[i])  # b = y -  (m * x)
        m_var_AvP[i + 1] = m
        b_var_AvP[i + 1] = b
        x = np.array(axs.get_xlim())  # This sets axis range based on the highest and lowest values of x
        y = m * x + b  # y = mx + b
        equation_str = str(amount[i]) + " to " + str(amount[i + 1]) + ": y = " + "({:,.4f})x".format(m) + \
            " + (" + "{:,.4f})".format(b)
        insert_text(equation_str, False)
        print(equation_str)
        lines[i] = [[(amount[i], price[i]),
                     (amount[i], price[i])]]  # This sets the lines.
        lc = mc.LineCollection(lines[i], colors=c, linewidths=2)  # Adds the lines to a collection.
        axs.add_collection(lc)  # Add collections to graph
        p1 = [amount[i], price[i]]
        p2 = [amount[i + 1], price[i + 1]]
        x_values = [p1[0], p2[0]]
        y_values = [p1[1], p2[1]]
        plt.plot(x_values, y_values, label=equation_str)
    own_amount()
    cursor = Cursor(axs)
    fig.canvas.mpl_connect('motion_notify_event', cursor.mouse_move)
    plt.legend(loc="upper left")  # Show legend
    plt.show()  # Show plot


def save_equations(event=None):
    global text1, price_per_amount, price, amount
    price.insert(0, 0)  # "Insert into index 0: 0"
    amount.insert(0, 0)
    remove_extra_data()

    doc_path = os.path.join(os.path.expanduser("~"), 'Documents')
    calc_path = os.path.join(doc_path, 'hoswoo_calculator')
    if not os.path.exists(os.path.join(doc_path, 'hoswoo_calculator')):  # Make folder in documents folder
        os.mkdir('hoswoo_calculator')
        print("Made folder in documents")
    else:   # Unless it already is there
        print("Did not make folder because it already exists")
    os.chdir(doc_path)
    #userdoc = os.path.join(os.path.expanduser("~"), 'Documents')
    entriesdir = os.path.join(os.path.expanduser("~/Documents/hoswoo_calculator/num_of_entries.dat"))
    priceperamountdir = os.path.join(os.path.expanduser("~/Documents/hoswoo_calculator/price_per_amount.dat"))
    np.savetxt(os.path.join(calc_path, 'm_AvP_data.dat'), m_var_AvP)
    np.savetxt(os.path.join(calc_path, 'b_AvP_data.dat'), b_var_AvP)
    np.savetxt(os.path.join(calc_path, 'm_PvA_data.dat'), m_var_PvA)
    np.savetxt(os.path.join(calc_path, 'b_PvA_data.dat'), b_var_PvA)
    np.savetxt(os.path.join(calc_path, 'prices.dat'), price)
    np.savetxt(os.path.join(calc_path, 'amounts.dat'), amount)

    with open(entriesdir, 'w') as f:
        f.write(str(num_of_entries))
    with open(priceperamountdir, 'w') as f:
        f.write(str(price_per_amount) + "\n" + unit_str(False))
    insert_text("Data was saved in your documents folder.")
    set_equations()
    print("Data was saved.")

# Calculators
def calculate_product_use_equations(event=None):
    global n_entries, amount, m_PvA, b_PvA, price, ppa, ppa_units

    try:
        pay = float(pay_entry_use_equations.get())
        final_rate = amount[n_entries] / price[n_entries]
        if pay <= 0:
            print("You must enter a number greater than 0.\n")
            insert_text("You must enter a number greater than 0.")
        for i in range(0, n_entries):
            if price[i] < pay <= price[i + 1]:
                product = (m_PvA[i] * pay) + b_PvA[i]  # y = mx + b
                print("m", m_PvA[i], "b", b_PvA[i])
        print("ppa units:", ppa_units)
        if pay > price[n_entries]:
            product = final_rate * pay

        print("product before conversion:", product)
        radio_var.get()
        # This is quite ugly lol
        if ppa_units.__contains__("(g)"):  # If user saved data as grams
            if radio_var.get() == 1:
                converted_product = convert_to_g(product, 'g')
            if radio_var.get() == 2:
                converted_product = convert_to_kg(product, 'g')
            if radio_var.get() == 3:
                converted_product = convert_to_oz(product, 'g')
            if radio_var.get() == 4:
                converted_product = convert_to_lb(product, 'g')
        if ppa_units.__contains__("(kg)"):  # If user saved data as kilograms
            if radio_var.get() == 1:
                converted_product = convert_to_g(product, 'kg')
            if radio_var.get() == 2:
                converted_product = convert_to_kg(product, 'kg')
            if radio_var.get() == 3:
                converted_product = convert_to_oz(product, 'kg')
            if radio_var.get() == 4:
                converted_product = convert_to_lb(product, 'kg')
        if ppa_units.__contains__("(oz)"): # If user saved data as ounces
            if radio_var.get() == 1:
                converted_product = convert_to_g(product, 'oz')
            if radio_var.get() == 2:
                converted_product = convert_to_kg(product, 'oz')
            if radio_var.get() == 3:
                converted_product = convert_to_oz(product, 'oz')
            if radio_var.get() == 4:
                converted_product = convert_to_lb(product, 'oz')
        if ppa_units.__contains__("(lb)"): # If user saved data as grams
            if radio_var.get() == 1:
                converted_product = convert_to_g(product, 'lb')
            if radio_var.get() == 2:
                converted_product = convert_to_kg(product, 'lb')
            if radio_var.get() == 3:
                converted_product = convert_to_oz(product, 'lb')
            if radio_var.get() == 4:
                converted_product = convert_to_lb(product, 'lb')
        print("product converted:", converted_product)
        ourCost = ppa * product
        profit = pay - ourCost
        product_str = "%g"%converted_product + unit_str(False)  # "%g"% gets rid of trailing 0
        radio_var.get()
        insert_text("You should give " + product_str + " for " + "${:,.2f}".format(pay)
                    + ".\nCost: " + "${:,.2f}".format(ourCost)
                    + "\nProfit: " + "${:,.2f}".format(profit))
        pay_var_use_equations.set("")
    except ValueError:
        print("ValueError")
        insert_text("Invalid input for pay amount.")
    # End calculate_pay


def calculate_pay_use_equations(event=None):
    global n_entries, amount, m_AvP, b_AvP, price, ppa, ppa_units
    try:
        product = float(product_var_use_equations.get())
        radio_var.get()
        if price_per_amount_units.__contains__("(g)"):  # If user saved data as grams
            if radio_var.get() == 1:
                converted_product = convert_to_g(product, 'g')
            if radio_var.get() == 2:
                converted_product = convert_to_g(product, 'kg')
            if radio_var.get() == 3:
                converted_product = convert_to_g(product, 'oz')
            if radio_var.get() == 4:
                converted_product = convert_to_g(product, 'lb')
        if price_per_amount_units.__contains__("(kg)"):  # If user saved data as kilograms
            if radio_var.get() == 1:
                converted_product = convert_to_kg(product, 'g')
            if radio_var.get() == 2:
                converted_product = convert_to_kg(product, 'kg')
            if radio_var.get() == 3:
                converted_product = convert_to_kg(product, 'oz')
            if radio_var.get() == 4:
                converted_product = convert_to_kg(product, 'lb')
        if price_per_amount_units.__contains__("(oz)"):  # If user saved data as ounces
            if radio_var.get() == 1:
                converted_product = convert_to_oz(product, 'g')
            if radio_var.get() == 2:
                converted_product = convert_to_oz(product, 'kg')
            if radio_var.get() == 3:
                converted_product = convert_to_oz(product, 'oz')
            if radio_var.get() == 4:
                converted_product = convert_to_oz(product, 'lb')
        if price_per_amount_units.__contains__("(lb)"):  # If user saved data as pounds
            if radio_var.get() == 1:
                converted_product = convert_to_lb(product, 'g')
            if radio_var.get() == 2:
                converted_product = convert_to_lb(product, 'kg')
            if radio_var.get() == 3:
                converted_product = convert_to_lb(product, 'oz')
            if radio_var.get() == 4:
                converted_product = convert_to_lb(product, 'lb')
        for i in range(0, n_entries):
            if amount[i] < converted_product <= amount[i + 1]:  # y = pay, x = amount
                pay = (m_AvP[i] * converted_product) + b_AvP[i]  # y = mx + b
                print("m", m_AvP[i], "b", b_AvP[i])
        final_rate = price[n_entries] / amount[n_entries]
        if converted_product > amount[n_entries]:
            pay = final_rate * converted_product

        if product <= 0:
            print("You must enter a number greater than 0.\n")
            insert_text("You must enter a number greater than 0.")
        print("radio_var:", radio_var.get())
        print("product before conversion:", product, unit_str(False))
        print("product after conversion:", converted_product, ppa_units)
        product_str = "%g"%product

        ourCost = ppa * converted_product
        profit = pay - ourCost
        print("You should charge ", "${:,.2f}".format(pay), " for ", product_str + unit_str(False),
                                                                              "\n-----------------------------------------",
              sep="")
        insert_text("You should charge " + "${:,.2f}".format(pay) + " for " + product_str + unit_str(False) +
                    "\nCost: " + "${:,.2f}".format(ourCost) + "\nProfit: " + "${:,.2f}".format(profit))
        product_var_use_equations.set("")
    except ValueError:
        print("ValueError")
        insert_text("Invalid input for product amount.")


def calculate_profit_own_prices(event=None):
    global ppa, ppa_units
    try:
        pay = float(pay_var_own_prices.get())
        product = float(product_var_own_prices.get())
        if ppa_units.__contains__("(g)"):  # If user saved data as grams
            if radio_var.get() == 1:
                converted_product = convert_to_g(product, 'g')
            if radio_var.get() == 2:
                converted_product = convert_to_g(product, 'kg')
            if radio_var.get() == 3:
                converted_product = convert_to_g(product, 'oz')
            if radio_var.get() == 4:
                converted_product = convert_to_g(product, 'lb')
        if ppa_units.__contains__("(kg)"):  # If user saved data as kilograms
            if radio_var.get() == 1:
                converted_product = convert_to_kg(product, 'g')
            if radio_var.get() == 2:
                converted_product = convert_to_kg(product, 'kg')
            if radio_var.get() == 3:
                converted_product = convert_to_kg(product, 'oz')
            if radio_var.get() == 4:
                converted_product = convert_to_kg(product, 'lb')
        if ppa_units.__contains__("(oz)"): # If user saved data as ounces
            if radio_var.get() == 1:
                converted_product = convert_to_oz(product, 'g')
            if radio_var.get() == 2:
                converted_product = convert_to_oz(product, 'kg')
            if radio_var.get() == 3:
                converted_product = convert_to_oz(product, 'oz')
            if radio_var.get() == 4:
                converted_product = convert_to_oz(product, 'lb')
        if ppa_units.__contains__("(lb)"): # If user saved data as pounds
            if radio_var.get() == 1:
                converted_product = convert_to_lb(product, 'g')
            if radio_var.get() == 2:
                converted_product = convert_to_lb(product, 'kg')
            if radio_var.get() == 3:
                converted_product = convert_to_lb(product, 'oz')
            if radio_var.get() == 4:
                converted_product = convert_to_lb(product, 'lb')
        print(ppa_units)
        if pay <= 0:
            insert_text("Number must be greater than 0.")
        if product <= 0:
            insert_text("\nValue must be greater than 0.")
        round(product, 3)
        ourCost = ppa * converted_product
        profit = pay - ourCost
        print("\nGiving ", "%g"%product + unit_str() + " for ", "${:,.2f}".format(pay) + " will" +
              "\nCost: ", "${:,.2f}".format(ourCost) +
              "\nProfit:", "${:,.2f}".format(profit) +
              "\n-----------------------------------------", sep="")
        insert_text("Giving " + "%g"%product + unit_str() + " for " + "${:,.2f}".format(pay) + " will" +
                    "\nCost: " + "${:,.2f}".format(ourCost) +
                    "\nProfit:" + "${:,.2f}".format(profit))
    except ValueError:
        print("ValueError")
        insert_text("Invalid input for product or pay amount.\n")


price_calc_label = tk.Label(root, text='Price Finder',
                            font=('calibre', 15, 'bold'), bg='#0A3D62', fg="#6ab04c", width=10, anchor="w")
# use_equations' stuff
use_equations_label = tk.Label(root, text=' Use Equations',
                               font=('calibre', 10, 'bold'), bg='#0A3D62', fg="#55efc4")
pay_label_use_equations = tk.Label(root, text='Pay($)',
                                   font=('calibre', 10, 'bold'), bg='#0A3D62', fg="#7ddeff", width=8, anchor="w")
# entry box
pay_entry_use_equations = tk.Entry(root, textvariable=pay_var_use_equations,
                                   font=('calibre', 10, 'normal'), width=8)
pay_entry_use_equations.config(validate="key", validatecommand=(reg, '%P'))
# So the user can press enter instead of clicking calculate
pay_entry_use_equations.bind("<Return>", calculate_product_use_equations)
product_label_use_equations = tk.Label(root, text='Amount',
                                       font=('calibre', 10, 'bold'), bg='#0A3D62', fg="#7ddeff", width=8, anchor="w")
product_entry_use_equations = tk.Entry(root, textvariable=product_var_use_equations,
                                       font=('calibre', 10, 'normal'), width=8)
product_entry_use_equations.config(validate="key", validatecommand=(reg, '%P'))
# So the user can press enter instead of clicking calculate
product_entry_use_equations.bind("<Return>", calculate_pay_use_equations)
# own_prices' stuff
own_prices_label = tk.Label(root, text='Custom Price',
                            font=('calibre', 10, 'bold'), bg='#0A3D62', fg="#55efc4")

pay_label_own_prices = tk.Label(root, text='Pay($)',
                                font=('calibre', 10, 'bold'), bg='#0A3D62', fg="#7ddeff", width=8, anchor="w")

pay_entry_own_prices = tk.Entry(root,
                                textvariable=pay_var_own_prices,
                                font=('calibre', 10, 'normal'), width=8)
pay_entry_own_prices.config(validate="key", validatecommand=(reg, '%P'))
# So the user can press enter instead of clicking calculate
# pay_entry_own_prices.bind("<Return>", calculate_profit_own_prices)

product_label_own_prices = tk.Label(root,
                                    text='Amount',
                                    font=('calibre', 10, 'bold'), bg='#0A3D62', fg="#7ddeff", width=8, anchor="w")

product_entry_own_prices = tk.Entry(root,
                                    textvariable=product_var_own_prices,
                                    font=('calibre', 10, 'normal'), width=8)
product_entry_own_prices.config(validate="key", validatecommand=(reg, '%P'))
pay_btn_use_equations = tk.Button(root, text='Calculate',
                                  command=calculate_product_use_equations, bg="#2C3335", fg="#7ddeff")

pay_btn_own_prices = tk.Button(root, text='Calculate',
                               command=calculate_profit_own_prices, bg="#2C3335", fg="#7ddeff")
# So the user can press enter instead of clicking calculate
pay_entry_own_prices.bind("<Return>", calculate_profit_own_prices)

product_btn = tk.Button(root, text='Calculate',
                        command=calculate_pay_use_equations, fg="#7ddeff", bg="#2C3335")

# So the user can press enter instead of clicking calculate
product_entry_own_prices.bind("<Return>", calculate_profit_own_prices)



pay_entry_own_prices = tk.Entry(root,
                                textvariable=pay_var_own_prices,
                                font=('calibre', 10, 'normal'), width=8)
pay_entry_own_prices.config(validate="key", validatecommand=(reg, '%P'))

# Price_calc stuff
price_calc_label.grid(row=0, column=1)
use_equations_label.grid(row=1, column=1)
pay_label_use_equations.grid(row=2, column=1)
pay_entry_use_equations.grid(row=2, column=2)
pay_btn_use_equations.grid(row=2, column=3)
product_label_use_equations.grid(row=3, column=1)
product_entry_use_equations.grid(row=3, column=2)
product_btn.grid(row=3, column=3)
own_prices_label.grid(row=4, column=1, columnspan=1)
pay_label_own_prices.grid(row=5, column=1)
pay_entry_own_prices.grid(row=5, column=2)
pay_btn_own_prices.grid(row=6, column=3, padx=2)
product_label_own_prices.grid(row=6, column=1)
product_entry_own_prices.grid(row=6, column=2)

root.mainloop()







