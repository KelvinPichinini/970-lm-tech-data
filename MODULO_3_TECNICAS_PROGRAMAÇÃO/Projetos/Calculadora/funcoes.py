def soma(a,b):
    try:
        return a + b
    except TypeError:
        print('a e b devem ser numeros')
        return 'ERRO'
