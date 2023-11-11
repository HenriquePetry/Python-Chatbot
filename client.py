import socket

def iniciar_cliente():
    host = '127.0.0.1'  # Use o mesmo host usado no servidor
    porta = 0  # Use a mesma porta usada no servidor

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        cliente.connect((host, porta))
    except Exception as e:
        print(f"Erro ao conectar: {e}")
        return

    while True:
        pergunta = input("Você: ")
        cliente.send(pergunta.encode('utf-8'))

        resposta = cliente.recv(1024).decode('utf-8')
        print(f"ChatBot: {resposta}")

        if pergunta.lower() == 'sair':
            break

    cliente.close()

if __name__ == "__main__":
    iniciar_cliente()
