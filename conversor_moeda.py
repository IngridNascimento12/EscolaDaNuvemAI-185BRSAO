# Definindo as variáveis
valor_reais = 100.00
taxa_dolar = 5.60
taxa_euro = 6.60

# Calculando os valores convertidos
valor_dolar = valor_reais / taxa_dolar
valor_euro = valor_reais / taxa_euro

# Exibindo os resultados arredondados para duas casas decimais
print(f"R$ {valor_reais} equivalem a:")
print(f"US$ {valor_dolar:.2f}")
print(f"€ {valor_euro:.2f}")