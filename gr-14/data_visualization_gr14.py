import pandas as pd
import matplotlib.pyplot as plt

# Carregar a base agrupada por Ano + Série + Disciplina
caminho_arquivo = r'C:\Users\Leticia\Desktop\Codigos\crisp-dm\gr-14\GR14_Agrupado_Ano_Disciplina.xlsx'
df = pd.read_excel(caminho_arquivo)

# # 2. Mostrar todas as disciplinas únicas
# disciplinas_unicas = df['DICIPLINA'].unique()
# print("\n=== Lista de Disciplinas Disponíveis ===")
# for i, d in enumerate(disciplinas_unicas):
#     print(f"{i+1}. {d}")

# # 3. Entrada do usuário
# print("\nDigite exatamente o nome da disciplina que deseja analisar (copie da lista acima se quiser):")
# disciplina = input("Disciplina: ").strip()

# # 4. Filtrar a disciplina
# df_disciplina = df[df['DICIPLINA'].str.lower() == disciplina.lower()]

# if df_disciplina.empty:
#     print("\nDisciplina não encontrada. Verifique o nome digitado.")
# else:
#     # 5. Agrupar por ano
#     df_evolucao = df_disciplina.groupby('ANO', as_index=False).agg({
#         'REPROVADOS': 'sum',
#         'APROVADOS': 'sum',
#         'TOTAL ALUNOS': 'sum'
#     })
#     df_evolucao['% REPROVADOS'] = (df_evolucao['REPROVADOS'] / df_evolucao['TOTAL ALUNOS']) * 100

#     # 6. Plotar
#     plt.figure(figsize=(8,5))
#     plt.plot(df_evolucao['ANO'], df_evolucao['% REPROVADOS'], marker='o')
#     plt.title(f'Evolução da Reprovação - {disciplina}')
#     plt.xlabel('Ano')
#     plt.ylabel('% de Reprovação')
#     plt.grid(True)
#     plt.tight_layout()
#     plt.show()
##################################################################################################################

# 2. Mostrar anos disponíveis
anos_disponiveis = df['ANO'].unique()
anos_disponiveis.sort()
print("\n=== Anos disponíveis na base ===")
print(anos_disponiveis)

# 3. Entrada do usuário
ano_escolhido = input("\nDigite o ano que deseja analisar: ").strip()

# Validação básica
try:
    ano_escolhido = int(ano_escolhido)
except ValueError:
    print("\nAno inválido. Digite um número como 2015, 2020, etc.")
    exit()

# 4. Filtrar os dados pelo ano escolhido
df_ano = df[df['ANO'] == ano_escolhido]

if df_ano.empty:
    print(f"\nNão há dados para o ano {ano_escolhido}.")
else:
    # 5. Agrupar por disciplina e somar reprovações
    df_top3 = df_ano.groupby('DICIPLINA', as_index=False).agg({
        'REPROVADOS': 'sum'
    }).sort_values(by='REPROVADOS', ascending=False).head(3)

    print(f"\nTop 3 disciplinas com mais reprovações em {ano_escolhido}:\n")
    print(df_top3)

    # 6. Gráfico de barras
    plt.figure(figsize=(8,5))
    plt.barh(df_top3['DICIPLINA'], df_top3['REPROVADOS'], color='red')
    plt.xlabel('Quantidade de Reprovações')
    plt.title(f'Top 3 Disciplinas com Mais Reprovações - {ano_escolhido}')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()