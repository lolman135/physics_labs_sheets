from functional import *

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 
           'H', 'I', 'J', 'K', 'L', 'M', 'N', 
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 
           'V', 'W', 'X', 'Y', 'Z', 'AA', 'AB',
           'AC', 'AD', 'AE', 'AF', 'AG', 'AH', "AI"]

letter_index = 0

amount_of_cells = 100

range_table = {
    1:[],
    2:[],
    3:[],
    4:[],
    5:[],
    6:[],
    7:[],
    8:[],
    9:[],
    10:[],
    11:[],
    12:[],
    13:[],
    14:[],
    15:[],
    16:[],
    17:[],
    18:[],
    19:[],
    20:[]
}

period = float(input("Введіть період пʼяти коливань: "))
deflection = period * uniform(0.02, 0.08)

array_of_five_oscillation_periods = [element_generating(period, deflection) for i in range(amount_of_cells)]
array_of_one_oscillation_periods = list(map(lambda x: x / 5, array_of_five_oscillation_periods))
sliced_one_oc_array = array_of_one_oscillation_periods[:50]

average_period = sum(array_of_one_oscillation_periods)/amount_of_cells
sliced_average_period = sum(sliced_one_oc_array)/(amount_of_cells/2)

delta_array =list(map(lambda x: x - average_period, array_of_one_oscillation_periods))
square_delta = list(map(lambda x: x ** 2, delta_array))

delta_sliced_array = list(map(lambda x: x - sliced_average_period, sliced_one_oc_array))
square_delta_sliced = list(map(lambda x: x ** 2, delta_sliced_array))

amount_of_cells = int(amount_of_cells/2)