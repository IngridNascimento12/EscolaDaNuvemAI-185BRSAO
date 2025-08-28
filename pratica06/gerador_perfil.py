import requests

url = "https://randomuser.me/api/"

try:
    response = requests.get(url)
    data = response.json()

    usuario = data['results'][0]
    nome = f"{usuario['name']['first']} {usuario['name']['last']}"
    email = usuario['email']
    pais = usuario['location']['country']

    print("Perfil de Usuário Aleatório:")
    print(f"Nome: {nome}")
    print(f"Email: {email}")
    print(f"País: {pais}")

except requests.exceptions.RequestException as e:
    print(f"Erro ao conectar à API: {e}")
except KeyError:
    print("Erro: A estrutura da resposta da API não é a esperada.")