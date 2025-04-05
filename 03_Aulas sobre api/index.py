import requests

# URL da API (endpoint de posts)
url = "https://jsonplaceholder.typicode.com/posts"

# Fazendo a requisição GET
response = requests.get(url)

# Verificando se a requisição foi bem-sucedida (código 200)
if response.status_code == 200:
    # Convertendo a resposta para JSON
    posts = response.json()

    # Limitando a exibição aos primeiros 5 posts
    for post in posts[:5]:
        print("UserID:", post['userId'])
        print("ID:", post['id'])
        print("Título:", post['title'])
        print("Corpo:", post['body'])
        print("-" * 100) 
else:
    print(f"Erro na requisição: Código {response.status_code}")
