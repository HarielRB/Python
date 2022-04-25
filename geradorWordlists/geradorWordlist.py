import itertools


string = input("String a ser permutada: ")

# variavel para armazenar o metodo permutation que realiza a permutacao das palavras e caracteres no wordlist
resultado = itertools.permutations(string, len(string))
count = 0
for i in resultado:
    # printa o caractere em forma de string com o join
    print(''.join(i))
    count += 1

print(f'Foram gerados {count} resultados!')
