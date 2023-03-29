def soma(a,b):
    try:
        return a + b
    except TypeError:
        print(f"O input 'a' e 'b' devem ser números, recebido {a}: {type(a)}, {b}: {type(b)} ")
        return 'ERRO'
