import pandas as pd
import matplotlib.pyplot as plt

# ====== 1. Carregar a base de dados ======
caminho_arquivo = r'C:\Users\Leticia\Desktop\Codigos\crisp-dm\gr-16\gr-16_demografias.xlsx'
abas = pd.read_excel(caminho_arquivo, sheet_name=None)

# Lista para armazenar os dataframes de cada ano
lista_df = []

# Loop para processar cada aba
for nome_aba, df in abas.items():
    # Ignorar abas que não sejam anos (caso existam)
    try:
        ano = int(nome_aba)
    except ValueError:
        continue

    # Adicionar coluna com o ano de referência
    df['ANO_REFERENCIA'] = ano

    # Remover espaços extras nas colunas de texto
    colunas_texto = ['CURSO', 'FAIXA ETARIA', 'SEXO', 'COR/RAÇA']
    for coluna in colunas_texto:
        if coluna in df.columns:
            df[coluna] = df[coluna].astype(str).str.strip()

    # Adicionar à lista
    lista_df.append(df)

# Concatenar todos os anos em um único dataframe
df_final = pd.concat(lista_df, ignore_index=True)

# --- Limpeza de categorias inconsistentes (exemplos - ajuste conforme necessário) ---
# Padronizar valores de SEXO
df_final['SEXO'] = df_final['SEXO'].replace({
    'Feminino': 'F',
    'Masculino': 'M',
    'f': 'F',
    'm': 'M'
})

# Padronizar valores de COR/RAÇA
if 'COR/RAÇA' in df_final.columns:
    df_final['COR/RAÇA'] = df_final['COR/RAÇA'].replace({
        'Branco': 'Branca',
        'Preto': 'Preta',
        'pardo': 'Parda',
        'preta': 'Preta'
        # Adicione outras correções se houver
    })
else:
    print("\nAtenção: Coluna 'COR/RAÇA' não encontrada no dataframe. Pulando padronização de raça/cor.")

# --- Criar coluna de situação aproximada ---
def classificar_situacao(serie):
    if serie == 4:
        return 'Possível Concluinte'
    else:
        return 'Em Andamento'

df_final['Situacao_Aproximada'] = df_final['SERIE'].apply(classificar_situacao)

# --- Criar faixa etária personalizada (exemplo opcional) ---
def faixa_personalizada(idade):
    if idade < 25:
        return '<25'
    elif idade <= 30:
        return '25-30'
    else:
        return '30+'


# ====== 7. Exportar o DataFrame limpo para um novo arquivo Excel ======
df_final.to_excel("GR16_Dados_Limpos.xlsx", index=False)

# --- Visualização inicial ---
print(df_final.head())