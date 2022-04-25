# importar o metodo  thread
from threading import Thread
import time


# possibilita o multithreading


def carro(velocidade, piloto):
    trajeto = 0
    fim = 100
    while trajeto <= fim:
        trajeto += velocidade
        time.sleep(0.5)
        print(f'Carro {piloto}: {trajeto}KM\n')


t_carro1 = Thread(target=carro, args=[1, 'Hariel'])
t_carro2 = Thread(target=carro, args=[1.5, 'Harianne'])

t_carro1.start()
t_carro2.start()
