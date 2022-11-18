import getpass

def men_inicial(x):
    print (x)
men_inicial("     Pagamentos     ")
print (10 * ('---'))

def insert_valor(valor):
    insert_valor = valor 
valor = input("Digite o valor: ")

if valor.isnumeric():
 print (f"Total da conta: R$ {valor} ") 
else:
    print("Valor Invalído")
    exit()
    
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

print (10 * ("---"))

def senha_bd(chama_s):
    senha = 1234
senha_cred = 2458
senha_deb = 1234
chama_s = int (getpass.getpass(prompt="Digite sua senha: ", stream=None))  

'''def tentativa(tent):
    senha_bd()

tent = 0

while tent < 3:
    if chama_s != senha_cred:
      print ("Senha incorreta") 
      break'''
           
def opc_cred ():
    entrada_card()
    
if opcao == 1:
    senha_bd(chama_s)   
    if chama_s == senha_cred:
        print ("Transação aceita!")
    else:
        exit() 
        
def opc_deb():
    entrada_card()
    
if opcao == 2:
   senha_bd(chama_s)
   if chama_s == senha_deb:
         print ("Transação aceita!")
   else:
       exit()
         
def nf():
    opc_deb()
    insert_valor()

if chama_s == senha_deb:  
      
   arquivo = open("nf.txt", "w")

linha = list()
linha.append("      | Nota Fiscal | \n       ")
linha.append("Modo de pagamento: Debito \n")
linha.append(f"       Valor da Conta: R$ {valor} \n")

arquivo.writelines(linha)
 
arquivo = open("nf.txt","r")


    