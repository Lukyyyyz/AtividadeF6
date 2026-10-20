import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados = pd.read_csv('dados/dados_regressao.csv')
cols = dados.columns

plt.figure(figsize=(11, 6))
sns.regplot(data=dados, x=cols[0], y=cols[1], scatter_kws={'alpha': 0.7}, line_kws={'color': 'crimson'})

plt.title('Gráfico de Regressão Linear Simples')
plt.xlabel(cols[0])
plt.ylabel(cols[1])
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()

plt.show()
