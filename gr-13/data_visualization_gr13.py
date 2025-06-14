import pandas as pd
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

# Carregar a tabela gerada na preparação
caminho_arquivo =  os.getenv('caminho_gr13')
pivot_df = pd.read_excel(caminho_arquivo)


# Plotar evolução absoluta
# plt.figure(figsize=(10, 6))
# for coluna in ['Formado', 'trancado', 'jubilado', 'Cancelado por abandono', 'Cancelado', 'abandono']:
#     plt.plot(pivot_df['PERIODO LETIVO'], pivot_df[coluna], marker='o', label=coluna)

# plt.title('Evolução Absoluta das Situações por Ano')
# plt.xlabel('Ano Letivo')
# plt.ylabel('Quantidade de Alunos')
# plt.legend()
# plt.tight_layout()
# plt.show()

categorias = ['% Formado', '% Trancado', '% Jubilado', '% Cancelado por abandono', '% Cancelado', '% Abandono']
# Criar a figura e os subplots (2 linhas x 3 colunas)
fig, axs = plt.subplots(2, 3, figsize=(18, 10))  # (altura, largura)

# Flatten os eixos para facilitar o loop
axs = axs.flatten()

# Loop pelas categorias e eixos
for i, coluna in enumerate(categorias):
    axs[i].plot(pivot_df['PERIODO LETIVO'], pivot_df[coluna], marker='o')
    axs[i].set_title(f'Evolução de {coluna}')
    axs[i].set_xlabel('Ano Letivo')
    axs[i].set_ylabel('Percentual (%)')
    axs[i].grid(True)

plt.tight_layout()
plt.suptitle('Evolução Percentual das Situações por Ano (GR13)', fontsize=16, y=1.05)
plt.show()



# pivot_df.plot(
#     x='PERIODO LETIVO',
#     y='Total',
#     kind='bar',
#     figsize=(10, 6),
#     title='Total de Saídas Acadêmicas por Ano'
# )

# plt.ylabel('Total de Alunos')
# plt.tight_layout()
# plt.show()

# Média das proporções ao longo de todos os anos
# media_proporcoes = pivot_df[categorias].mean()

# media_proporcoes.plot(
#     kind='pie',
#     autopct='%1.1f%%',
#     figsize=(8, 8),
#     title='Média Geral das Proporções (2008-2024)'
# )

# plt.ylabel('')
# plt.tight_layout()
# plt.show()
