while True:
    try:
        # Solicitando a entrada do usuário
        num1 = float(input("Digite o primeiro número: "))
        operacao = input("Digite a operação (+, -, *, /): ")
        num2 = float(input("Digite o segundo número: "))

        resultado = 0

        # Verificando a operação
        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 == 0:
                # Divisão por zero é um erro específico
                print("Erro: Divisão por zero não é permitida.")
                continue  # Continua o loop para pedir nova entrada
            resultado = num1 / num2
        else:
            # Operação inválida
            print("Erro: Operação inválida. Use +, -, *, ou /.")
            continue  # Continua o loop

        # Se tudo deu certo, exibe o resultado e encerra
        print(f"O resultado é: {resultado}")
        break  # Encerra o loop e o programa

    except ValueError:
        # Captura erro se o usuário digitar algo que não é número
        print("Erro: Entrada inválida. Por favor, digite números.")
        continue  # Continua o loop