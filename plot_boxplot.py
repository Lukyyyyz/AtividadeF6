import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados = pd.read_csv('dados/dados_boxplot.csv')

plt.figure(figsize=(11, 6))
dados_num = dados.select_dtypes(include=['number'])
sns.boxplot(data=dados_num, palette='Set3')

plt.title('Gráfico de Boxplot - Dispersão das Variáveis')
plt.grid(axis='y', linestyle=':', alpha=0.6)
plt.tight_layout()

plt.show()
