'''
Lista de exercicio - Treinando Pandas (Básico)
Autor: Rodrigo Asafh
Data: 17/02/2024

Lisence: MIT
'''

# imports
import pandas as pd

def divide_exercicios(n):
    print(190 * '-')
    print(f'\nExercicio-> {n}')

def mostra_resultado(result):
    print(result)

df_padrao = pd.read_csv('dsa_manipulacao_dados_pandas/res/dataset.csv')

# Execício 1 
divide_exercicios(1)
moda = df_padrao['Quantidade'].mode()[0] #Zero a primeira ocorrencia que mais se repete.
df_padrao['Quantidade'] = df_padrao['Quantidade'].fillna(moda)
mostra_resultado(df_padrao.isna().sum())

# Exercicio 2
divide_exercicios(2)
df_valores_diversos = df_padrao[df_padrao['Quantidade'].isin([5, 7, 9, 11])]
mostra_resultado(df_valores_diversos)

# Exercicio 3
divide_exercicios(3)
mostra_resultado(df_valores_diversos.query('300 < Valor_Venda < 1000'))
mostra_resultado(df_valores_diversos.Valor_Venda.describe().astype(int)) # para resolver o exercicio 5

# Exercicio 4
divide_exercicios(4)
mostra_resultado(df_valores_diversos[:10])

# Exercicio 5
divide_exercicios(5)
mostra_resultado(df_valores_diversos.query('Valor_Venda > 375'))

# Exercicio 6
divide_exercicios(6)
print('A:\n') 
mostra_resultado(df_padrao[(df_padrao.Segmento == 'Consumer') & (df_padrao.Regiao == 'West')].head())
print('\nB:')
mostra_resultado(df_padrao[(df_padrao.Segmento == 'Consumer') | (df_padrao.Regiao == 'West')].tail())
print('\nC:')
mostra_resultado(df_padrao[(df_padrao.Segmento != 'Consumer') & (df_padrao.Regiao != 'West')].sample(5))