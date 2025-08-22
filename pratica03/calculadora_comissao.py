nome_vendedor = input("Digite o nome do vendedor: ")
salario_fixo = float(input("Digite o salário fixo: "))
total_vendas = float(input("Digite o total de vendas (em dinheiro): "))

comissao = total_vendas * 0.15
salario_final = salario_fixo + comissao

print(f"TOTAL = R$ {salario_final:.2f}")