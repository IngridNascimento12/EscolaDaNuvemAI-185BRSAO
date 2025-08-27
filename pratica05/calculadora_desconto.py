# Requisitando a entrada do usuário
preco_original = float(input("Digite o preço do produto: "))
percentual_desconto = float(input("Digite o percentual de desconto (ex: 10): "))

# Calculando o valor do desconto
valor_desconto = preco_original * (percentual_desconto / 100)

# Calculando o preço final
preco_final = preco_original - valor_desconto

# Exibindo o preço final formatado com duas casas decimais
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Desconto de {percentual_desconto:.2f}%: R$ {valor_desconto:.2f}")
print(f"Preço final com desconto: R$ {preco_final:.2f}")