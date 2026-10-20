import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('dados/dados_linhas.csv')
cols = dados.columns

plt.figure(figsize=(11, 6))
plt.plot(dados[cols[0]], dados[cols[1]], marker='s', linewidth=2.5, color='royalblue')

plt.title('Gráfico de Linhas - Evolução dos Dados')
plt.xlabel(cols[0])
plt.ylabel(cols[1])
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()

plt.show()
