presets =[]     #список пресетов
itog =[]        #список куда запишем все строки соответствующие условиям
buckets =[]     #список человеческих запросов
querys = []
zapros = []     #список квери
popa  =[]     #список строк которые я не могу сразу проверить 



with open("trol.txt", newline='') as f:
    for line in f:
        preset = line.split("|")[1]
        bucket = line.split("|")[7]
        query = line.split("|")[6]
        zapro = line.split("|")[0]
        
        if preset not in presets and bucket not in buckets:
            buckets.append(bucket)
            presets.append(preset)
        
        else:
            popa.append(line)

            

with open("все_записи_с_повторным_пресетом.txt", newline='') as f:
    for line in f:
        preset = line.split("|")[1]
        bucket = line.split("|")[7]
        query = line.split("|")[6]
        zapro = line.split("|")[0]

        if line in popa:
            if query in querys or zapro in zapros:
                    continue
            elif query not in querys and zapro not in zapros:
                querys.append(query)
                zapros.append(zapro)
                itog.append(line)

        #else:
        #    if zapros not in zapross:
        #        if query not in querys:
        #            itog.append(line)


def write_file(itog):        # Собирает файл из списка.
    f = open( 'финальный.txt', 'w' )
    f.write("".join(itog))
    f.close
    
write_file(itog)
