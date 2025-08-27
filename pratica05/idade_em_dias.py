from datetime import date

def calcular_idade_em_dias(ano_nascimento):
    """
    Calcula a idade de uma pessoa em dias.

    Args:
        ano_nascimento (int): O ano de nascimento da pessoa.

    Returns:
        int: A idade em dias.
    """
    data_atual = date.today()
    data_nascimento = date(ano_nascimento, 1, 1)
    diferenca_dias = (data_atual - data_nascimento).days
    return diferenca_dias

# Exemplo de uso
ano_nascimento = int(input("Digite o ano de nascimento: "))
idade_dias = calcular_idade_em_dias(ano_nascimento)

print(f"A pessoa tem aproximadamente {idade_dias} dias de vida.")