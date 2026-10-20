import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('dados/dados_dispersao.csv')
cols = dados.columns

plt.figure(figsize=(11, 6))
plt.scatter(dados[cols[0]], dados[cols[1]], color='darkorange', alpha=0.75, edgecolors='black')

plt.title('Gráfico de Dispersão entre Variáveis')
plt.xlabel(cols[0])
plt.ylabel(cols[1])
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()

plt.show()
