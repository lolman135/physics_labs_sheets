from random import uniform
from openpyxl import *

def cell_name_forming(letter, index):
    return letter + str(index)

def element_generating(a, d):
    element = uniform(a-d, a+d)
    element = round(element, 2)
    return element

def clean_sheet(sheet):
    for row in sheet.iter_rows(min_row=2):
        for cell in row:
            cell.value = None

def choice(a, b, i):
    if i == 1: return a
    else: return b

def distribution(a, some):
    h = -0.1
    a = round(a, 4)
    for key in some:
        if a >= h and a < h + 0.01:
            some[key].append(a)
        h += 0.01      

def inscription(x):
    return str(round(x, 2)) + " <= ∆Ti < " + str(round(x+0.01, 2))
