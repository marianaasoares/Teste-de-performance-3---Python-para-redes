# Servidor
import socket, psutil, pickle

# Cria o socket
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# Obtem o nome da máquina
host = socket.gethostname()                         
porta = 9991
# Associa a porta
socket_servidor.bind((host, porta))
# Escutando...
socket_servidor.listen()
print("Servidor de nome", host, "esperando conexão na porta", porta)
# Aceita alguma conexão
(socket_cliente,addr) = socket_servidor.accept()
print("Conectado a:", str(addr))

while True:
  # Recebe pedido do cliente:
  msg = socket_cliente.recv(4)
  if msg.decode('ascii') == 'fim':
      break
  # Gera a lista de resposta
  resposta = [p.name() for p in psutil.process_iter()]
  resposta.append(resposta)
  # Prepara a lista para o envio
  bytes_resp = pickle.dumps(resposta)
  # Envia os dados
  socket_cliente.send(bytes_resp)

# Fecha socket do servidor e cliente
socket_cliente.close()
socket_servidor.close()
  
