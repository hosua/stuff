import random, string
import tkinter as tk
import sys, os, time
from PIL import Image, ImageTk

SCREEN_WIDTH = 425
SCREEN_HEIGHT = 425
GRIDSIZE = 50
GRID_WIDTH = SCREEN_HEIGHT / GRIDSIZE
GRID_HEIGHT = SCREEN_WIDTH / GRIDSIZE
debug_mode = False  # Set this to false to display output to tkinter
#game_surface.fill(color="grey")
root = tk.Tk()
root.configure(bg='#0A3D62')    # Change BG color
root.title('Roulette')
unex = "1270x450"
ex = "1270x720"
root.geometry(unex)
root.update()



# Sizes taken at dimensions of 425x425 length*width
position_dict = {"0": (227, 369), "1": (319, 87), "2": (90, 304), "3": (279, 353), "4": (130, 343), "5": (215, 53), "6": (58, 208),
              "7": (354, 284), "8": (138, 75), "9": (372, 182), "10": (190, 62), "11": (98, 111), "12": (324, 323),  "13": (66, 155),
              "14": (349, 131), "15": (174, 366), "16": (270, 65), "17": (68, 257), "18": (371, 233), "19": (151, 357), "20": (334, 110),
              "21": (108, 327), "22": (372, 205), "23": (164, 66), "24": (240, 60), "25": (77, 284), "26": (252, 364), "27": (60, 181),
              "28": (339, 310), "29": (362, 258), "30": (117, 91), "31": (360, 156), "32": (201, 372), "33": (290, 77), "34": (56, 232),
              "35": (301, 344), "36": (81, 131)}

wheel_order = [0, 26, 3, 35, 12, 28, 7, 29, 18, 22, 9, 31, 14, 20, 1, 33, 16, 24, 5, 10, 23, 8, 30, 11, 36, 13, 27,
               6, 34, 17, 25, 2, 21, 4, 19, 15, 32]

class Roulette_Wheel():
    def __init__(self):
        self.wheel_path = Image.open(r"C:\Users\Josh\PycharmProjects\pythonProject\Roulette_wheel.png")
        self.wheel = ImageTk.PhotoImage(self.wheel_path)
        self.wheel_frame = tk.Frame(root, height=430, width=430)
        self.wheel_canvas = tk.Canvas(self.wheel_frame, width=425, height=425, bg="#006600")
        self.wheel_canvas.create_image(212.5, 215, image=self.wheel)

        self.wheel_frame.place(x=730, y=5)
        self.roulette_ball_path = Image.open(r"C:\Users\Josh\PycharmProjects\pythonProject\roulette_ball.png")
        self.roulette_ball = ImageTk.PhotoImage(self.roulette_ball_path)
        self.roll = self.wheel_canvas.create_text(200, 120, font="times 15 bold", text="")
    def draw_wheel(self):
        self.wheel_canvas.image = self.wheel
        self.wheel_canvas.place(x=1, y=1)

    def draw_roll(self, roll):
        try:
            self.wheel_canvas.delete(self.ball) # delete previous ball if it exists
        except:
            pass
        number_pos = position_dict.get(str(roll))
        self.ball = self.wheel_canvas.create_image(number_pos[0], number_pos[1], image=self.roulette_ball)
        self.roll = self.wheel_canvas.create_text(200, 120, font="times 15 bold", text="You rolled " + str(roll))

class Roulette:
    def __init(self, make_bet):
        self.result = roulette_wheel.wheel_canvas.create_text(300, 450, text="", font="times 15 bold")
        pass
    def format_money(self, m):
        return "${:,.2f}".format(m)

    def win(self, bet):
        string = "You won:" + self.format_money(bet)
        print(string + "\n")
        self.result = roulette_wheel.wheel_canvas.create_text(220, 280, font='times 15 bold', text=string)
        return self.result


    def lose(self, bet):
        string = "You lost:" + self.format_money(-bet)
        print(string + "\n")
        self.result = roulette_wheel.wheel_canvas.create_text(220, 280, font='times 15 bold', text=string)
        return self.result


    def make_bet(self, money):
        try:
            roulette_wheel.wheel_canvas.delete(self.result) # Remove previous text first
            roulette_wheel.wheel_canvas.delete(roulette_wheel.roll)
        except:
            pass

        try:
            #bet = float(input("How much do you want to bet?"))
            bet = float(bet_var.get())
            if bet > money:
                print("ERROR: You do not have enough money for that!")
                return 0
            if bet <= 0:
                print("ERROR: You must bet something!")
                return 0
        except ValueError:
            print("ERROR: Could not read a number from 'Bet'")
            return 0

        money -= bet

        try:
            bet_type = bet_type_var.get()
            if bet_type == "0" or int(bet_type) > 36:
                print("ERROR: Invalid range!")
                return 0
        except:
            pass

        bet_type.lower()
        roll = random.randint(0, 36)

        roulette_wheel.draw_wheel()
        roulette_wheel.draw_roll(roll)
        root.update()
        print("Rolled", roll)
        if bet_type == "even":
            if roll % 2 == 0 and roll != 0:   # If even and not = 0
                payout = bet
                self.win(payout)
            else:
                payout = -bet
                self.lose(payout)
        elif bet_type == "odd":
            if roll % 2 != 0:    # if odd
                payout = bet
                self.win(payout)
            else:
                payout = -bet
                self.lose(payout)

        elif bet_type.isdigit():
            if 0 >= int(bet_type) > 36:
                print("ERROR: Invalid number.")
                return 0
            if roll == int(bet_type):
                payout = bet * 36
                self.win(payout)
            else:
                payout = -bet
                self.lose(payout)
        # Inequalities
        elif bet_type[0] == "<":   # input should be something like < 5
            fixed_str = bet_type.replace(" ", "")   # get rid of any spaces
            number = int(fixed_str[1:].strip(string.punctuation).strip(string.ascii_letters))

            if 0 >= number > 36:
                print("Invalid number.")
                return 0

            bet_chance = number / 36
            pay_rate = 36/number - 1
            print("odds: ", bet_chance, "or (", number, " / ", "36)")

            if number >= roll != 0:   # if number chosen is less than the roll
                payout = bet * pay_rate
                self.win(payout)
            else:
                payout = -bet
                self.lose(payout)

        elif bet_type[0] == ">":
            fixed_str = bet_type.replace(" ", "")  # get rid of any spaces
            number = int(fixed_str[1:].strip(string.punctuation).strip(string.ascii_letters)) # strip any typos
            if 0 >= number > 36:
                print("ERROR: Invalid number.")
                return 0
            bet_chance = (36 - number) / 36   # 36 - number here because we're dealing with the complement
            pay_rate = 36 / (36 - number) - 1

            print("Odds:", bet_chance, " or (36 - ", number, ") / 36", sep="")
            if number <= roll != 0:  # if number chosen is less than the roll
                payout = bet * pay_rate
                self.win(payout)
            else:
                payout = -bet
                self.lose(payout)

        # List
        elif bet_type[0] == "[":
            new_str = bet_type.strip(string.punctuation).strip(string.ascii_letters).replace(" ", "")    # input correction
            #print(new_str)
            num_list = new_str.split(",")
            #print("numlist:", num_list)
            new_list = list(map(int, num_list))  # Map converts all the strings in the list into an int
            for num in new_list:
                if 0 >= int(num) > 36:
                    new_list.remove(num)
            #print("newlist:", new_list)  # No duplicates
            number = len(new_list)      # Number will refer to the input variable that we need to calculate the payout.
            #print("number", number)
            try:
                bet_chance = number / 36
                pay_rate = (36 / number) - 1
            except ZeroDivisionError:
                print("ERROR: Tried to divide by zero! Did you enter anything into the list?")
                return 0
            print("Payrate: (36/" + str(number) + ") - 1 = ", pay_rate, "odds:", bet_chance, "or", str(number) + "/" + "36")

            if roll in new_list:
                payout = bet * pay_rate
                self.win(payout)
            else:
                payout = -bet
                self.lose(payout)

        # Range
        elif bet_type[0] == "(":
            new_str = bet_type.strip(string.punctuation).strip(string.ascii_letters).replace(" ", "")  # input correction
            range_list = new_str.split("-")
            num_list = []
            if len(range_list) != 2:
                print("ERROR: Invalid input. It should look something like (1-4)")
                return 0
            else:
                for num in range(int(range_list[0]), int(range_list[1]) + 1):
                    if 0 < num <= 36:
                        num_list.append(int(num))
                if len(num_list) < 1:
                    print("Error: No valid values entered in the range!")
                    return 0
            number = len(num_list)  # Number will refer to the input variable that we need to calculate the payout.
            bet_chance = number / 36
            pay_rate = (36 / number) - 1

            print("Payrate: (36/" + str(number) + ") - 1 = ", pay_rate, "odds:", bet_chance, "or", str(number) + "/" + "36")
            if roll in num_list:
                payout = bet * pay_rate
                self.win(payout)
            else:
                payout = -bet
                self.lose(payout)
        else:
            print("ERROR: Your input was invalid!")
            return 0
        return payout



# Note to self: TextRedirector() may be useful in the future.
# Source: https://stackoverflow.com/questions/12351786/how-to-redirect-print-statements-to-tkinter-text-widget
# This redirects text from console to the the text_box widget
class TextRedirector(object):
    def __init__(self, widget, tag="stdout"):
        self.widget = widget
        self.tag = tag
    def write(self, str):
        self.widget.configure(state="normal")
        self.widget.insert("end", str, (self.tag,))
        self.widget.configure(state="disabled")

expanded = False

def show_tutorial():    # Hides and expands the tutorial when button is pressed
    global expanded
    if not expanded:
        root.geometry(ex)    # expanded
        expanded = True
    else:
        root.geometry(unex)    # default
        expanded = False


roulette_wheel = Roulette_Wheel()
game = Roulette()

bet_frame = tk.Frame(root, bg="#A4B0BD", height=120, width=200)
bet_frame.place(x=515, y=320)

roulette_wheel.draw_wheel()

dev_label = tk.Label(bet_frame, text='Made by Hoswoo', font=('times', 10, 'bold'), bg="#A4B0BD", fg="darkblue",
                     anchor="w")  # Hoswoo

text_box = tk.Text(root, bg="#A4B0BD", height=20, width=80, font=("times", 10, "bold"))
text_box.config(state="disabled")
if debug_mode == False:
    sys.stdout = TextRedirector(text_box)   # Redirect console output to text widget
    sys.stderr = TextRedirector(text_box)   # Redirect error messages to text widget in case user somehow breaks the game


money = 100000
money_var = tk.StringVar()
money_var.set("${:,.2f}".format(money))     # Formatting money to look nice


money_text_label = tk.Label(bet_frame, text="Money:", bg='#A1AAB5')
money_label = tk.Label(bet_frame, textvariable=money_var, bg='#A1AAB5')

bet_var = tk.StringVar()
bet_var.set("0")
bet_label = tk.Label(bet_frame, text="Bet:", bg='#A1AAB5')
bet_entry = tk.Entry(bet_frame, textvariable=bet_var, width=8)

bet_type_var = tk.StringVar()
bet_type_label = tk.Label(bet_frame, text="Bet Type:", bg='#A1AAB5')
bet_type_entry = tk.Entry(bet_frame, textvariable=bet_type_var, width=8)


tutorial_button = tk.Button(bet_frame, text="Tutorial", command=show_tutorial, bg="#2C3335", fg="#7ddeff")
tutorial_label = tk.Label(root, text="How to play:\n"
                                     "There consists of 37 total numbers (0-36)\n"
                                     "Rolling a 0 is an automatic loss.\n"
                                     "Rolling a 0 will also not count as an even number.\n"
                                     "0 is excluded when calculating probability.\n"
                                     "\nPayout:\n"
                                     "Your payout rate can be calculated with the formula (36/n) - 1\n"
                                     "Where n = the amount of numbers you are betting on.\n"
                                     "\nBet types:\n"
                                     "1) You can type even or odd to bet on all even or odd numbers.\n"
                                     "2) You can bet on a specific number by just typing that number in.\n"
                                     "3) You can bet on a list of numbers by typing [ at the start, and then all of the numbers you wish to bet on.\n"
                                     "For example, to bet on numbers 1, 2, and 13, I would type [1,2,13]\n"
                                     "4) You can bet on any range of numbers by typing ( at the start, and then your start and end numbers separated by a '-'\n"
                                     "For example, if I wanted to bet on all numbers from 2 to 13, I would type (2-13)", justify="left", bg='#A1AAB5')


def play():
    converted_money = money_var.get().replace("$", "").replace(",", "")  # Since we formatted money earlier we need to remove $ and commas from string
    payout = game.make_bet(float(converted_money))
    money_var.set("${:,.2f}".format(float(converted_money) + payout))    # Convert new value back to money format
    text_box.see("end")

def random_bet():
    money = float(money_var.get().replace(",", "").replace("$", ""))
    #max_bet = float(money_var.get().replace(",", "").replace("$", "")) / 2  # /2 will ensure that the max_bet is never over half of the money left
    max_bet = 5000
    if money < 5000:
        max_bet = money / 2
    bet_var.set(random.uniform(0, max_bet)) # random.uniform randomizes a range with floats
    bet_type_var.set("(" + str(random.randint(1, 18)) + "-" + str(random.randint(18, 36)) + ")")
    play()

money = float(money_var.get().replace(",", "").replace("$", ""))


random_bet_button = tk.Button(bet_frame, text="Random bet", command=random_bet, bg="#2C3335", fg="#7ddeff")
roll_button = tk.Button(bet_frame, text="Roll", command=play, width=10, bg="#2C3335", fg="#7ddeff")
dev_label.place(x=0, y=0)
text_box.place(x=150, y=5)  # Manually placing these is stupid but whatever
money_text_label.place(x=1, y=25)
money_label.place(x=45, y=25)
bet_label.place(x=1, y=50)
bet_entry.place(x=30, y=50)
bet_type_label.place(x=1, y=75)
bet_type_entry.place(x=60, y=75)
roll_button.place(x=118, y=25)
random_bet_button.place(x=118, y=55)
tutorial_button.place(x=118, y=90)
tutorial_label.place(x=150, y=450)

root.mainloop()


