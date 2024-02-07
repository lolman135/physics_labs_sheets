from functional import *
from alphabet import letters

amount_of_cells = int(input("Введіть кількість комірок: "))
period = float(input("Введіть період пʼяти коливань: "))
delta_period = period*0.0115
array_of_five_oscillation_periods = [element_generating(period, delta_period) for i in range(amount_of_cells)]
array_of_one_oscillation_periods = list(map(one_oscillation, array_of_five_oscillation_periods))
average_period = sum(array_of_one_oscillation_periods)/amount_of_cells

try:
    file = "test.xlsx"
    workbook = load_workbook(file)
    sheet = workbook["data"]

    clean_sheet(sheet)
    for i in range(len(array_of_five_oscillation_periods)):
        sheet[cell_name_forming(letters[0], i+2)] = i+1
        sheet[cell_name_forming(letters[1], i+2)] = array_of_five_oscillation_periods[i]
        sheet[cell_name_forming(letters[2], i+2)] = round(array_of_five_oscillation_periods[i]/5, 4)
        sheet[cell_name_forming(letters[3], i+2)] = round(array_of_one_oscillation_periods[i]-average_period, 5)
        sheet[cell_name_forming(letters[4], i+2)] = round((array_of_one_oscillation_periods[i]-average_period)**2, 7)
        
    workbook.save(file)
    workbook.close()

    print("Таблицю успішно створено")
    
except FileNotFoundError:
    print("Файл не знайдено")   
