import random, math
import numpy as np
import os.path
import pickle
np.set_printoptions(precision=20)
# WARNING: This program will write data to a file and save it.
# If you use extremely high numbers, you will create huge files.

# Note that these results will differ from online calculators if using smaller sample sizes.
def flip_coin(n):
    roll_list = [0, 0]
    for i in range(n):
        roll = random.random()
        if roll < 0.5:
            roll_list[0] += 1
    roll_list[1] = n - roll_list[0]
    rate_heads = round(roll_list[0] / n, 2)
    str_rate_heads = "{:.3f}".format(rate_heads)
    rate_tails = 1 - rate_heads
    str_rate_tails = "{:.3f}".format(rate_tails)
    print("[H,T] =", roll_list, "   %[H]:" + str_rate_heads + "   %[T]:" + str_rate_tails)
    # Saving these Trials to a .dat file

    with open('Coin_flip_data.dat', 'a') as f:  # Instead of 'w', use 'a' to append here
        f.write(str(roll_list) + "          " + str_rate_heads + "        " + str_rate_tails)
        f.write("\n")
    return rate_heads   # Later if we need rate tails, just calculate it again with 1 - rate_heads


def multi_flipper(lst, num_of_trials, num_of_flips):   # Takes in 2D List
    for i in range(num_of_trials):
        print("Trial", i + 1)
        x = flip_coin(num_of_flips)    #  x = rate of heads
        lst[0].append(x)
        lst[1].append(round(1 - x, 2))   # AKA, 1 - rate_heads
    print(lst)


# Should have made multi-flipper and flip_coin as one function. Oh well


def statistics_calculator(lst):
    # Variable Finder
    sum_of_x = 0
    sum_of_squared = 0
    n = len(lst)
    for var in lst:
        sum_of_x += var
        sum_of_squared += math.pow(var, 2)
    variance = (sum_of_squared - (math.pow(sum_of_x, 2)/n))/(n-1)
    heads_deviation = math.sqrt(variance)
    print("Variance:", "{:.4f}".format(variance), "  Standard Deviation:", "{:.4f}".format(heads_deviation))
    q1 = np.percentile(lst, 25, interpolation='midpoint')
    q3 = np.percentile(lst, 75, interpolation='midpoint')
    IQR = q3 - q1
    print("Q1:", q1, "Q3:", q3, "IQR:", round(IQR, 3))
    lower_bound = q1 - 1.5 * IQR
    upper_bound = q3 + 1.5 * IQR
    lower_extreme_bound = q1 - 3 * IQR
    upper_extreme_bound = q3 + 3 * IQR
    print("Lower extreme bounds:", lower_extreme_bound, "   Lower bounds:", lower_bound, "  Upper bounds:", upper_bound,
          " Upper extreme bounds:", upper_extreme_bound)
    # Outlier Check
    outlier_list = [[], [], [], []]  # [[Extreme_lower], [Lower], [Upper], [Extreme_upper]]
    outlier_index_list = [[], [], [], []]  # [[Extreme_lower], [Lower],[Upper], [Extreme_upper]]
    extreme_lower_count = 0     # Extremes are not properly implemented yet
    lower_count = 0
    upper_count = 0
    extreme_upper_count = 0
    for i in range(len(lst)):
        if lower_extreme_bound < lst[i] < lower_bound:  # lower bounds
            outlier_list[1].append(lst[i])
            lower_count += 1
            outlier_index_list[1].append(i+1)
        if lst[i] < lower_extreme_bound:
            outlier_list[0].append(lst[i])
            extreme_lower_count += 1
            outlier_index_list[0].append(i+1)
        if upper_extreme_bound > lst[i] > upper_bound:  # upper bounds
            outlier_list[2].append(lst[i])
            upper_count += 1
            outlier_index_list[2].append(i+1)
        if lst[i] > upper_extreme_bound:
            outlier_list[3].append(lst[i])
            extreme_upper_count += 1
            outlier_index_list[3].append(i+1)
    print("# of lower outliers:", lower_count, "\n# of upper outliers:", upper_count)
    print("# of extreme lower outliers:", extreme_lower_count, "\n# of extreme upper outliers:", extreme_upper_count)
    print("Percentage of outliers in data set:", str(round(((lower_count + upper_count) / n) * 100, 5)) + "%")
    print("Percentage of extreme outliers in data set:", str(round(((extreme_lower_count + extreme_upper_count) / n) * 100, 5)) + "%")

    with open('calculation_data.dat', 'w') as f:
        f.write("Extreme Lower Outliers: " + str(outlier_list[0]))
        f.write("\nExtreme Lower Trial #(s): " + str(outlier_index_list[0]))
        f.write("\nLower Outliers: " + str(outlier_list[1]))
        f.write("\nLower Trial #(s): " + str(outlier_index_list[1]))
        f.write("\nUpper Outliers: " + str(outlier_list[2]))
        f.write("\nUpper Trial #(s): " + str(outlier_index_list[2]))
        f.write("\nExtreme Upper Outliers: " + str(outlier_list[3]))
        f.write("\nExtreme Upper Trial #(s): " + str(outlier_index_list[3]))
        f.write("\n# of lower outliers: " + str(lower_count) + "\n# of upper outliers:" + str(upper_count))
        f.write("\n# of extreme lower outliers: " + str(extreme_lower_count) +"\n# of extreme upper outliers:" + str(extreme_upper_count))
        f.write("\nPercentage of outliers in data set: " + str(round(((lower_count + upper_count) / n) * 100, 5)) + "%")
        f.write("\nPercentage of extreme outliers in data set: " + str(round(((extreme_lower_count + extreme_upper_count) / n) * 100, 5)) + "%")
        f.write("\nVariance: " + "{:.4f}".format(variance) + "  Standard Deviation: " + "{:.4f}".format(heads_deviation) + "\n"
            + "Q1: " + "{:.4f}".format(q1) + "  Q3: " + "{:.4f}".format(q3) + "  IQR: " + "{:.4f}".format(IQR) + "\n" +
            "Lower extreme bounds:" + "{:.4f}".format(lower_extreme_bound) + "  Lower bounds:" + "{:.4f}".format(
            lower_bound) + "  Upper bounds:" + "{:.4f}".format(upper_bound) + "  Upper extreme bounds:" + "{:.4f}".format(
            upper_extreme_bound))
    return outlier_list

# Make Directory
cwd = os.getcwd()
dir = os.path.join(os.path.join(cwd, 'coin_flipper'))
if not os.path.exists(dir):   # If it does not exist already
    os.makedirs('coin_flipper')
os.chdir(dir)  # Change to the directory
f = open('Coin_flip_data.dat', 'w')    # Clear coin flip data first with 'w'
f.write("[H , T ]           %[H]         %[T]\n")  # Write first line
f.close()

rate_of_flips_list = [[],[]] # [Heads], [Tails]
trials = int(input("Enter # of trials:"))
flips = int(input("Enter # of flips:"))
multi_flipper(rate_of_flips_list, trials, flips)

print("\nStatistics for Heads")
statistics_calculator(rate_of_flips_list[0])

# Why the hell did I make this lol