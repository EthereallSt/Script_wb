# Cкрипт для объединения всех  csv-файлов в директории.

import fileinput
import glob

file_list = glob.glob("*.csv")

with open('общий.csv', 'w') as f:
    input_lines = fileinput.input(file_list)
    f.writelines(input_lines)

        