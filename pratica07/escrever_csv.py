import csv

dados_pessoais = [
    ['Nome', 'Idade', 'Cidade'],
    ['João', 30, 'São Paulo'],
    ['Maria', 25, 'Rio de Janeiro'],
    ['Pedro', 40, 'Belo Horizonte']
]

with open('pessoas.csv', 'w', newline='') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    for linha in dados_pessoais:
        escritor.writerow(linha)

print("Dados escritos em 'pessoas.csv' com sucesso!")