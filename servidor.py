import socket

# cria o socket TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# associa IP e porta (0.0.0.0 significa "todas interfaces")
server.bind(("0.0.0.0", 5000))
server.listen(1)

print("Servidor esperando conexão...")

# aceita conexão
conn, addr = server.accept()
print(f"Conectado a {addr}")

# recebe dados do cliente
data = conn.recv(1024).decode()
print(f"Recebi: {data}")

# espera resposta do cliente
try:
    notas = [float(n) for n in data.split()]
    if len(notas) != 3:
        raise ValueError
except ValueError:
    conn.send("Envie exatamente 3 notas separadas por espaço.".encode())
    conn.close()
    server.close()
    exit()


media = sum(notas) / 3


if media >= 7:
    resultado = "Aprovado"
elif 4 <= media < 7:
    resultado = "AF"
else:
    resultado = "Reprovado"

# envia resposta
conn.send(f"Média: {media:.2f} - {resultado}".encode())
print(f"Resultado enviado: {resultado} (média {media:.2f})")

# fecha conexão
conn.close()
server.close()
