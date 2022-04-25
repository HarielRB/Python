# importar biblioteca Hashlib
import hashlib


arquivo1 = 'a.txt'
arquivo2 = 'b.txt'

# criar as variaveis para armazenar os hashs
# utiliza-se o  metodo new com o nome do tipo de hash a ser criado

hash1 = hashlib.new('ripemd160')

#
hash1.update(open(arquivo1, 'rb').read())

hash2 = hashlib.new('ripemd160')
hash2.update(open(arquivo2, 'rb').read())

if hash1.digest() != hash2.digest():
    # o metodo digest resume os dados passados para o metodo update
    print(f'O arquivo {arquivo1} é diferente do arquivo {arquivo2} ')

    # hexdigest resume o hash em hexadecimal
else:
    print(f' O aqruivo {arquivo1} é igual ao arquivo {arquivo2} ')

print(f'O hash do arquivo {arquivo1} é: {hash1.hexdigest()}')
print(f'O hash do arquivo {arquivo2} é: {hash2.hexdigest()}')