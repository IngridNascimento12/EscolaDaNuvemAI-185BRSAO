# Lendo os valores de entrada do usuário
numero_funcionario = int(input())
horas_trabalhadas = int(input())
valor_por_hora = float(input())

# Calculando o salário
salario = horas_trabalhadas * valor_por_hora

# Exibindo o resultado formatado
print(f"NUMBER = {numero_funcionario}")
print(f"SALARY = R$ {salario:.2f}")