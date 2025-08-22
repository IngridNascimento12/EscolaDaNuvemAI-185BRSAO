temperatura = float(input("Digite a temperatura: "))
unidade_origem = input("Unidade de origem (C/F/K): ").upper()
unidade_destino = input("Unidade de destino (C/F/K): ").upper()

resultado = 0

if unidade_origem == "C":
    if unidade_destino == "F":
        resultado = (temperatura * 9/5) + 32
    elif unidade_destino == "K":
        resultado = temperatura + 273.15
    else:
        resultado = temperatura
elif unidade_origem == "F":
    if unidade_destino == "C":
        resultado = (temperatura - 32) * 5/9
    elif unidade_destino == "K":
        resultado = (temperatura - 32) * 5/9 + 273.15
    else:
        resultado = temperatura
elif unidade_origem == "K":
    if unidade_destino == "C":
        resultado = temperatura - 273.15
    elif unidade_destino == "F":
        resultado = (temperatura - 273.15) * 9/5 + 32
    else:
        resultado = temperatura

print(f"A temperatura convertida é: {resultado:.2f} {unidade_destino}")