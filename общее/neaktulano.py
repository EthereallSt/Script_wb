# Этот вариант скрипта очень долго выполняется из-за неоптимального написания, отказался от него.

import csv

presets= [0]          # список всех пресетов 
zap = []              # список cтрок с повторяющимися пресетами


def found_preset():     # Эта функция проходит по файлу csv построчно и пополняет список(presets)
    with open('result_copy.csv', newline='') as f:
        reader = csv.reader(f, delimiter='|')
        for stringg in reader:
            if len(stringg[1]):
                presets.append(int(stringg[1]))

def found_repeat_presets(presets):  #фун. для поиска и подсчёта всех повторяющихся пресетов из списка
    counter = {}
    for elem in presets:
        counter[elem] = counter.get(elem, 0) + 1

    pepa=[element for element, count in counter.items() if count > 1]
    return(pepa)

found_preset()
repeat = found_repeat_presets(presets)


def found_repeat_zapis(repeat):  #фун. для поиска и всех повторяющихся записей из списка
    stroks = []
    with open('result_copy.csv', newline='') as f:
        reader = csv.reader(f, delimiter='|')
        for stringg in reader:
            for i in repeat:
                if len(stringg[1]) and str(i) in stringg:
                        stroks.append(stringg)
                               
    return stroks

stroks = found_repeat_zapis(repeat)

def found_repeat_zapis_with_if(stroks):
    strokss = []  #фун. для поиска и всех повторяющихся записей из списка
    with open('result_copy.csv', newline='') as f:
        reader = csv.reader(f, delimiter='|')
        for stringg in reader:
            for i in stroks:
                if len(stringg[1]) and str(i[1]) in stringg and i[2] not in stringg:
                        strokss.append(stringg)

strokss = found_repeat_zapis_with_if(stroks)
print(strokss)
#print(stroks)