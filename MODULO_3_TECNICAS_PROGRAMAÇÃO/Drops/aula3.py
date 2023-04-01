import numpy as np
import matplotlib.pyplot as plt

#array numeros sequenciais 12-37
print(np.arange(12,38,1))
#array distribuição poisson
n= 10000
poisson = np.random.poisson(5,n)
#plt.hist(poisson)
#plt.show()
#array distribuição normal
normal = np.random.normal(5,10,n)
#plt.hist(normal)
#plt.show()
#array distribuição exponencial
exponential = np.random.exponential(5,n)
#plt.hist(exponential)
#plt.show()
#crie uma matriz 10X8
#selecione apenas as colunas com indice par e linhas com indice impar
n_rows = 10
n_cols = 8
matriz_10x8 = np.random.randint(0,100,(n_rows, n_cols))
odd_index = [i for i in range(10) if i%2 != 0]
even_index = [i for i in range(8) if i%2 == 0]
print(matriz_10x8)
result = matriz_10x8[odd_index, : ][:,even_index]
print(result)