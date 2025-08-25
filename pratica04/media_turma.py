soma_notas = 0
total_notas = 0

while True:
    entrada = input("Digite a nota (0-10) ou 'fim' para sair: ")

    if entrada.lower() == 'fim':
        break  # Sai do loop

    try:
        nota = float(entrada)

        if 0 <= nota <= 10:
            soma_notas += nota
            total_notas += 1
            print(f"Nota {nota} registrada.")
        else:
            print("Nota inválida. Por favor, digite um valor entre 0 e 10.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número ou 'fim'.")

if total_notas > 0:
    media = soma_notas / total_notas
    print(f"A média da turma é: {media:.2f}")
else:
    print("Nenhuma nota válida foi inserida.")