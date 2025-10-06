import socket

# Cria o socket TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associa IP e porta (0.0.0.0 significa "todas interfaces")
server.bind(("0.0.0.0", 5000))
server.listen(1)

print("Servidor esperando conexão...")

# Aceita conexão
conn, addr = server.accept()
print(f"Conectado a {addr}")

# Recebe dados do cliente
data = conn.recv(1024).decode()
print(f"Recebi: {data}")

# Espera que o cliente envie algo como: "6.5 7 8"
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

# Envia resposta
conn.send(f"Média: {media:.2f} - {resultado}".encode())
print(f"Resultado enviado: {resultado} (média {media:.2f})")

# Fecha conexão
conn.close()
server.close()