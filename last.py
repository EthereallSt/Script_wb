presets =[]     #список пресетов
itog =[]        #список куда запишем все строки соответствующие условиям
zapross =[]     #список человеческих запросов
querys = []     #список квери

with open("trol.txt", newline='') as f:
    for line in f:
        preset = line.split("|")[1]
        zapros = line.split("|")[0]
        query = line.split("|")[6]
        if preset not in presets:
            presets.append(preset)
            zapross.append(zapros)
            querys.append(query)
        else:
            if zapros not in zapross:
                if query not in querys:
                    itog.append(line)



def write_file(znachen):        # Собирает файл из списка.
    f = open( 'querys.txt', 'w' )
    f.write("".join(znachen))
    f.close
    
write_file(itog)
