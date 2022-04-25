import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Socket criado com Sucesso!")
host = 'localhost'
porta = 5432

# o método bind é responsável por fazer a ligação entre cliente/servidor através do host e da porta
s.bind((host, porta))
mensagem = "\nServidor: Olá, Cliente! Suave, e você?"


while 1:
    # enquanto verdadeiro
    dados, endereco = s.recvfrom(4096)

    if dados:
        print('Servidor enviado Mensagem!')
        s.sendto(dados + (mensagem.encode()), endereco)
