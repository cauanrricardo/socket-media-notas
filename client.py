
import socket

# IP do servidor (se for no mesmo PC, use localhost)
HOST = "192.168.0.2"   
PORT = 5000

# Cria o socket TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta ao servidor
client.connect((HOST, PORT))

# Envia mensagem
mensagem = input("Digite uma mensagem para o servidor: ")
client.send(mensagem.encode())

# Recebe resposta
resposta = client.recv(1024).decode()
print("Servidor respondeu:", resposta)

# Fecha conexão
client.close()
