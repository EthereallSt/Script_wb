import csv

presets= [0]
presets_repeat= []    # в этот список я добавлю все пресеты которые соберу с файла.

def found_preset():     # Эта функция проходит по файлу csv построчно и добавляет в список пресеты
    with open('result_copy.csv', newline='') as f:
        reader = csv.reader(f, delimiter='|')
        for stringg in reader:
            if len(stringg[1]):
                presets.append(int(stringg[1]))


def found_repeat_presets(presets):
    counter = {}

    for elem in presets:
        counter[elem] = counter.get(elem, 0) + 1

    doubles = {element: count for element, count in counter.items() if count > 1}
    return(doubles)


def get_repeat_numbers(presets):
    repeat = []
    unice = []

    for number in presets:
        if number in unice:
            repeat.append(number)
        else:
            unice.append(number)
    return repeat

found_preset()
print(found_repeat_presets(presets))
print(get_repeat_numbers(presets))