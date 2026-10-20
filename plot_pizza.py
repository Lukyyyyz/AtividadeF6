import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('dados/dados_pizza.csv')
cols = dados.columns

plt.figure(figsize=(8, 8))
plt.pie(dados[cols[1]], labels=dados[cols[0]], autopct='%1.1f%%', startangle=90, colors=plt.cm.Set3.colors)

plt.title('Gráfico de Pizza - Proporção por Categoria')
plt.tight_layout()

plt.show()
