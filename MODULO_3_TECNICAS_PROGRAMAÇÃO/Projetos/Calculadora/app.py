from funcoes import *

operations = {
    "soma":soma,
    "subtracao":subtracao,
    "multiplicacao":multiplicacao,
    "divisao":divisao,
    '+':soma,
    '-':subtracao,
    '/':divisao,
    '*':multiplicacao
}

def calcule():
    a = input("Digite o primeiro número: ")
    operation = input('Qual operação? ')
    b = input("Digite o segundo numero: ")
    try:
        a = float(a)
        b = float(b)
    except:
        print("Números inválidos")
        return None
    try:
        return operations[operation](a,b)
    except:
        print("Operação inválida")
        return None

print(calcule())