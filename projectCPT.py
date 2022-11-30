import getpass # Módulo para ocultar a senha dos cartões;
import time #import do módulo TIME para criar um tempo de espera entre as respostas

from datetime import datetime # Import para usar a data e hora;

# Função determinar a data e hora;
def d1():
    pula_linha()
dha = datetime.now()
dht = dha.strftime('%d/%m/%Y %H:%M')

def pula_linha(): # Função pula linha;
    print() 

pula_linha()

def men_inicial(x): # Printar a primeira mensagem na tela;
    print (x)
men_inicial("         -> Restaurante TPC  <-       ")

# Printar uma linha;  
print (10 * ('____'))

pula_linha()

def insert_valor(valor):
    pula_linha()

# Inserir o valor da conta;
valor = input("Digite o Valor: ") 
time.sleep(1.0) # Cria um tempo de espera no valor de 1 segundo;
pula_linha()
if valor.isnumeric():
    # Caso valor seja numerico, printar o solicitado;
   print (f"Total da Conta: R$ {valor} ") 
else:
    # Caso não seja numerico
    print("Valor Invalído!")
    exit()  

print (10 * ('____'))

def entrada_card(opcao): # Função dos cartões aceitos
    pula_linha()

opcao = int (input ('''   
                    
            CARTÕES ACEITOS                                
 ______________________________________ 
|                 ||                   |
|[1] Crédito      ||[3]Vale-Refeição   |
|_________________||___________________|
|                 ||                   |
|[2] Débito       ||[4]Vale-Alimentação|
|_________________||___________________|

          Escolha uma das opções
                  
                 ->  '''))

time.sleep(2.5)

print (10 * ("____"))

def opc_error():
    entrada_card(opcao)

if opcao > 4: # Caso seja númerico é maior que 4;
    pula_linha()
    print('''
           _____________________
          |  Opcão inexistente  |
          |  Repita o processo  | 
          |_____________________|
                                   ''')
    print (10 * ("____"))
    pula_linha()
    exit() # Parar o código;

def senha_bd(chama_s):
    entrada_card(opcao)
# Senhas Pré-definidas;
senha_cred = 2458
senha_deb = 1234
senha_vr = 7987
senha_va = 6543
pula_linha()    
chama_s = int (getpass.getpass(prompt="Digite sua senha: ", stream=None))     
print (10 * ("____"))
               
def opc_cred ():   # Função para se caso for escolhido crédito
    entrada_card()   
if opcao == 1:
    opc_val = ("Crédito")
    senha_bd(chama_s)   
    if chama_s == senha_cred:
        time.sleep(1.5)
        print (10 * ('____'))
        print ('''            
          Transação aceita!            ''')
        pula_linha()  
    else:
         time.sleep(1.5)
         pula_linha()
         print('''  
         _____________________
         |                   |  
         |  Senha Incorreta! |
         | Repita o processo |
         |___________________|
                                ''')
         
         pula_linha()
         exit()
          
def opc_deb():   # Função para se caso for escolhido débito
    entrada_card()   
if opcao == 2:
   opc_val = ("Débito")
   senha_bd(chama_s)
   if chama_s == senha_deb:
         time.sleep(1.5)
         print ('''            
           Transação aceita!            ''')
         pula_linha()  
   else:
       time.sleep(1.5)
       pula_linha()
       print('''  
         _____________________
         |                   |  
         |  Senha Incorreta! |
         | Repita o processo |
         |___________________|
                                ''')
             
       pula_linha()
       exit()
       
def opc_vr():    # Função para se caso for escolhido vr (vale-refeição)
    entrada_card()
if opcao == 3:
    opc_val = ("Vale-Refeição")
    senha_bd(chama_s)
    if chama_s == senha_vr:
        time.sleep(1.5)
        print ('''            
          Transação aceita!            ''')
        pula_linha()  
    else:
      time.sleep(1.5)
      pula_linha()
      print('''  
         _____________________
         |                   |  
         |  Senha Incorreta! |
         | Repita o processo |
         |___________________|
                                ''')
            
      pula_linha()
      exit()

def opc_va():    # Função para se caso for escolhido va (vale-alimentação)
    entrada_card()
if opcao == 4:
    opc_val = ("Vale-Alimentação")
    senha_bd(chama_s)
    if chama_s == senha_va:
        time.sleep(1.5)
        print ('''            
          Transação aceita!            ''')
        pula_linha()  
    else:
     time.sleep(1.5)
     pula_linha()
     print('''  
         _____________________
         |                   |  
         |  Senha Incorreta! |
         | Repita o processo |
         |___________________|
                                ''')
         
     pula_linha()
     exit()
                             
# Função para gerar nota fiscal                      
def nf():
    d1()
    insert_valor()
if chama_s == senha_deb or chama_s == senha_cred or chama_s == senha_vr or senha_va: # Caso a senha seja a correta...
    pula_linha()
    print("        Gerando nota fiscal...     ")
    # Tempo de carregamento
    time.sleep(2.0)
nota = open("nf.txt", "w", encoding="utf-8") # Criando arquivo "nf.txt"
linha = list()

# Usando f-strings
linha.append(f'''
             
     _________________________________
    |                                 |
    |          Nota Fiscal            |
    |                                 |
    |                                 |   
    |   Gerado em: {dht}   |
    |                                 |
    |                                 |
    |    Modo de Pagamento: {opc_val}    |
    |                                 |
    |                                 |                           
    |     Valor da Conta: R$ {valor}      |
    |                                 |
    |_________________________________|
              
                    
                ''')

nota.writelines(linha) # Escrever nas linhas
time.sleep(1.5)
print('''
      
      ___________________________     
     |                           |  
     |                           |
     | Nota Fiscal Gerada!       |
     | Obrigado pela preferencia |
     |                           |
     |___________________________|  
            
                                           ''')

nota = open("nf.txt", "r") # Abrir e ler o arquivo
time.sleep(2.0)
exit()
