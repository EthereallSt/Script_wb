presets =[]     #список пресетов
itog =[]        #список куда запишем все строки соответствующие условиям
buckets =[]     #список человеческих запросов
querys = []     #список квери

with open("trol.txt", newline='') as f:
    for line in f:
        preset = line.split("|")[1]
        bucket = line.split("|")[7]
        query = line.split("|")[6]
        
        if query not in querys and bucket not in buckets:
            querys.append(query)
            buckets.append(bucket)
            
        else:
            if bucket in buckets and query not in querys:
                querys.append(query)
                itog.append(line)

        #else:
        #    if zapros not in zapross:
        #        if query not in querys:
        #            itog.append(line)



def write_file(itog):        # Собирает файл из списка.
    f = open( 'itog.txt', 'w' )
    f.write("".join(itog))
    f.close
    
write_file(itog)
