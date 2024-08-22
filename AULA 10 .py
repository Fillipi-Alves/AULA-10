# def soma():
#     n = 10
#     n2 = 20
#     result = n +n2
#     print (result)

#soma()

# print('Ola mundo')

# def display():
#     print('Ola mundo')

#     display()

def soma():
    n1 = int(input('>>'))
    n2 = int(input('>>'))
    r =  n1 + n2
    print(r)

def sub():
    n1 = int(input('>>'))
    n2 = int(input('>>'))
    r =  n1 - n2
    print(r)


def mult():
    n1 = int(input('>>'))
    n2 = int(input('>>'))
    r =  n1 * n2
    print(r)



def div():
    n1 = int(input('>>'))
    n2 = int(input('>>'))
    r =  n1 / n2
    print(r)            



def calculadora():
  
    escolha  =  input('+ | - | * | / Escolha a operação: ')
    
    if escolha == '+':
       soma() 
    elif escolha == '-':
        sub()
    elif escolha == '*':
         mult()
    elif escolha == '/':
        div()

    else:
        print('Essa opção não existe')  

while True:
      calculadora()      
