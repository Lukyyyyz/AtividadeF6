import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados = pd.read_csv('dados/dados_frequencia.csv')
cols_validas = [c for c in dados.columns if 'id' not in c.lower()]

plt.figure(figsize=(11, 6))

if len(cols_validas) > 0:
    alvo = cols_validas[0]
    sns.countplot(data=dados, x=alvo, order=dados[alvo].value_counts().index, palette='muted')
    plt.xlabel(alvo)
else:
    alvo = dados.columns[0]
    sns.countplot(data=dados.head(10), x=alvo, palette='muted')
    plt.xlabel(f'{alvo} (Apenas top 10)')

plt.title('Gráfico de Frequência (Contagem por Valor)')
plt.ylabel('Quantidade')
plt.grid(axis='y', linestyle=':', alpha=0.6)
plt.xticks(rotation=40)
plt.tight_layout()

plt.show()
