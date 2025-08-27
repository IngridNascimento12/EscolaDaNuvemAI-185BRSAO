def eh_palindromo(texto):
    """
    Verifica se uma string é um palíndromo.

    Args:
        texto (str): A palavra ou frase a ser verificada.

    Returns:
        bool: True se for um palíndromo, False caso contrário.
    """
    # Remove espaços e pontuação e converte para minúsculas
    texto_limpo = "".join(char for char in texto if char.isalnum()).lower()

    # Compara a string com a sua versão invertida
    return texto_limpo == texto_limpo[::-1]

# Exemplo de uso
frase1 = "Anotaram a data da maratona"
frase2 = "python"

if eh_palindromo(frase1):
    print(f'"{frase1}" -> Sim')
else:
    print(f'"{frase1}" -> Não')

if eh_palindromo(frase2):
    print(f'"{frase2}" -> Sim')
else:
    print(f'"{frase2}" -> Não')