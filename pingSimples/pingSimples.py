import os # importando a biblioteca 

print('#' * 60)
print('Verificador de Ping e Host')
print('#' * 60)
# criar variavel para receber o IP ou Host a ser pingado
ip_ou_host = input("Digite o IP ou Host a ser verificado: ")

# chamar o ping do SO pela biblioteca OS com comandos de sistemas

os.system(f'ping -n 6 {ip_ou_host}')
# a biblioteca chamou o método system que executa comandos do cmd do windows
