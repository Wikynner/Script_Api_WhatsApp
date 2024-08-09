#Codigo Simples para automatição de mensagem Via whatsapp atravéz de API_Whatsapp gratuita (https://comunidadezdg.com.br/api-gratis-2024/)
# Necessario seguir instruçoes presentes no link acima para baixar e instalar a api
#Após Seguir todos os procedimentos ultilize este codigo para fazer seus testes e se comunicar com a api
#OBS: api_key foi trocada para 2024controladoria4202 mas voce pode colocar a api_key que desejar na parte do .env .Inicialmente vem como padrão Comunidadezdg.com.br


import http.client
import json

# Configurações da API
host = "localhost"  
port = 3000  # porta onde a API roda por padrao
endpoint = "/client/sendMessage/comunidadezdg" #endpoint para enviar mensagem 

# Sua chave de API
api_key = "2024controladoria4202" #Inicialmente vem como padrão Comunidadezdg.com.br

# Dados da mensagem
data = {
    "chatId": "5565123456789@c.us", # Identificador do numero para onde a mensagem será enviada.tem que seguir este modelo DDI (55)Brasil, DDD(Regiao onde o numero pertence) e o numero do celular
    "contentType": "string", #Tipo de conteúdo da mensagem (neste caso, string).
    "content": """🚀 Novidade Quentinha! 📲✨
    
Agora, estamos ainda mais conectados com você! 🤝
💬 A partir de hoje, começamos a enviar mensagens automáticas pelo WhatsApp. 🎉📢

🔔 Receba atualizações instantâneas, promoções exclusivas 🛍️, 
lembretes importantes 🗓️ e muito mais, tudo de forma rápida e prática. ⚡🤩

Fique ligado e não perca nenhuma novidade! 😉👍

Caso tenha alguma dúvida, estamos por aqui para ajudar! 🤗💬

Um grande abraço da nossa equipe! 🤗✨
"""
    
     # Conteudo  que sera enviado 
}

# Convertendo os dados para JSON
json_data = json.dumps(data)

# Criando a conexão HTTP
conn = http.client.HTTPConnection(host, port)

# Cabeçalhos da requisição
headers = {
    "Content-Type": "application/json",
    "x-api-key": api_key  # Adicionando a chave de API no cabeçalho
}
#print(headers)
# Fazendo a requisição POST
conn.request("POST", endpoint, body=json_data, headers=headers)

# Obtendo a resposta
response = conn.getresponse()
response_data = response.read().decode('utf-8')

# Verificando a resposta
if response.status == 200:
    print("Mensagem enviada com sucesso!")
    print("Resposta do servidor:", response_data)
else:
    print(f"Erro ao enviar a mensagem: {response.status}")
    print("Detalhes:", response_data)

# Fechando a conexão
conn.close()
