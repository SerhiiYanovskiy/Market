import copy
import os
import sys
import csv
from Product import Product



STORE = []


with open("prod.csv", "r") as file:
    for i in file.readlines():
        d = i.split(',')
        STORE.append(Product(d[0], d[1], float(d[2])))











