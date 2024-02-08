from functional import *
from alphabet import letters

amount_of_cells = int(input("Введіть кількість комірок: "))
period = float(input("Введіть період пʼяти коливань: "))
deflection = period*0.0115
array_of_five_oscillation_periods = [element_generating(period, deflection) for i in range(amount_of_cells)]
array_of_one_oscillation_periods = list(map(lambda x: x / 5, array_of_five_oscillation_periods))
average_period = sum(array_of_one_oscillation_periods)/amount_of_cells
delta_array =list(map(lambda x: x - average_period, array_of_one_oscillation_periods))
square_delta = list(map(lambda x: x ** 2, delta_array))

try:
    file = "test.xlsx"
    workbook = load_workbook(file)
    sheet = workbook["data"]

    clean_sheet(sheet)
    for i in range(amount_of_cells):
        sheet[cell_name_forming(letters[0], i+2)] = i+1
        sheet[cell_name_forming(letters[1], i+2)] = array_of_five_oscillation_periods[i]
        sheet[cell_name_forming(letters[2], i+2)] = round(array_of_five_oscillation_periods[i]/5, 4)
        sheet[cell_name_forming(letters[3], i+2)] = round(delta_array[i], 5)
        sheet[cell_name_forming(letters[4], i+2)] = round(square_delta[i], 7)
    sheet[cell_name_forming(letters[2], amount_of_cells+2)] = sum(array_of_one_oscillation_periods)
    sheet[cell_name_forming(letters[2], amount_of_cells+3)] = (sum(array_of_one_oscillation_periods))/amount_of_cells
    sheet[cell_name_forming(letters[4], amount_of_cells+2)] = sum(square_delta)
    sheet[cell_name_forming(letters[4], amount_of_cells+2)] = sum(square_delta)/amount_of_cells

    workbook.save(file)
    workbook.close()

    print("Таблицю успішно створено")
    
except FileNotFoundError:
    print("Файл не знайдено")   
