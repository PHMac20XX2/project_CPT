import getpass

def men_inicial(x):
    print (x)
men_inicial("     Pagamentos     ")
print (10 * ('---'))

def insert_valor(valor):
    insert_valor = valor 
valor = (input("Valor da conta: "))
print (f"Total da conta:{valor}") 

print (10 * ('---'))

def entrada_card(opcao):
    entrada_card = int (opcao)

opcao = int (input ('''
               
     Escolha uma das opções:               
|-------------||-------------------|
|[1] Crédito  ||[3]Vale-Refeição   |
|-------------||-------------------|
|[2] Débito   ||[4]Vale-Alimentação|
|-------------||-------------------|

:'''))

print (10 * ("----"))

def senha_bd():
    senha = int (getpass.getpass(prompt="Digite sua senha: ", stream=None))  
senha = 1234
    
def opc ():
    entrada_card()
  
if opcao == 1:
    senha_bd()
    
    if senha == 1234:
        print ("Transação aceita!")