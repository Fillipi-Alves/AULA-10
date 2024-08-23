# # AULA 10 -  Funções

# Variáveis
# Escopo
# Globais

# Locais

# ## 4.3. Funções

# Vimos nas ultimas aulas introdução à função.

# Vamos continuar explorando as possibilidades com Funções. 

# Toda função precisa ser criada e chamada, logo, sabemos que são ações no nosso código.

# Com a capacidade de deixar o desenvolvimento, muito mais interessante.

# ****

# **4.4. Variáveis**

# **Podemos declarar variáveis dentro de funções, e fora delas também.** 

# Atentar-se para a declaração é importante, pois variáveis locais só devem ser utilizadas dentro de funções.

# Chegamos então no escopo das variáveis: 

# **4.4.1.escopo** 

# Escopo de variáveis refere-se ao posicionamento de variáveis mediante as funções Ou seja sua localização.

# **Globais**

# Variáveis globais, podem ser utilizadas fora das funções, ou em qualquer lugar do código.

# **Locais**

# Locais são variáveis com o escopo mais restrito. podem ser utilizadas apenas dentro de uma função. 

# Vantagens:

# - Encapsulamento
# - Segurança
# - Evita conflitos

# ```python
# # LOCAIS 
# # Dentro da Funções 

# # def soma(): 
# #     n = 10
# #     x = 11
# #     soma  = n + x 
# #     print(soma)

# # soma()    

# # def subtracao():
# #     print(150-200)

# # subtracao()

# #Variáveis Globais

# numero  = 10
# numero2 = 15

# def soma():
#     somando = numero + numero2
#     print(somando)

# soma()    

# ```

# ```jsx

# #Função com Parâmetros 

# def saque(a, b):
#     print('Saldo:', a - b)

# def deposito(a,b):
#      print('Saldo:', a + b)

# def depositos(saldo):
#      print('Saldo:', saldo)     

# def banco(saldo):   

#     escolha=input('Digite sua operação: ')
#     b = float(input('>>'))
    
#     if escolha == '1':
#        saque(saldo,b)
#     elif escolha == '2':
#         deposito(saldo,b) 
#     elif escolha == '3':
#         saldo(saldo)          

# banco(2000)
# ```

# ## Exercícios com funções:

# 1 

# CRIE UMA FUNÇÃO PARA COMPARAR 2 NÚMEROS (par ou impar). UTILIZE VARIÁVEIS LOCAIS.

# 2

# CRIE UM AFUNÇÃO PARA MULTIPLICAR 3 NUMEROS.

# 3

# CRIE UMA FUNÇÃO PARA DESCOBRIR O VALOR ELEVADO DE UM NÚMERO.

# 4

# CRIE UMA FUNÇÃO PARA MOSTRAR UMA MENSAGEM PERSONALIZADA NA TELA, SE O USUÁRIO  DIGITAR, 18 ANOS

# 5

# DESENVOLVA UMA FUNÇÃO PARA DESCOBRIR A IDADE DE UMA PESSOA.

# 6

# DESENVOLVA UM AFUNÇÃO PARA VER SE O BRASIL GANHOU A COPA DE 1999

# 7 

# DESENVOLVA UM SISTEMA DE RESTAURANTE, ONDE O CLIENTE TEM OPÇÃO DE ESCOLHER ENTRE SALADA, MACARRONADA, SANDUICHE, SORVETE.  

# [Exercícios](https://www.notion.so/Exerc-cios-92d155c2cfa042a4961b74ae65336d03?pvs=21)

# Subir para  o Github** 

# ……………………………………………………………………………………………

# **CRIANDO MÓDULOS:**

# Com funções python:

# ```jsx
# Exemplo:
# ```

# ```jsx
# ATIVIDADES:

# CRIE UM MERCADO 
# ```

# Módulos intrinsecos

# O módulo **`statistics`** é uma biblioteca padrão do Python que fornece funções para realizar cálculos estatísticos básicos em conjuntos de dados. Ele inclui uma variedade de funções úteis para calcular medidas estatísticas comuns, como média, mediana, moda, desvio padrão e variância.

# Aqui estão algumas das funções mais comuns disponíveis no módulo **`statistics`**:

# 1. **mean()**: Esta função calcula a média aritmética de uma sequência de números. A média é calculada somando todos os números na sequência e dividindo pela quantidade total de números.
# 2. **median()**: A função **`median()`** calcula a mediana de uma sequência de números. A mediana é o valor que está no meio de uma lista ordenada de números. Se houver um número par de elementos, a mediana é a média dos dois valores do meio.
# 3. **mode()**: A função **`mode()`** calcula a moda de uma sequência de números. A moda é o valor que aparece com mais frequência na sequência.
# 4. **stdev()**: Esta função calcula o desvio padrão de uma sequência de números. O desvio padrão é uma medida de dispersão que indica o quanto os números estão dispersos em relação à média.

# https://docs.python.org/pt-br/3/library/statistics.html

# ```python
# Função do módulo statistics

# 1. mean() - Calcula a média aritmética de uma lista de números.

# import statistics

# lista = [1, 2, 3, 4, 5]
# media = statistics.mean(lista)
# print("Média:", media)

# 2. median() - Calcula a mediana de uma 
# lista de números.

# import statistics

# lista = [1, 2, 3, 4, 5]
# mediana = statistics.median(lista)
# print("Mediana:", mediana)

# 3. mode() - Calcula a moda (o valor mais comum) 
# de uma lista de números.

# import statistics

# lista = [1, 2, 2, 3, 3, 3, 4, 4, 5]
# moda = statistics.mode(lista)
# print("Moda:", moda)

# 4. stdev() - Calcula o desvio padrão de uma 
# lista de números.

# import statistics

# lista = [1, 2, 3, 4, 5]
# desvio_padrao = statistics.stdev(lista)
# print("Desvio Padrão:", desvio_padrao)

# 5. variance() - Calcula a variância de uma 
# lista de números.

# '''Dado um conjunto de dados, a variância é 
# uma medida de dispersão que mostra o quão 
# distante cada valor desse conjunto está do 
# valor central (médio).'''

# import statistics

# lista = [1, 2, 3, 4, 5]
# variancia = statistics.variance(lista)
# print("Variância:", variancia)

# ```

# ```jsx
# import statistics

# def calcular_media(lista):
#     # Verifica se a lista está vazia
#     if not lista:
#         return "A lista está vazia, não é possível calcular a média."
    
#     # Calcula a média utilizando a função mean da biblioteca statistics
#     media = statistics.mean(lista)
#     return f"A média dos números na lista é: {media}"

# # Exemplo de uso
# numeros = [10, 20, 30, 40, 50]
# print(calcular_media(numeros))
# ```

# ## 

# ## Desafio 1

# VOCÊ É UM DEV E PRECISA CRIAR UM SISTEMA PARA UMA ESCOLA. 

# SISTEMA DE NOTAS DE ALUNOS QUE MOSTRE COM ESTATISTICA A MODA E A MEDIA, VARIANÇA E DESVIO DE PADRÃO, DAS NOTAS DE ALUNOS DE UM COLÉGIO, ALÉM DE MOSTRAR MENOR E A  MAIOR NOTA, SEPARE EM FUNÇÕES DIFERENTES 

# 1 -  ***VOCÊ CRIAR SEUS PRÓPRIOS MÓDULOS***

# 2 - ***OU USAR STATISTICS *****

# ## Desafio 2

# Você é um analista de dados, e decidiu trocar de emprego.

# Utilize a media, moda, mediana e o desvio padrão para decidir qual empresa faz sentido para você:

# Justificar por que decidiu por essa empresa.

# ***Verifique isso através dos salários:***

# empresa1 = [1000,6000,1200,8000,1400]

# empresa2 = [5000,4000,3000,2000,7000]

# empresa3 = [1200,1300,8000,3000,15000]

# empresa4 = [1400,1750,2000,4500,5900,7000]

# [Resolução (1)](https://www.notion.so/Resolu-o-1-8cb0d54134124f0c97fc5ac607605175?pvs=21)

# # #Adicionar comentários:  justifique sua escolha;

# # #Sua escolha, com o você fez isso e por que escolheu a empresa?