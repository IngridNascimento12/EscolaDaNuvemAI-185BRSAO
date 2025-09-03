import json

# Escrevendo dados em um arquivo JSON
dados_pessoa = {
    'nome': 'Ana',
    'idade': 28,
    'cidade': 'Curitiba'
}

with open('pessoa.json', 'w') as arquivo_json:
    json.dump(dados_pessoa, arquivo_json, indent=4)

print("Dados escritos em 'pessoa.json' com sucesso!")

# Lendo dados do arquivo JSON
with open('pessoa.json', 'r') as arquivo_json:
    dados_lidos = json.load(arquivo_json)

print("\nDados lidos do arquivo:")
print(f"Nome: {dados_lidos['nome']}")
print(f"Idade: {dados_lidos['idade']}")
print(f"Cidade: {dados_lidos['cidade']}")