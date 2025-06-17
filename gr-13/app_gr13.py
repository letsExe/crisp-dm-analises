import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Lê os dados já preparados
caminho_arquivo = r'C:\Users\Leticia\Desktop\Codigos\crisp-dm\gr-13\saida_tabela_GR13.xlsx'
pivot_df = pd.read_excel(caminho_arquivo)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ====== Título geral ======
st.title('📊 Análise da Situação Acadêmica (GR-13)')

# ====== Exibir a tabela ======
st.header('📋 Tabela Final com Totais e Proporções')
st.dataframe(pivot_df)

# ====== Gráfico de Evolução das Categorias Absolutas ======
st.header('📈 Evolução Absoluta das Situações')

fig, ax = plt.subplots(figsize=(10, 6))
for coluna in ['Formado', 'trancado', 'jubilado', 'Cancelado por abandono', 'Cancelado', 'abandono']:
    if coluna in pivot_df.columns:
        ax.plot(pivot_df['PERIODO LETIVO'], pivot_df[coluna], marker='o', label=coluna)

ax.legend()
ax.set_xlabel('Ano Letivo')
ax.set_ylabel('Quantidade de Alunos')
ax.set_title('Evolução Absoluta das Situações por Ano')
plt.tight_layout()
st.pyplot(fig)

# ====== Heatmap de Proporções (Gráficos de Linha) ======
st.header('🌡️ Evolução Percentual das Situações')

categorias = ['% Formado', '% Trancado', '% Jubilado', '% Cancelado por abandono', '% Cancelado', '% Abandono']

fig, axs = plt.subplots(2, 3, figsize=(18, 10))
axs = axs.flatten()

for i, coluna in enumerate(categorias):
    if coluna in pivot_df.columns:
        axs[i].plot(pivot_df['PERIODO LETIVO'], pivot_df[coluna], marker='o')
        axs[i].set_title(f'Evolução de {coluna}')
        axs[i].set_xlabel('Ano Letivo')
        axs[i].set_ylabel('Percentual (%)')
        axs[i].grid(True)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
fig.suptitle('Evolução Percentual das Situações por Ano (GR-13)', fontsize=16)
st.pyplot(fig)

#streamlit run app_gr13.py
