import requests
import json
import spisok

new_spisok =[]


def request_v2(item: str) -> dict:
    '''Примет строку с человеческим запросом. Вернет отчет по записи из ручки v2.'''
    link = 'http://exactmatch-common.wbxsearch-internal.svc.k8s.wbxsearch-dp/v2/search?'
    query = {"query": item.replace(')', '').replace('(', '')}

    with requests.session() as session:
        session.headers['User-Agent'] = 'insomnia/2022.2.1'
        response = session.get(link, params=query)
        result = json.loads(response.text)
        
    return(result["query"])


def found_presets():
    counti = 0
    with open('search.csv', newline='') as f:
            reader = f.readlines()
            for stringg in reader:
                polozhenie = stringg.split('|')[2]
                zapros = stringg.split('|')[0]
                if polozhenie == "no":   
                    if (zapros in spisok.spisok_zaprosov):
                        print(zapros)
                        counti += 1
            print(counti)


            
found_presets()  
'''
 and ("t0" or "t1") not in request_v2(zapros):
 '''