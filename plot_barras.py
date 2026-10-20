import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados = pd.read_csv('dados/dados_barras.csv')

plt.figure(figsize=(11, 6))

cols_num = dados.select_dtypes(include=['number']).columns

if len(cols_num) > 0:
    eixo_y = cols_num[0]
    coluna_hue = 'regiao' if 'regiao' in dados.columns else None
    sns.barplot(data=dados, x='categoria', y=eixo_y, hue=coluna_hue, palette='crest')
    plt.ylabel(eixo_y)
else:
    sns.countplot(data=dados, x='categoria', hue='regiao' if 'regiao' in dados.columns else None, palette='crest')
    plt.ylabel('Quantidade (Contagem)')

plt.title('Gráfico de Barras por Categoria')
plt.xlabel('Categoria')
plt.xticks(rotation=40)
plt.grid(axis='y', linestyle=':', alpha=0.6)
plt.tight_layout()

plt.show()
