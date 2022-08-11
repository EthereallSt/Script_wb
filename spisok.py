spisok_zaprosov = []
def create_spisok():
    with open('Выключенные ru.csv', newline='') as f:
                reader = f.readlines()
                for stringger in reader:
                    preset = stringger.split('|')[1]
                    zaprosik = stringger.split('|')[0]
                    spisok_zaprosov.append(zaprosik)
    return(spisok_zaprosov)
