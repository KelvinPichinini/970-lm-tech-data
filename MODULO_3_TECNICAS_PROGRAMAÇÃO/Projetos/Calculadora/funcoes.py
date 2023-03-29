def soma(a:float,b:float) -> float:
    '''Takes the numbers a and b and returns the sum of them'''
    try:
        return a + b
    except TypeError:
        print(f"O input 'a' e 'b' devem ser números, recebido {a}: {type(a)}, {b}: {type(b)} ")
        return 'ERRO'

def subtracao(a:float,b:float) -> float:
    '''Takes the numbers a and b and returns the subtraction of them'''
    try:
        return a - b
    except TypeError:
        print(f"O input 'a' e 'b' devem ser números, recebido {a}: {type(a)}, {b}: {type(b)} ")
        return 'ERRO'
    
def divisao(a:float,b:float) -> float:
    '''Takes the numbers a and b and returns the division of them'''
    if b == 0:
        return 0
    else:
        try:
            return a/b
        except TypeError:
            print(f"O input 'a' e 'b' devem ser números, recebido {a}: {type(a)}, {b}: {type(b)} ")
            return 'ERRO' 
        
def multiplicacao(a:float,b:float) -> float:
    '''Takes the numbers a and b and returns the multiplication of them'''
    try:
        return a*b
    except TypeError:
        print(f"O input 'a' e 'b' devem ser números, recebido {a}: {type(a)}, {b}: {type(b)} ")
        return 'ERRO'