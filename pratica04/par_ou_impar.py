pares = 0
impares = 0

while True:
    entrada = input("Digite um número inteiro ou 'fim' para sair: ")

    if entrada.lower() == 'fim':
        break

    try:
        numero = int(entrada)

        if numero % 2 == 0:
            print(f"O número {numero} é par.")
            pares += 1
        else:
            print(f"O número {numero} é ímpar.")
            impares += 1
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um número inteiro.")

print("--- Resumo ---")
print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")