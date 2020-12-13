import pyautogui, random, keyboard, datetime
import tkinter as tk

root = tk.Tk()
root.configure(bg='#0A3D62')    # Change BG color
root.title('Autoclicker')

dev_label = tk.Label(root, text='Made by Hoswoo', font=('calibre', 10, 'bold'), bg="#0A3D62", fg="#7ddeff")
# setting the windows size
root.geometry("530x320")
# canvas = tk.Canvas(root, height=320, width=240,bg="#263D42")
# canvas.pack()

min_var = tk.StringVar()
max_var = tk.StringVar()


def checkNum(n):    # Ensure input is a number
    try:
        float(n)
    except:
        return False
    return True


min_var_entry = tk.Entry(root, textvariable=min_var, font=('calibre', 10, 'normal'), width=8)
max_var_entry = tk.Entry(root, textvariable=max_var, font=('calibre', 10, 'normal'), width=8)

min_var_entry.insert(tk.INSERT, "0.0")
max_var_entry.insert(tk.INSERT, "1.0")

reg = root.register(checkNum) # Make sure to check this register AFTER initializing the entry widgets
min_var_entry.config(validate="key", validatecommand=(reg, '%P'))    # Only call when a "key" is pressed
max_var_entry.config(validate="key", validatecommand=(reg, '%P'))
# NOTE FOR FUTURE REFERENCE
# When using global inside a function, you must always specify that it's a global variable
# inside of every function you use it in. Global functions are defined outside the scope
# of all functions.
running = False


def start_clicking_task(event=None):
    global running
    if running is False:
        running = True
        start_clicking()


def start_clicking(event=None):
    global running
    text1.config(state="normal")

    if running:
        min = min_var.get()
        max = max_var.get()
        text1.insert(tk.INSERT, "\n" + "(" + '{:%H:%M:%S}'.format(datetime.datetime.now()) + ")")
        try:    # Show exception to user
            min = float(min)
            max = float(max)
        except ValueError:
            text1.insert(tk.INSERT, "One or both of your inputs are invalid.")
        random_range = random.uniform(min, max)
        random_range_s_to_ms = int(random_range * 1000)     # Convert seconds to ms
        range_str_s = "{:,.2f}s".format(random_range)
        range_str_ms = "{:,.2f}ms".format(random_range_s_to_ms)
        print("(" +'{:%H:%M:%S}'.format(datetime.datetime.now()))
        text1.insert(tk.INSERT, "\nTime since last click: " + range_str_s + " (" + range_str_ms + ")\n")
        pyautogui.click()
        root.after(random_range_s_to_ms, start_clicking)    # Recursively call start_clicking`
    text1.see("end")
    text1.config(state="disabled")


def stop_clicking(event=None):
    global running
    text1.config(state="normal")
    if running is True:
        text1.insert(tk.INSERT, "\n" + "(" + '{:%H:%M:%S}'.format(datetime.datetime.now()) + ")")
        text1.insert(tk.INSERT, "\nStopping...\n")
        running = False
    text1.see("end")
    text1.config(state="disabled")
    print(running)


def force_close(even=None):
    start_btn.master.destroy()  # This destroys the entire window


text1 = tk.Text(root, height=20, width=41, bg="#A4B0BD")

# NOTE FOR FUTURE REFERENCE
# Using keyboard module instead of tkinter.bind makes the hotkeys work while the window is unfocused
keyboard.add_hotkey('f2', start_clicking_task)
keyboard.add_hotkey('f3', stop_clicking)
keyboard.add_hotkey('esc', force_close)
#keyboard.add_hotkey('f5', enable_start_btn)
#if min_var


dev_label.grid(row=0, column=0)
text1.grid(row=1, column=0, rowspan=10,padx=10)
range_label = tk.Label(root, text="Click Interval\n(seconds)", font=('calibre', 10, 'bold'), bg="#0A3D62", width=11, fg="#7ddeff")
min_label = tk.Label(root, text="Min", font=('calibre', 10, 'bold'), bg="#0A3D62", width=3, fg="#7ddeff")

max_label = tk.Label(root, text="Max", font=('calibre', 10, 'bold'), bg="#0A3D62", width=3, fg="#7ddeff")

start_btn = tk.Button(root, text='Start(F2)', bg="#2C3335", width=7, fg="#7ddeff", command=start_clicking_task)
stop_btn = tk.Button(root, text='Stop(F3)', bg="#2C3335", width=7, fg="#7ddeff", command=stop_clicking)
force_close_btn = tk.Button(root, text='Force close\n(Esc)', bg="#2C3335", width=8, fg="#7ddeff", command=force_close)
range_label.grid(row=1, column=2)
min_label.grid(row=2, column=1)
min_var_entry.grid(row=2, column=2)
max_label.grid(row=3, column=1)
max_var_entry.grid(row=3, column=2)
start_btn.grid(row=2, column=3, padx=3)
stop_btn.grid(row=3, column=3, padx=3)
force_close_btn.grid(row=8, column=2)

root.mainloop()
