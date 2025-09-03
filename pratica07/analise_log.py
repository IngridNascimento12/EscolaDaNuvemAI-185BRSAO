import re
import numpy as np

tempos_execucao = []

with open('log_treinamento.txt', 'r') as arquivo:
    for linha in arquivo:
        match = re.search(r'Tempo: (\d+\.\d+)s', linha)
        if match:
            tempos_execucao.append(float(match.group(1)))

media = np.mean(tempos_execucao)
desvio_padrao = np.std(tempos_execucao)

print(f"Tempos de execução: {tempos_execucao}")
print(f"Média: {media:.2f}s")
print(f"Desvio Padrão: {desvio_padrao:.2f}s")