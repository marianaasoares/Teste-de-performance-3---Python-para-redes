import socket, sys, os

#Imprime o status de download
def imprime_status(bytes, tam):
    kbytes = bytes/1024
    tam_bytes = tam/1024
    texto = 'Baixando...'
    texto = texto + '{:<.2f}'.format(kbytes) + ' KB '
    texto = texto + 'de ' + '{:<.2f}'.format(tam_bytes) + ' KB'
    print(texto)

#Cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

nome_arquivo = input("Entre com o nome do arquivo: ")

try:
    #Tenta se conectar ao servidor
    s.connect((socket.gethostname(), 8881))
    #Envia o nome do arquivo:
    s.send(nome_arquivo.encode('ascii'))
    #Recebe o tamanho do arquivo:
    msg = s.recv(12)
    tamanho = int(msg.decode('ascii'))
    #Checa se o tamanho do arquivo existe no servidor:
    if tamanho >= 0:
        #Gera o arquivo local na pasta de download
        arquivo = open('download\\' + nome_arq, "wb")
        soma = 0
        bytes = s.recv(4096)
        #Escreve o arquivo
        while bytes:
            arq.write(bytes)
            #Impressão do status de download
            soma = soma + len(bytes)
            os.system('cls')
            imprime_status(soma, tamanho)
            bytes = s.recv(4096)
        #Fecha o arquivo
        arquivo.close()
    else:
        print('Arquivo não encontrado no servidor!')
except Exception as erro:
    print(str(erro))

#Fecha socket
    s.close()

input("Pressione qualquer tecla para sair...")