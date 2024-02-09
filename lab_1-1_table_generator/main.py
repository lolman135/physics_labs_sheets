from variables import *
import os

try:
    file = "test.xlsx"
    workbook = load_workbook(file)
    sheet = workbook["data"]

    clean_sheet(sheet)

    for loop in range(1, 3):
        itera_cells_amount = amount_of_cells * loop
        for i in range(itera_cells_amount):
            sheet[cell_name_forming(letters[letter_index], i+2)] = i+1
            sheet[cell_name_forming(letters[letter_index+1], i+2)] = array_of_five_oscillation_periods[i]
            sheet[cell_name_forming(letters[letter_index+2], i+2)] = round(array_of_five_oscillation_periods[i]/5, 3)
            sheet[cell_name_forming(letters[letter_index+3], i+2)] = round(delta_array[i], 5)
            sheet[cell_name_forming(letters[letter_index+4], i+2)] = round(square_delta[i], 7)
        sheet[cell_name_forming(letters[letter_index+2], itera_cells_amount+2)] = sum(choice(sliced_one_oc_array, array_of_one_oscillation_periods, loop))
        sheet[cell_name_forming(letters[letter_index+2], itera_cells_amount+3)] = (sum(choice(sliced_one_oc_array, array_of_one_oscillation_periods, loop)))/itera_cells_amount
        sheet[cell_name_forming(letters[letter_index+4], itera_cells_amount+2)] = sum(choice(square_delta_sliced, square_delta, loop))
        sheet[cell_name_forming(letters[letter_index+4], itera_cells_amount+3)] = sum(square_delta)/itera_cells_amount

        for i in choice(delta_sliced_array, delta_array, loop):
            distribution(i, range_table)

        x = -0.1
        counter = 0
        for i in range(0, 10, 3):
            for j in range(5):
                sheet[cell_name_forming(letters[letter_index+j], choice(amount_of_cells, (amount_of_cells*2), loop)+5+i)] = inscription(x)
                sheet[cell_name_forming(letters[letter_index+j], choice(amount_of_cells, (amount_of_cells*2), loop)+6+i)] = list(range_table.keys())[counter]
                sheet[cell_name_forming(letters[letter_index+j], choice(amount_of_cells, (amount_of_cells*2), loop)+7+i)] = len(range_table[counter+1])
                x+=0.01; counter+=1

        
        sheet[cell_name_forming(letters[13], 2+loop)] = n_equals_inscription(itera_cells_amount)
        for i in range(20):
            sheet[cell_name_forming(letters[14+i], 2+loop)] = round(len(range_table[i+1])/itera_cells_amount,4)

        letter_index += 7

    sheet[cell_name_forming(letters[13], 2)] = "Інтервали відхилень\n за номерами No"
    for i in range(20):
        sheet[cell_name_forming(letters[14+i], 2)] = i

    workbook.save(file)
    workbook.close()

    print("Таблицю успішно створено")
    
    if os.name == "posix":
        os.system(f'open -a "Microsoft Excel" "{file}"')
    else:
        os.system(f'start excel "{file}"')
    

except FileNotFoundError:
    print("Файл не знайдено")   
