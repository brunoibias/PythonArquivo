print('*' * 40)
print('*', ' ' * 36, '*')
print('* Aluno: BRUNO IBIAS PEREIRA', ' '*9, '*')
print('* Prof: SERGIO', ' '*23, '*')
print('* EM S2 Python S2', ' '*20, '*')
print('*', ' ' * 36, '*')
print('*' * 40)

arquivoCliente = "Cliente.txt" # Nome do arquivo de texto

def leArquivoCliente():                # Função que le o arquivo de texto
    try:                         # Tratamento de erro
        arq = open(arquivoCliente,"r+") # Abre o arquivo para leitura
        print( '\n'+arq.read() ) # Quebra linha e mostra o conteudo
        arq.close()              # Fecha o arquivo
    except IOError:              # Tratamento de erro
        print('\nArquivo não encontrado!')

def escreveArquivoCliente(texto):        # Função que le e escreve no arquivo
    try:                           # Tratamento de erro
        arq = open(arquivoCliente,"a+")   # Abre o arquivo para gravação no final do arquivo
        arq.writelines('\n'+texto) # Escreve no arquivo o parametro 'texto'
        arq.close()                # Fecha o arquivo
        print('\nRegistro gravado com sucesso')
    except IOError:                # Tratamento de erro
        print('\nErro ao abrir o arquivo!') # Mostra na tela uma mensagem de erro

arquivoFornecedor = "Fornecedor.txt" 

def leArquivoFornecedor():                
    try:                         
        arq = open(arquivoFornecedor,"r+") 
        print( '\n'+arq.read() ) 
        arq.close()              
    except IOError:              
        print('\nArquivo não encontrado!')

def escreveArquivoFornecedor(texto):       
    try:                           
        arq = open(arquivoFornecedor,"a+")   
        arq.writelines('\n'+texto) 
        arq.close()                
        print('\nRegistro gravado com sucesso')
    except IOError:                
        print('\nErro ao abrir o arquivo!') 

while(True):                     # Loop infinito 
    print('\nEscolha a opcao:')
    print('1-Cadastrar Cliente')
    print('2-Cadastrar Fornecedor')
    print('3-Listar Cliente')
    print('4-Listar Fornecedor')
    print('5-Pesquisar Fornecedor ')
    print('6-Pesquisar Cliente ')
    print('0-Sair')
    vOpcao = int(input('Porfavor digite a sua opcao:')) # Entrada da opcao pelo teclado

    if vOpcao == 1:                           # Se a opcao for 1
        nome = input('\nPorfavor digite o nome do Cliente:')      # Entrada do nome pelo teclado
        nome = (nome)          # Recebe o nome + o telefone
        escreveArquivoCliente(str(nome))            # Chama a função que grava em arquivo
    elif vOpcao == 2:                           # Se a opcao for 2
        nome = input('\nPorfavor digite o nome do Fornecedor:')      # Entrada do nome pelo teclado
        nome = (nome)          # Recebe o nome + o telefone
        escreveArquivoFornecedor(str(nome))            # Chama a função que grava em arquivo
    elif vOpcao == 3:             # Se a opcao for 3
        leArquivoCliente()              # Chama a função que le o arquivo
    elif vOpcao == 4:             # Se a opcao for 4
        leArquivoFornecedor()              # Chama a função que le o arquivo
    elif vOpcao == 5:
        nomeCliente = input('Digite um nome do cliente que deseja pesquisar:')
        with open('arquivoCliente.txt') as f:
            if nomeCliente in f.read():
                arq = open('arquivoCliente.txt', "r+")
                print('\n'+arq.read())
                arq.close()
            else:
                print('Não encontrado !!!! ')
    elif vOpcao == 6:
        nomeFornecedor = input('Digite um nome do fornecedor que deseja pesquisar: ')
        with open('arquivoFornecedor.txt') as f:
            if nomeFornecedor in f.read():
                arq = open('arquivoFornecedor.txt', "r+")
                print('\n'+arq.read())
                arq.close()
            else:
                print('Não encontrado !!!! ')
    elif vOpcao == 0:             # Se a opcao for 0
        break                     # Quebra o laço infinito

    
   