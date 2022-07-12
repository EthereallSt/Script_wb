import fileinput
import glob

file_list = glob.glob("*.csv")

with open('result.csv', 'w') as f:
    input_lines = fileinput.input(file_list)
    f.writelines(input_lines)

# это мне поможет объединить все csv файлы.
        