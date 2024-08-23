# Exercícios com funções:


# # 1 CRIE UMA FUNÇÃO PARA COMPARAR 2 NÚMEROS (par ou impar). UTILIZE VARIÁVEIS LOCAIS

numero = int(input("Digite um número: "))


if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")





# # Exercicio 2 
# #CRIE UM AFUNÇÃO PARA MULTIPLICAR 3 NUMEROS.

numero1 = 4
numero2 = 76
numero3 = 9   
print('O resultado da multiplicação é', numero1 * numero2 * numero3)



# # Exercicio 3 
# #CRIE UMA FUNÇÃO PARA DESCOBRIR O VALOR ELEVADO DE UM NÚMERO.

def elevado():
     print(n**2)

n = int(input('Digite um numero: '))
elevado()   



# Exercicio 4 
#CRIE UMA FUNÇÃO PARA MOSTRAR UMA MENSAGEM PERSONALIZADA NA TELA, SE O USUÁRIO  DIGITAR, 18 ANOS


idade = int(input("Digite a sua idade: "))

if idade >= 18:
    print("Você pode entrar nesta festa.")
else:
    print("Você não pode entrar nesta festa.")


# Exercicio 5
# #DESENVOLVA UMA FUNÇÃO PARA DESCOBRIR A IDADE DE UMA PESSOA.
    
idade = int(input("Qual e a sua idade: "))
print("Obrigado por nos informar, tenha uma boa dia")



# # Exercicio 6
# #***DESENVOLVA UM AFUNÇÃO PARA VER SE O BRASIL GANHOU A COPA DE 1999***


def copa():
     ano =  int(input('Ano da copa: '))
     copas  = [1958, 1962, 1970, 1994, 2002] 
     if ano in copas:
        print('Esse ano o Brasil ganhou a copa do mundo deste ano')
     else:
         print('O Brasil não ganhou a copa do mundo deste ano')

copa()


# Exercicio 7
#DESENVOLVA UM SISTEMA DE RESTAURANTE, ONDE O CLIENTE TEM OPÇÃO DE ESCOLHER ENTRE SALADA, MACARRONADA, SANDUICHE, SORVETE.  


meu_carrinho = []
total_valores = []
produtos = ["salada" , "macarronada" , "sanduiche", "sorvete"]
valores = [20,12,6,7]

produto1 = int(input("Digite o produto 0:"))
produto2 = int(input("Digite o produto 1:"))
produto3 = int(input("Digite o produto 2:"))
produto4 = int(input("Digite o produto 3:"))

if (produto1, produto2, produto3, produto4):
       meu_carrinho += (produtos[produto1], produtos[produto2], produtos[produto3], produtos[produto4])
       print(meu_carrinho)
       total_valores+=(valores[produto1], valores[produto2], valores[produto3], valores[produto4])
       soma = sum(total_valores)
print('Total do pedido foi R$', soma)




























