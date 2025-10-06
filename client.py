
import socket

# IP do servidor (se for no mesmo PC, use localhost)
HOST = "192.168.0.2"   
PORT = 5000

# cria o socket TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# conecta ao servidor
client.connect((HOST, PORT))

# envia mensagem
mensagem = input("Digite uma mensagem para o servidor: ")
client.send(mensagem.encode())

# recebe resposta
resposta = client.recv(1024).decode()
print("Servidor respondeu:", resposta)


client.close()
