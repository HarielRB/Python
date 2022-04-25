# importar biblioteca random e biblioteca string
import random
import string


# variável que define o tamanho de caracteres da senha
tamanho = int(input("Insira o tamanho da senha desejada: "))
# segue o padrão de boas práticas de SI

# variavel para receber a estrutura da senha a ser gerada
# o metodo ascii_letters envolve letras maiusculas e minusculas na senha
# o string.digits traz os digitos de 0 a 9
chars = string.ascii_letters + string.digits + '!@#$%&*()-=_+ç'

# criar variavel para armazenar
rnd = random.SystemRandom()  # os.urandom que gera numeros aleatorios a partir de fontes do SO

# printando uma senha que é gerada randomicamente entre os parametros selecionados em chars
# sempre vai ter numeros, letras e simbolos
print(''.join(rnd.choice(chars) for i in range(tamanho)))
