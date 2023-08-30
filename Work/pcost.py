# pcost.py
#
# Exercise 1.27

import csv
import sys


def portfolio_cost(filename):
    cost = 0.0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            try:
                price = float(row[2])
                shares = int(row[1])
            except ValueError:
                print("Couldn't parse entry. Continuing.")
            cost += price * shares
    return cost


if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'Data/missing.csv'
    total_cost = portfolio_cost(filename)
    print(total_cost)
