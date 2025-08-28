import requests

def consultar_cep(cep):
    """
    Consulta informações de endereço a partir de um CEP.
    """
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        response = requests.get(url)
        data = response.json()
        if 'erro' in data:
            return None
        return data
    except requests.exceptions.RequestException:
        return None

cep_usuario = input("Digite o CEP (apenas números): ")

dados_cep = consultar_cep(cep_usuario)

if dados_cep:
    print(f"Logradouro: {dados_cep.get('logradouro')}")
    print(f"Bairro: {dados_cep.get('bairro')}")
    print(f"Cidade: {dados_cep.get('localidade')}")
    print(f"Estado: {dados_cep.get('uf')}")
else:
    print("CEP não encontrado ou inválido.")