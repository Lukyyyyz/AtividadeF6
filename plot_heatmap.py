import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados = pd.read_csv('dados/dados_heatmap.csv')

dados_num = dados.select_dtypes(include=['number'])

plt.figure(figsize=(11, 8))
sns.heatmap(dados_num, annot=True, cmap='magma', fmt='.2f')
plt.title('Mapa de Calor (Heatmap) dos Dados Numéricos')
plt.tight_layout()

plt.show()
