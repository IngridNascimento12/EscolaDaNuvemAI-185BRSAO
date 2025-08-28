import random
import string

def gerar_senha(tamanho):
    """
    Gera uma senha aleatória com caracteres especiais.
    """
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    return senha

tamanho_senha = int(input("Digite a quantidade de caracteres para a senha: "))
senha_gerada = gerar_senha(tamanho_senha)
print(f"Sua senha aleatória é: {senha_gerada}")