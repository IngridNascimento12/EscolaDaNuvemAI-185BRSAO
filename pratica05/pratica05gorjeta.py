def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    """
    Calcula o valor da gorjeta.

    Args:
        valor_conta (float): O valor total da conta.
        porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%).

    Returns:
        float: O valor da gorjeta calculada.
    """
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

# Exemplo de uso da função
valor_total = 75.50
porcentagem = 15
valor_gorjeta = calcular_gorjeta(valor_total, porcentagem)

print(f"O valor da conta foi de R$ {valor_total:.2f}")
print(f"A gorjeta de {porcentagem}% é de R$ {valor_gorjeta:.2f}")
print(f"O total a ser pago é de R$ {valor_total + valor_gorjeta:.2f}")