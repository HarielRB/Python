# importar a biblioteca Socket
# importar biblioteca sys

import socket
import sys


def main():
    # tentar uma conexão TCP/IP
    try:
        # utilizar o método socket com os parametros para referenciar o tipo de protocolo utilizado
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as erro:
        print("A conexão falhou!")
        print(f'Erro: {erro}')
        # função que encerra o programa da biblioteca sys
        sys.exit()
    print('Socket criado com sucesso!')

    # definir qual o host a ser conectado
    host_alvo = input("Digite o Host ou IP a ser conectado: ")
    porta_alvo = input('Digite a porta a ser conectada: ')

    try:
        # a porta sempre tem que ser int
        s.connect((host_alvo, int(porta_alvo)))
        print('Cliente TCP conectado com sucesso!')
        print(f'Host: {host_alvo} \nPorta: {porta_alvo}')
        # encerrar conexão para não ficar em loop com método shutdown
        s.shutdown(2)
    except socket.error as erro:
        print("A conexão Falhou!")
        print(f'Erro: {erro}')
        sys.exit()


if __name__ == "__main__":
    main()
