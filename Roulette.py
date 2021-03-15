import random, string   # Made by Hoswoo
import keyboard as kb
import time
class Roulette:

    def format_money(self, m):
        return "${:,.2f}".format(m)

    def __init(self, make_bet):
        print("init")

    def win(self, bet):
        print("You won:", self.format_money(bet))
        print("Money left:", self.format_money(money))

    def lose(self, bet):
        print("You lost:", self.format_money(bet))
        print("Money left:", self.format_money(money))


    def make_bet(self, money):

        try:
            bet = float(input("How much do you want to bet?"))
            if bet > money:
                print("ERROR: You do not have enough money for that!")
                return 0
            if bet <= 0:
                print("ERROR: You must bet something!")
                return 0
        except ValueError:
            print("ERROR: That is not a number!")
            return 0

        money -= bet
        print("Money left:", self.format_money(money))

        try:
            bet_type = input("1. Even, odd, or specific #(1-36)"
                             "\n\n2. Inequalities like: < 5 (this is inclusive)"
                             "\n\n3. A list of numbers starting with [ and separated with commas like: [1,2,3]"
                             "\n[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]"
                             "\n\n4. A range of numbers starting with ( separated with hyphens like: (1-12), (13-24), (25-36), etc."
                             "\n\nRolling 0 is an automatic loss")
            if bet_type == "0" or int(bet_type) > 36:
                print("ERROR: Invalid range!")
                return 0
        except:
            pass

        bet_type.lower()
        roll = random.randint(0, 36)
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
            inequality = fixed_str[0]
            number = int(fixed_str[1:].strip(string.punctuation).strip(string.ascii_letters))

            if 0 >= number > 36:
                print("Invalid number.")
                return 0

            bet_chance = number / 36
            pay_rate = 36/number - 1
            print("odds:", bet_chance, "or", number, "/", "36")
            print("num:", number, "roll:", roll)

            if number >= roll != 0:   # if number chosen is less than the roll
                payout = bet * pay_rate
                self.win(payout)
            else:
                payout = -bet
                self.lose(payout)

        elif bet_type[0] == ">":
            fixed_str = bet_type.replace(" ", "")  # get rid of any spaces
            inequality = fixed_str[0]
            number = int(fixed_str[1:].strip(string.punctuation).strip(string.ascii_letters)) # strip any typos
            if 0 >= number > 36:
                print("ERROR: Invalid number.")
                return 0
            bet_chance = (36 - number) / 36   # 36 - number here because we're dealing with the complement
            pay_rate = 36 / (36 - number) - 1

            print("odds:", bet_chance, "or (36 -", number, ")/", "36", sep="")
            print("num:", number, "roll:", roll)
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
            print("payrate: (36 / ", number, ") - 1 = ", pay_rate, sep="")
            print("odds:", bet_chance, "or", number, "/", "36")
            print("num:", number, "roll:", roll)
            if roll in new_list:
                payout = bet * pay_rate
                self.win(payout)
            else:
                payout = -bet
                self.lose(payout)

        # Range
        elif bet_type[0] == "(":
            new_str = bet_type.strip(string.punctuation).strip(string.ascii_letters).replace(" ", "")  # input correction
            print(new_str)
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
                print(num_list)
            number = len(num_list)  # Number will refer to the input variable that we need to calculate the payout.
            # print("number", number)

            bet_chance = number / 36
            pay_rate = (36 / number) - 1

            print("payrate: (36 / ", number, ") - 1 = ", pay_rate)
            print("odds:", bet_chance, "or", number, "/", "36")
            print("num:", number, "roll:", roll)
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

def betting_bot(bet, bet_type, delay, money_left):
    time.sleep(.2)
    if bet > money_left:
        new_bet = str(money_left)
    else:
        new_bet = str(bet)
    kb.write(new_bet)
    kb.press('enter')
    time.sleep(delay)
    kb.write(bet_type)
    kb.press('enter')
    time.sleep(delay)
    if kb.is_pressed("esc"):
        quit()


money = 1000000
game = Roulette()   # Don't forget to instantiate first
while True:
    #betting_bot(random.randint(50, 200000), "(" + str(random.randint(1, 18)) + "-" + str(random.randint(18, 36)) + ")", .2, money)
    if money <= 0:
        print("You are out of money! Exiting...")
        quit()
    else:
        print("Money left:", "${:,.2f}".format(money))
        money += game.make_bet(money)
        print("")