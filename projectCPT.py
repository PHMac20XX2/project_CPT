import getpass
import time


def pula_linha():
    print()

pula_linha()

def men_inicial(x):
    print (x)
men_inicial("         -> Restaurante TPC  <-       ")


print (10 * ('____'))


pula_linha()


def insert_valor(valor):
    pula_linha()
valor = input("Digite o valor: ")
time.sleep(1.0)
pula_linha()
if valor.isnumeric():
   print (f"Total da conta: R$ {valor} ") 
else:
    print("Valor Invalído")
    exit()
  

print (10 * ('____'))


def entrada_card(opcao):
    entrada_card = int (opcao)

opcao = int (input ('''   
                    
            CARTÕES ACEITOS                                
 ______________________________________ 
|                 ||                   |
|[1] Crédito      ||[3]Vale-Refeição   |
|_________________||___________________|
|                 ||                   |
|[2] Débito       ||[4]Vale-Alimentação|
|_________________||___________________|

Escolha uma das opções: '''))


print (10 * ("____"))


def senha_bd(chama_s):
    senha = 1234
senha_cred = 2458
senha_deb = 1234
pula_linha()
chama_s = int (getpass.getpass(prompt="Digite sua senha: ", stream=None))  
               
def opc_cred ():
    entrada_card()   
if opcao == 1:
    senha_bd(chama_s)   
    if chama_s == senha_cred:
        time.sleep(1.5)
        print ("Transação aceita!")

               
def opc_deb():
    entrada_card()   
if opcao == 2:
   senha_bd(chama_s)
   if chama_s == senha_deb:
         time.sleep(1.5)
         print ("Transação aceita!")


# Função para gerar nota fiscal                      
def nf():
    opc_deb()
    insert_valor()
if chama_s == senha_deb: # Caso a senha seja a correta...
    print("Gerando nota fiscal")
    # Tempo de carregamento
    time.sleep(2.0)
nota = open("nf.txt", "w") # Criando arquivo "nf.txt"

linha = list()
linha.append(''' 
             
             ___________________________________
             |                                 |
             |           Nota Fiscal           |  
             |                                 |
             |                                 |
             |    Modo de Pagamento: Debito    |
             |                                 |
             |_________________________________|
              
                    
                ''')

linha.append(f"       Valor da Conta: R$ {valor} \n")

nota.writelines(linha)

nota = open("nf.txt", "w") # Criando arquivo "nf.txt"

print('''
      
     ___________________________     
    |                           |  
    |                           |
    | Nota Fiscal Gerada!       |
    | Obrigado pela preferencia |
    |                           |
    |___________________________|  
            
                                           ''')





    