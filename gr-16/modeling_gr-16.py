import pandas as pd
import matplotlib.pyplot as plt

# ====== 1. Carregar a base de dados ======
df = pd.read_excel("gr-16_demografias.xlsx")

# try:
#     # Tente ler o arquivo
#     df = pd.read_excel("gr-16_demografias.xlsx")
    
#     # Se der certo, mostre as primeiras linhas
#     print("Leitura do arquivo realizada com sucesso!")

# except FileNotFoundError:
#     print("Erro: Arquivo não encontrado. Verifique o nome e o caminho do arquivo.")

# except ImportError as e:
#     print(f"Erro de dependência: {e}. Verifique se o pacote openpyxl está instalado.")

# except Exception as e:
#     print(f"Erro inesperado durante a leitura: {e}")

# ====== 3. Distribuição por Série × Sexo ======
pivot_sexo = pd.pivot_table(
    df,
    index='SERIE',
    columns='SEXO',
    values='IDADE',  # Pode ser qualquer coluna não nula para contar
    aggfunc='count',
    fill_value=0
)

# Gráfico: Barras empilhadas (Série x Sexo)
pivot_sexo.plot(kind='bar', stacked=True)
plt.title('Distribuição por Série e Sexo')
plt.xlabel('Série')
plt.ylabel('Quantidade de Alunos')
plt.legend(title='Sexo')
plt.tight_layout()
plt.show()

# ====== 4. Distribuição por Série × Faixa Etária ======
# pivot_faixa = pd.pivot_table(
#     df_cc,
#     index='Série',
#     columns='Faixa Etária',
#     values='Idade',
#     aggfunc='count',
#     fill_value=0
# )

# # Gráfico: Barras empilhadas (Série x Faixa Etária)
# pivot_faixa.plot(kind='bar', stacked=True)
# plt.title('Distribuição por Série e Faixa Etária')
# plt.xlabel('Série')
# plt.ylabel('Quantidade de Alunos')
# plt.legend(title='Faixa Etária', bbox_to_anchor=(1.05, 1))
# plt.tight_layout()
# plt.show()

# # ====== 5. Evolução histórica (2008–2024) por Sexo ======
# pivot_ano_sexo = pd.pivot_table(
#     df_cc,
#     index='Ano',
#     columns='Sexo',
#     values='Idade',
#     aggfunc='count',
#     fill_value=0
# )

# # Gráfico: Evolução % por sexo ao longo dos anos
# pivot_ano_sexo_pct = pivot_ano_sexo.div(pivot_ano_sexo.sum(axis=1), axis=0) * 100
# pivot_ano_sexo_pct.plot(kind='line', marker='o')
# plt.title('Evolução da Proporção de Alunos por Sexo (2008–2024)')
# plt.xlabel('Ano')
# plt.ylabel('Percentual (%)')
# plt.legend(title='Sexo')
# plt.tight_layout()
# plt.show()

# # ====== 6. Idade média por Série ======
# idade_media = df_cc.groupby('Série')['Idade'].mean().sort_index()

# # Gráfico: Linha com Idade Média por Série
# idade_media.plot(kind='line', marker='o')
# plt.title('Idade Média por Série')
# plt.xlabel('Série')
# plt.ylabel('Idade Média')
# plt.tight_layout()
# plt.show()

# ====== 7. Exportar tabelas de resultados (Opcional) ======
pivot_sexo.to_excel('Resultado_Serie_Sexo.xlsx')
# pivot_faixa.to_excel('Resultado_Serie_FaixaEtaria.xlsx')
# pivot_ano_sexo.to_excel('Resultado_Ano_Sexo.xlsx')
# idade_media.to_frame().to_excel('Resultado_Idade_Media_Serie.xlsx')

print("Análises concluídas com sucesso!")
