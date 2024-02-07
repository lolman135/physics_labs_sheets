from random import uniform
from openpyxl import *

def cell_name_forming(letter, index):
    return letter + str(index)

def element_generating(a, d):
    element = uniform(a-d, a+d)
    element = round(element, 4)
    return element

def clean_sheet(sheet):
    for row in sheet.iter_rows(min_row=2):
        for cell in row:
            cell.value = None

def one_oscillation(x):
    return x/5

