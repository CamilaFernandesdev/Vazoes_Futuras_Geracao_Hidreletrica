
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 14:56:21 2022.

@author: E805511
"""

import pandas as pd
import numpy as np
from pathlib import Path
import seaborn as sns
from copy import deepcopy
from collections import deque

#%%
"""
ESTATÍSTICA DESCRITIVA

CORRELAÇÃO DE PEARSON:
    
    Quando uma hipótese de aumento ou queda de uma variável está associado à
    evolução de outra variável, aplica-se o coeficiente de correlação de Pearson
    com o intervalo de -1 a 1. O valor 0 indica que não há correlação entre as 
    duas variáveis
    
    O coeficiente de correlação de Pearson mede o associação linear entre variáveis. Seu valor pode ser interpretado da seguinte forma:

        +1 - Correlação positiva completa
        +0,8 - Correlação positiva forte
        +0,6 - Correlação positiva moderada
        0 - nenhuma correlação
        -0,6 - Correlação negativa moderada
        -0,8 - Correlação negativa forte
        -1 - Correlação negativa completa
"""


#meses = 'JAN FEV MAR ABR MAI JUN JUL AGO SET OUT NOV DEZ'.split()
meses = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


def leitura_vazao(end) -> pd.DataFrame:
    """Leitura do arquivo vazões.dat."""
    tab = pd.read_csv(end, sep='\s+', header = None )
    cab = ['POSTO', 'ANOS'] + meses
    tab.columns = cab
    tab.set_index(['POSTO'], drop=True, inplace=True)
    return tab
    
end = Path(r'C:\Users\E805511\Downloads\vazoes 2022')
df_end = leitura_vazao(end)

#------------------------------------------------------------------------------

# %% 


def organizando_dados():
    """Digitar depois..."""
    #--------------------------------------------------------------
    selecao1 = ~(df_end.loc[:, 'ANOS'] == 2022).values
    selecao2 = ~(df_end.loc[:, 'ANOS'] == 1931).values
    #--------------------------------------------------------------
    df_end_1 = deepcopy(df_end[selecao1])
    df_end_2 = deepcopy(df_end[selecao2])
    #--------------------------------------------------------------
    df_end_1.rename(columns={'ANOS': 'ANO_INI'}, inplace=True)
    df_end_2.rename(columns={'ANOS': 'ANO_FIM'}, inplace=True)
    #--------------------------------------------------------------
    #Seleciona em qual mês inicia, realocando os meses anteriores
    #No caso, inicia em Abril
    df_end_1.loc[:, 1:3] = df_end_2.loc[:, 1:3]
    
    return df_end_1

def organizando_colunas():
    """Para modificação do nome das colunas relacionada aos meses.
    Seleção da como começam a tabela atráves da biblioteca collections,
    classe deque.
    -------------------
    Exemplo:
    com o rotate=0
    imprime: deque(['JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN',
                    'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ'])
    com rotate= -3
    imprime: deque([4, 5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 3])
    equivalente: deque(['ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET',
                        'OUT', 'NOV', 'DEZ', 'JAN', 'FEV', 'MAR'])
    ------------------
    """
    anos_sel = deque(meses)
    anos_sel.rotate(-3)
    print(anos_sel)
    return anos_sel




#------------------------------------------------------------------------------
#Tabela organizada
anos_sel = organizando_colunas()
dados = organizando_dados()
#------------------------------------------------------------------------------
df_final = dados.loc[:, ['ANO_INI'] + list(anos_sel)]
df_final['ANO_INI'] = df_final['ANO_INI'].astype(str) + '-' + (df_final['ANO_INI'] + 1).astype(str)
#------------------------------------------------------------------------------


#%% SELECIONAR UMA OU MúlTIPLAS USINAS
# Código das maiores usinas de cada submercado de energia
"""Apenas uma usina por enquanto"""
def selecione_usina(cod:int) -> pd.DataFrame:
    """Digite o código da usina."""
    teste_usinas = df_final.groupby("POSTO").get_group(cod)
    return teste_usinas


usina_sel = selecione_usina(1)

# =============================================================================
# %% CÁLCULO FABIANO
# =============================================================================
"""

vazoes = np.random.rand(91, 12) *100
vazao_ref = np.random.rand(1, 12) * 100
corre = np.corrcoef(vazao_ref, vazoes)[1:, 0]
series = [str(ano) + '-' + str(ano+1) for ano in range(1931, 2022)]
ano_escolhido = series[corre.argmax()]

"""
#Organizar em uma função
#pegar a coluna com os anos 

series_anos = usina_sel['ANO_INI']
series_anos.reset_index(drop=True, inplace=True)

usina_sel.set_index('ANO_INI', inplace=True)


#%%
#função é usada para acessar a última linha do dataframe
x = np.array(usina_sel.tail(1))

# correlacao = np.corrcoef(x=x,
#                          rowvar=True) #default)


#for i, y in usina_sel.iterrows():
    # correlacao = np.corrcoef(x=x,y=usina_sel, rowvar=True)
#    print(y)

correlacao = np.corrcoef(x=x, y=usina_sel)[1: -1, 0]

#Ano escolhido
ano_escolhido = series_anos[correlacao.argmax()]

#------------------------------------------------------------------------------
