from math import log, exp
from scipy.stats import linregress
import fileinput
import csv
import collections

x = []
y = []

def linreg(option):
    line = 1
    with open('price-elasticity.csv', 'rb') as csvfile:
        rows = csv.reader(csvfile)
        x = []
        y = []
        for row in rows:
            if not line == 1:
                if option == 'weekday' and int(row[0]) < 6:
                    x.append(log(float(row[2].replace('$', ''))))
                    y.append(log(float(row[1])))
                elif option == 'weekend' and int(row[0]) > 5:
                    x.append(log(float(row[2].replace('$', ''))))
                    y.append(log(float(row[1])))
            else:
                line = 0

        return linregress(x, y)

options = ['weekday', 'weekend']

for option in options:
    slope, intercept, r_value, p_value, std_err = linreg(option)

    print option + " report:"
    print slope, intercept, r_value, p_value, std_err

    ans = exp(slope * log(1) + intercept)
    print ans

    revenue = collections.defaultdict()

    max_revenue = 0
    max_price = 0
    max_room = 0
    for price in range(1, 2000):
        rooms = slope * log(price) + intercept
        rooms = exp(rooms)

        if rooms < 1100:
            if price * rooms > max_revenue:
                max_revenue = price * rooms
                max_price = price
                max_room = rooms
            revenue[price] = price * rooms

    #print revenue
    print "Maximum revenue: $" + str(max_revenue)
    print "Price for max revenue: $" + str(max_price)
    print "Rooms for max revenue: " + str(max_room)