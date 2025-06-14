import pandas as pd
import os
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

# Carregar a tabela gerada na preparação
caminho_arquivo =  os.getenv('caminho_gr13')
df = pd.read_excel(caminho_arquivo)

# 2. Pivotar a tabela
pivot_df = df.pivot_table(
    index='PERIODO LETIVO', 
    columns='SITUACAO', 
    values='QUANTIDADE', 
    aggfunc='sum', 
    fill_value=0
)

# 3. Garantir que todas as categorias existam como colunas
for col in ['Formado', 'trancado', 'jubilado', 'Cancelado por abandono', 'Cancelado', 'abandono']:
    if col not in pivot_df.columns:
        pivot_df[col] = 0

# 4. Calcular o total e as proporções
pivot_df['Total'] = (
    pivot_df['Formado'] +
    pivot_df['trancado'] +
    pivot_df['jubilado'] +
    pivot_df['Cancelado por abandono'] +
    pivot_df['Cancelado'] +
    pivot_df['abandono']
)

# 5. Calcular as proporções (%)
pivot_df['% Formado'] = (pivot_df['Formado'] / pivot_df['Total']) * 100
pivot_df['% Trancado'] = (pivot_df['trancado'] / pivot_df['Total']) * 100
pivot_df['% Jubilado'] = (pivot_df['jubilado'] / pivot_df['Total']) * 100
pivot_df['% Cancelado por abandono'] = (pivot_df['Cancelado por abandono'] / pivot_df['Total']) * 100
pivot_df['% Cancelado'] = (pivot_df['Cancelado'] / pivot_df['Total']) * 100
pivot_df['% Abandono'] = (pivot_df['abandono'] / pivot_df['Total']) * 100

# 7. Resetar o index para que o PERIODO LETIVO vire uma coluna normal
pivot_df = pivot_df.reset_index()

# 8. Verificar as colunas finais
#print("Colunas finais no DataFrame:", pivot_df.columns)
print(pivot_df)

# 9. Exportar para Excel SEM o índice extra
pivot_df.to_excel('saida_tabela_GR13.xlsx', index=False)
