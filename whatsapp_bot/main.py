import requests

def enviar_mensagem(numero: str, mensagem: str):
    url = "http://localhost:21465/api/send-message"
    payload = {
        "phone": numero,
        "message": mensagem
    }

    try:
        resposta = requests.post(url, json=payload)
        if resposta.status_code == 200:
            print("Mensagem enviada com sucesso:", resposta.json())
        else:
            print("Erro ao enviar mensagem:", resposta.status_code, resposta.text)
    except Exception as e:
        print("Erro de conexão:", e)

if __name__ == "__main__":
    numero_destino = input("Digite o número com DDI e DDD (ex: 5511999999999): ")
    texto = input("Digite a mensagem: ")
    enviar_mensagem(numero_destino, texto)
