import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
caminho_arquivo = r'C:\Users\Leticia\Desktop\Codigos\crisp-dm\gr-14\GR14_Agrupado_Ano_Disciplina.xlsx'
df = pd.read_excel(caminho_arquivo)

df.columns = df.columns.str.upper().str.strip()

st.title("📊 Análise de Reprovação - Ciência da Computação")

# Seletor de Ano
anos = sorted(df['ANO'].unique())
ano_selecionado = st.selectbox("Selecione o Ano:", anos)

# Filtro pelo ano
df_ano = df[df['ANO'] == ano_selecionado]

# Top 3 disciplinas com mais reprovações
st.subheader(f"Top 3 Disciplinas com Mais Reprovações em {ano_selecionado}")
top3 = df_ano.groupby('DICIPLINA', as_index=False)['REPROVADOS'].sum().sort_values(by='REPROVADOS', ascending=False).head(3)
st.dataframe(top3)

# Seletor de disciplina
disciplinas = df_ano['DICIPLINA'].unique()
disciplina_selecionada = st.selectbox("Selecione uma Disciplina para ver a Evolução:", disciplinas)

# Evolução da disciplina ao longo dos anos
df_disciplina = df[df['DICIPLINA'] == disciplina_selecionada]
df_evolucao = df_disciplina.groupby('ANO', as_index=False)['REPROVADOS'].sum()

# Gráfico de linha da evolução
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(df_evolucao['ANO'], df_evolucao['REPROVADOS'], marker='o')
ax.set_title(f'Evolução de Reprovações - {disciplina_selecionada}')
ax.set_xlabel('Ano')
ax.set_ylabel('Total de Reprovações')
st.pyplot(fig)

st.markdown("---")
st.write("Projeto de Iniciação Científica - Análise Descritiva baseada no CRISP-DM Adaptado")
