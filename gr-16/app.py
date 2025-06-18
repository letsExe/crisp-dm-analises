import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ===== 1. Carregar os dados =====
df_final = pd.read_excel('GR16_Dados_Limpos.xlsx')

# ===== 2. Título da aplicação =====
st.title('📊 Perfil Demográfico dos Acadêmicos - GR-16')

# ===== 3. Filtro de Ano =====
anos_disponiveis = sorted(df_final['ANO_REFERENCIA'].unique())
ano_selecionado = st.selectbox('Selecione o Ano:', anos_disponiveis)

# Filtrar o dataframe pelo ano
df_ano = df_final[df_final['ANO_REFERENCIA'] == ano_selecionado]

st.markdown(f"### 📅 Ano selecionado: {ano_selecionado}")

# ===== 4. Distribuição por Gênero =====
st.header('Distribuição Geral por Gênero')
genero_counts = df_ano['SEXO'].value_counts()

fig1, ax1 = plt.subplots(figsize=(6, 4))
genero_counts.plot(kind='bar', color=['blue', 'pink'], ax=ax1)
ax1.set_xlabel('Sexo')
ax1.set_ylabel('Número de Acadêmicos')
ax1.set_title('Distribuição por Gênero')
st.pyplot(fig1)

# ===== 5. Distribuição por Faixa Etária =====
st.header('Distribuição Geral por Faixa Etária')
faixa_counts = df_ano['FAIXA ETARIA'].value_counts().sort_index()

fig2, ax2 = plt.subplots(figsize=(8, 4))
faixa_counts.plot(kind='bar', ax=ax2)
ax2.set_xlabel('Faixa Etária')
ax2.set_ylabel('Número de Acadêmicos')
ax2.set_title('Distribuição por Faixa Etária')
st.pyplot(fig2)

# ===== 6. Distribuição de Gênero por Série =====
st.header('Distribuição de Gênero por Série')
serie_sexo = pd.crosstab(df_ano['SERIE'], df_ano['SEXO'])

fig3, ax3 = plt.subplots(figsize=(8, 5))
serie_sexo.plot(kind='bar', stacked=True, color=['blue', 'pink'], ax=ax3)
ax3.set_xlabel('Série')
ax3.set_ylabel('Número de Acadêmicos')
ax3.set_title('Distribuição de Gênero por Série')
st.pyplot(fig3)

# ===== 7. Distribuição de Faixa Etária por Série =====
st.header('Distribuição de Faixa Etária por Série')
serie_faixa = pd.crosstab(df_ano['SERIE'], df_ano['FAIXA ETARIA'])

fig4, ax4 = plt.subplots(figsize=(10, 6))
serie_faixa.plot(kind='bar', stacked=True, ax=ax4)
ax4.set_xlabel('Série')
ax4.set_ylabel('Número de Acadêmicos')
ax4.set_title('Distribuição de Faixa Etária por Série')
st.pyplot(fig4)

# ===== 8. Informação sobre os dados =====
st.markdown("---")
st.caption('Fonte: Relatório Institucional GR-16 | Análise por Ciência da Computação - Campus X')
