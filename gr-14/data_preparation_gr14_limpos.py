import pandas as pd

# ====== 1. Carregar o arquivo já limpo da etapa anterior ======
caminho_arquivo = r'C:\Users\Leticia\Desktop\Codigos\crisp-dm\gr-14\GR14_Dados_Limpos.xlsx'
df = pd.read_excel(caminho_arquivo)

#print(df.columns.tolist())


df_agrupado_ano_disciplina = df.groupby(['ANO', 'SERIE', 'DICIPLINA'], as_index=False).agg({
    'REPROVADOS': 'sum',
    'APROVADOS': 'sum',
    'TOTAL ALUNOS': 'sum'
})

# 5. Recalcular as porcentagens
df_agrupado_ano_disciplina['% REPROVADOS'] = (df_agrupado_ano_disciplina['REPROVADOS'] / df_agrupado_ano_disciplina['TOTAL ALUNOS']) * 100
df_agrupado_ano_disciplina['% APROVADOS'] = (df_agrupado_ano_disciplina['APROVADOS'] / df_agrupado_ano_disciplina['TOTAL ALUNOS']) * 100

# 6. Salvar o resultado
df_agrupado_ano_disciplina.to_excel("GR14_Agrupado_Ano_Disciplina.xlsx", index=False)

print(df_agrupado_ano_disciplina)