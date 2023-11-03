'''Crie um programa que receba um numero e imprime o fatorial daquele numero
1º solicitar um numero ao usuário
"n! = n · (n-1) · (n-2) … 3 · 2 · 1"
ex. fatorial de 5 = 5*4*3*2*1 = resultado
após imprimir o resultado para o usuário
'''
while True:
    
    numero = int(input('Digite um numero para calcular o seu fatoria: '))
    fatorial = 1
    if numero < 0:
        print('O fatorial não pode ser caculado com numeros negativos.') 
    elif numero == 0:
        print('1') 
    else:
        for item in range(1, numero +1):
            fatorial = fatorial * item
        print(fatorial)

    reiniciar = input("Deseja reiniciar o programa? (s/n): ")
    if reiniciar.lower() != "s":
        break
'''def calcular_fatorial(numero):
    if numero < 0:
        return "O fatorial não está definido para números negativos"
    elif numero == 0:
        return 1
    else:
        fatorial = 1
        for i in range(1, numero + 1):
            fatorial *= i
        return fatorial

numero = int(input("Digite um número para calcular o fatorial: "))
resultado = calcular_fatorial(numero)
print(f"O fatorial de {numero} é {resultado}")'''


'''def calcular_fatorial(numero):
    if numero < 0:
        return "O fatorial não está definido para números negativos"
    elif numero == 0:
        return 1
    else:
        return numero * calcular_fatorial(numero - 1)

numero = int(input("Digite um número para calcular o fatorial: "))
resultado = calcular_fatorial(numero)
print(f"O fatorial de {numero} é {resultado}")'''

