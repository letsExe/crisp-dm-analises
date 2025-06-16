import pandas as pd

# ====== 1. Carregar todas as abas de uma vez ======
caminho_arquivo = r'C:\Users\Leticia\Desktop\Codigos\crisp-dm\gr-14\GR14.xlsx'
xls = pd.ExcelFile(caminho_arquivo)

df_list = []

for aba in xls.sheet_names:
    temp_df = pd.read_excel(caminho_arquivo, sheet_name=aba)
    temp_df['Ano'] = int(aba)  # Adiciona coluna com o ano (pegando do nome da aba)
    df_list.append(temp_df)

# ====== 2. Unificar todas as abas em um único DataFrame ======
df = pd.concat(df_list, ignore_index=True)

# ====== 3. Remover espaços extras nos nomes das colunas ======
df.columns = df.columns.str.strip()

# ====== 4. Padronizar campos de porcentagem (remover % e transformar em float) ======
df['% Aprovados'] = df['% APROVADOS'].astype(str).str.replace('%', '').str.replace(',', '.').astype(float)
df['% Reprovados'] = df['% REPROVADOS'].astype(str).str.replace('%', '').str.replace(',', '.').astype(float)

# ====== 5. Padronizar "Ano Letivo" (Série) se houver variações ======
df['Ano Letivo'] = df['SERIE'].astype(str).str.strip().str.replace('ano', 'º ano', regex=False)

# Exemplo: se quiser forçar correção manual de alguns casos:
# df['Ano Letivo'] = df['Ano Letivo'].replace({'1 ano': '1º ano', '2 ano': '2º ano'})

# ====== 6. Criar coluna de Total de Alunos por Disciplina ======
df['Total Alunos'] = df['REPROVADOS'] + df['APROVADOS']

print(df)


# ====== 7. Exportar o DataFrame limpo para um novo arquivo Excel ======
df.to_excel("GR14_Dados_Limpos.xlsx", index=False)

