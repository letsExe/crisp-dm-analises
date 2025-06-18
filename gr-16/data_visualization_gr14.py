import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ====== 1. Carregar a base de dados ======
caminho_arquivo = r'C:\Users\Leticia\Desktop\Codigos\crisp-dm\gr-16\GR16_Dados_Limpos.xlsx'
df_final = pd.read_excel(caminho_arquivo)

# # Exibir anos disponíveis
# anos_disponiveis = sorted(df_final['ANO_REFERENCIA'].unique())
# print("Anos disponíveis:", anos_disponiveis)

# # ===== Escolher o ano manualmente =====
ano_selecionado = 2020  # <<--- Troque aqui pelo ano que quiser analisar

# Filtrar o dataframe
df_ano = df_final[df_final['ANO_REFERENCIA'] == ano_selecionado]

# Contagem por gênero
genero_counts = df_ano['SEXO'].value_counts()

# Plotar o gráfico
plt.figure(figsize=(6, 4))
genero_counts.plot(kind='bar', color=['blue', 'pink'])
plt.title(f'Distribuição Geral por Gênero - Ano {ano_selecionado}')
plt.xlabel('Sexo')
plt.ylabel('Número de Acadêmicos')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

#-----------------------------------------------------------------
# ===== Escolha manual do ano =====
# ano_selecionado = 2020  # <<--- Troque para o ano desejado

# # Filtrar o DataFrame pelo ano escolhido
# df_ano = df_final[df_final['ANO_REFERENCIA'] == ano_selecionado]

# =============================
# 1) Distribuição por Faixa Etária
# =============================
# faixa_counts = df_ano['FAIXA ETARIA'].value_counts().sort_index()

# plt.figure(figsize=(8, 4))
# faixa_counts.plot(kind='bar')
# plt.title(f'Distribuição por Faixa Etária - Ano {ano_selecionado}')
# plt.xlabel('Faixa Etária')
# plt.ylabel('Número de Acadêmicos')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# =============================
# 2) Distribuição de Gênero por Série
# =============================
# serie_sexo = pd.crosstab(df_ano['SERIE'], df_ano['SEXO'])
# print("\nTabela Série x Sexo:")
# print(serie_sexo)

# serie_sexo.plot(kind='bar', stacked=True, figsize=(8, 5), color=['blue', 'pink'])
# plt.title(f'Distribuição de Gênero por Série - Ano {ano_selecionado}')
# plt.xlabel('Série')
# plt.ylabel('Número de Acadêmicos')
# plt.legend(title='Sexo')
# plt.tight_layout()
# plt.show()

# # =============================
# # 3) Distribuição de Faixa Etária por Série
# # =============================
# serie_faixa = pd.crosstab(df_ano['SERIE'], df_ano['FAIXA ETARIA'])
# print("\nTabela Série x Faixa Etária:")
# print(serie_faixa)

# serie_faixa.plot(kind='bar', stacked=True, figsize=(10, 6))
# plt.title(f'Distribuição de Faixa Etária por Série - Ano {ano_selecionado}')
# plt.xlabel('Série')
# plt.ylabel('Número de Acadêmicos')
# plt.legend(title='Faixa Etária', bbox_to_anchor=(1.05, 1))
# plt.tight_layout()
# plt.show()

# #################################################################################
# plt.figure(figsize=(8, 6))
# sns.boxplot(x='SERIE', y='IDADE', data=df_final)
# plt.title('Distribuição das Idades por Série (Boxplot)')
# plt.xlabel('Série')
# plt.ylabel('Idade')
# plt.tight_layout()
# plt.show()