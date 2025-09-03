import csv

with open('pessoas.csv', 'r') as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    for linha in leitor:
        print(f"Nome: {linha[0]}, Idade: {linha[1]}, Cidade: {linha[2]}")