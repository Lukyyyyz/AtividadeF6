import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados = pd.read_csv('dados/dados_distribuicao.csv')
cols = dados.columns

plt.figure(figsize=(11, 6))
sns.histplot(dados[cols[0]], kde=True, color='seagreen')

plt.title('Gráfico de Distribuição dos Valores')
plt.xlabel(cols[0])
plt.ylabel('Frequência')
plt.grid(axis='y', linestyle=':', alpha=0.6)
plt.tight_layout()

plt.show()
