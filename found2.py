
pok = []
with open("итоги_полный_файл.txt", "r", newline='') as f:
    reader = f.readlines()
    for stringg in reader:
        if stringg.split('|')[0] in unice:




