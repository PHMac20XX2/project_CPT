import getpass

def men_ini(text):
    text = print (" -----> Maquininha de Pagamentos <----- ")
    return men_ini  

def entry_card():
    opcao = int (opcao)
    
    opcao = input(''' Tipos de cartão aceito
                    
 [1] Crédito:
 [2] Débito: 
 
 Digite o número do tipo de cartão: ''')

def puxa_opcao(opcao): 
    entry_card()

    if opcao == 1:
        print ("Opção escolhida: Crédito:")
    elif opcao == 2:
        print ("Opção escolhida: Débito: ")
    else:
        print ("Opção incorreta, escolha entre as existentes")
        
''' def senha(senha_bd):
    senha = int (senha_bd)
senha_bd = 1234

def maq_func(opcao, senha_bd):
    
    entry_card()
    
    puxa_opcao()
    
    senha()
    senha = (getpass.getpass(prompt="Digite a senha: ", stream=None)) '''
