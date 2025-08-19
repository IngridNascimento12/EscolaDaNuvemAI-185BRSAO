# Definindo as variáveis
nome_produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20

# Calculando o valor do desconto
valor_desconto = preco_original * (porcentagem_desconto / 100)

# Calculando o preço final
preco_final = preco_original - valor_desconto

# Exibindo os resultados
print(f"Produto: {nome_produto}")
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Desconto ({porcentagem_desconto}%): R$ {valor_desconto:.2f}")
print(f"Preço final com desconto: R$ {preco_final:.2f}")