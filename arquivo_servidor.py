import socket, os

#criar socket
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Obtém o nome da máquina
nome_da_maquina = socket.gethostname()
porta = 8881

#associa a porta
socket_servidor.bind((host, porta))

#Escutando...
socket_servidor.listen()
print("Nome do servidor", host, "esperando conexão na porta", porta)

while True:
    #Aceita alguma conexão
    (socket_cliente, addr) = socket_servidor.accept()
    print("Conectado a: ", str(addr))
    
    #Recebe mensagem do cliente:
    msg = socket_cliente.recv(2048)
    nome_arquivo = msg.decode('ascii')
    if os.path.isfile(nome_arquivo):
        #Envia o tamanho primeiro
        tamanho = os.stat(nome_arquivo).st_size
        socket_cliente.send(str(tamanho).enconde('ascii'))
        #Abre o arquivo em modo leitura de bytes
        arquivo = open(nome_arquivo, 'rb')
        #Envia dados
        bytes = arquivo.read(4096)
        while bytes:
            socket_cliente.send(bytes)
            bytes = arquivo_read(4096)
        #Fecha arquivo
        arquivo.close()
    else:
        print("Não encontrou o arquivo")
        #Tamanho é -1 é para indicar que não encontrou o arquivo
        socket_cliente.send('-1'.encode('ascii'))
    #Fecha o socket cliente
    socket_cliente.close()

#Fecha o socket servidor
socket_servidor.close()
    