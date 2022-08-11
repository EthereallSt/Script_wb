import csv, spisok
import json, requests


def request_v2(item: str) -> dict:      
    '''Примет строку с человеческим запросом. Вернет отчет по записи из ручки v2.'''
    link = 'http://exactmatch-common.wbxsearch-internal.svc.k8s.wbxsearch-dp/v2/search?'
    query = {"query": item.replace(')', '').replace('(', '')}

    with requests.session() as session:
        session.headers['User-Agent'] = 'insomnia/2022.2.1'
        response = session.get(link, params=query)
        result = json.loads(response.text)
        
    return(result["query"])


counti = 0      #cчётчик
'''функция которая собирает в список все чел. запросы из файла выключенных записей'''
spisok.create_spisok() 


input = open('search.csv', 'rt')        #идём построчно в указанном файле
output = open('search_new.csv', 'w')    #записываем в новый файл без проблемных строк (удаление)

writer = csv.writer(output, delimiter='|')
for row in csv.reader(input, delimiter='|'):
    if row[2] == "no" and (row[0] in spisok.spisok_zaprosov) and ("t0" or "t1") not in request_v2(row[0]):
        counti+=1
        print(f"на данный момент обнаружено {counti} записей на удаление")
    else:
        writer.writerow(row)



input.close()
output.close()
print(f"столько записей: {counti} нужно удалить")








