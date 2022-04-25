import os
# importação das bibliotecas
import time


# abrindo um arquivo e salvando em uma variável?
with open('host.txt') as file:
    # lendo o arquivo contido em file e salvando-o em uma varíavel
    dump = file.read()
    # dividindo o arquivo em linhas
    dump = dump.splitlines()
    for ip in dump:
        print('-' * 60)
        print(f'Verificando IP: {ip}')
        os.system(f'ping -n 2 {ip}')
        print('-' * 60)
        time.sleep(2)
