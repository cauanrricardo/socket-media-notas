# Comunicação Cliente/Servidor TCP — Média de Notas

- Projeto/trabalho de Redes de Computadores; Desenvolvido em **dupla** durante o estudo do capítulo 2 do livro _Computer Networking: A Top-Down Approach (Kurose, 8ª ed.)_,
- com o objetivo de compreender a comunicação entre processos via **sockets TCP**.

---

## Integrantes

- **Cauan Ricardo** — Servidor
- **Rodrigo Rodrigues** — Cliente

Ambos conectados na **mesma rede Wi-Fi**, realizando comunicação real entre dois computadores utilizando **endereçamento IP** e **porta TCP**.

---

## Descrição do projeto

O sistema cliente-servidor foi implementado em **Python**.  
O cliente envia **três notas numéricas** ao servidor, que calcula a **média aritmética** e devolve o resultado acompanhado do status acadêmico:

| Resultado            | Significado   |
| -------------------- | ------------- |
| Aprovado             | Média ≥ 7     |
| AF (Avaliação Final) | 4 ≤ Média < 7 |
| Reprovado            | Média < 4     |

---

## Funcionalidades

- Comunicação **TCP/IP** confiável entre dois dispositivos reais.
- Troca bidirecional de mensagens (envio e resposta).
- Cálculo automático da média e retorno do status.
- Implementação validada entre dois notebooks conectados na mesma rede local.

---

## Estrutura do Projeto

| Arquivo                        | Descrição                                                             |
| ------------------------------ | --------------------------------------------------------------------- |
| `server.py`                    | Servidor TCP — recebe as notas, calcula a média e envia o resultado   |
| `client.py`                    | Cliente TCP — envia as notas e exibe a resposta recebida              |
| `imagem-terminal-servidor.png` | Captura do terminal do servidor mostrando conexão e cálculo da média  |
| `imagem-terminal-cliente.png`  | Captura do terminal do cliente mostrando envio e resposta da mensagem |

> ⚙️ Este projeto foi desenvolvido com base em estudos de redes e apoio em materiais didáticos e explicações assistidas por IA (ChatGPT).  
> Todo o código foi testado e adptado pro nosso interesse.

