while True:
    senha = input("Crie uma senha forte (mínimo 8 caracteres, com número) ou 'sair': ")

    if senha.lower() == 'sair':
        break

    # Verificando se a senha é forte
    tem_numero = any(char.isdigit() for char in senha)

    if len(senha) >= 8 and tem_numero:
        print("Senha forte. Acesso concedido.")
        break
    else:
        if len(senha) < 8:
            print("Erro: A senha deve ter pelo menos 8 caracteres.")
        if not tem_numero:
            print("Erro: A senha deve conter pelo menos um número.")