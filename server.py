import socket

# Dicionário de perguntas e respostas (em minúsculas)
perguntas_respostas = {
    "tudo bem?": "Sim, tudo ótimo!",
    "quais são os serviços oferecidos?": "Oferecemos consultas, vacinações, cirurgias e outros serviços veterinários.",
    "qual é o horário de funcionamento?": "Estamos abertos de segunda a sexta, das 9h às 18h, e aos sábados, das 9h às 12h.",
    "vocês atendem emergências?": "Sim, atendemos emergências 24 horas por dia, 7 dias por semana.",
    "quanto custa uma consulta?": "O custo de uma consulta varia dependendo do tipo de serviço. Recomendamos entrar em contato para obter informações específicas.",
    "vocês oferecem serviços de banho e tosa?": "Sim, oferecemos serviços de banho e tosa para animais de estimação.",
    "quais são os veterinários disponíveis?": "Temos uma equipe dedicada de veterinários altamente qualificados. Eles estão disponíveis para atender às necessidades de saúde do seu animal de estimação.",
    "como faço para marcar uma consulta?": "Você pode marcar uma consulta ligando para o nosso número ou visitando a clínica pessoalmente.",
    "qual é o endereço da clínica?": "Estamos localizados em [seu endereço].",
    "sair": "Obrigado por utilizar nossos serviços veterinários! Se precisar de mais alguma coisa, estamos aqui para ajudar."
}

def iniciar_servidor():
    host = '127.0.0.1'
    porta = 0

    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((host, porta))
    servidor.listen(1)

    print(f"Servidor aguardando conexão na porta {porta}...")

    conexao, endereco = servidor.accept()
    print(f"Conectado por {endereco}")

    while True:
        pergunta = conexao.recv(1024).decode('utf-8').lower()  # Converter para minúsculas
        if not pergunta:
            break

        resposta = perguntas_respostas.get(pergunta, "Desculpe, não entendi sua pergunta. Pode reformular?")
        conexao.send(resposta.encode('utf-8'))

    conexao.close()

if __name__ == "__main__":
    iniciar_servidor()
