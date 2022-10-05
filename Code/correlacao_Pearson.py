
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 14:56:21 2022.

@author: E805511
"""

import pandas as pd
import numpy as np
from pathlib import Path
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
MESES = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


def leitura_vazao(end) -> pd.DataFrame:
    """Leitura do arquivo vazões.dat."""
    tab = pd.read_csv(end, sep='\s+', header = None )
    cab = ['POSTO', 'ANOS'] + MESES
    tab.columns = cab
    tab.set_index(['POSTO'], drop=True, inplace=True)
    return tab
    
caminho = Path(r'C:\Users\E805511\Downloads\vazoes 2022')
df_vazao_original = leitura_vazao(caminho)

#------------------------------------------------------------------------------

# %% 


def organizando_dados():
    """Digitar depois..."""
    #--------------------------------------------------------------
    selecao1 = ~(df_vazao_original.loc[:, 'ANOS'] == 2022).values
    selecao2 = ~(df_vazao_original.loc[:, 'ANOS'] == 1931).values
    #--------------------------------------------------------------
    df_end_1 = deepcopy(df_vazao_original[selecao1])
    df_end_2 = deepcopy(df_vazao_original[selecao2])
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
    anos_sel = deque(MESES)
    anos_sel.rotate(-3)
    print(anos_sel)
    return anos_sel



def tabela_auxiliar(): 
    """Digitar depois."""
    #------------------------------------------------------------------------------
    #Tabela organizada
    anos_sel = organizando_colunas()
    dados = organizando_dados()
    #------------------------------------------------------------------------------
    df_final = dados.loc[:, ['ANO_INI'] + list(anos_sel)]
    df_final['ANO_INI'] = df_final['ANO_INI'].astype(str) + '-' + (df_final['ANO_INI'] + 1).astype(str)
    #------------------------------------------------------------------------------
    return df_final
    

tabela_aux = tabela_auxiliar()
#%% SELECIONAR UMA OU MúlTIPLAS USINAS
# Código das maiores usinas de cada submercado de energia
"""Apenas uma usina por enquanto"""
def selecione_usina(cod:int) -> pd.DataFrame:
    """Digite o código da usina."""
    teste_usinas = tabela_aux.groupby("POSTO").get_group(cod)
    if cod == 6:
        print('FURNAS')
    elif cod == 74:
        print('GBM')
    elif cod == 169:
        print('TUCURUÍ')
    elif cod == 275:
        print('SOBRADINHO')
    else:
        print('Escolha entre as usinas cod:[6, 74, 169, 275]')
    
    return teste_usinas


usina_sel = selecione_usina(74)

# =============================================================================
# %% CÁLCULO FABIANO
# =============================================================================

def periodo_correlacao():
    """Escrever depois."""
    #-----------------------------------------------------------
    #Seleção da coluna com os anos da tabela auxiliar
    series_anos = usina_sel['ANO_INI']
    series_anos.reset_index(drop=True, inplace=True)
    #-----------------------------------------------------------
    usina_sel.set_index('ANO_INI', inplace=True)
    #-----------------------------------------------------------
    
    return series_anos

series_anos = periodo_correlacao()

    
def calculo_correlacao():
    """Milhões de coisa em uma função.
    imprime: período da correlação: 2018-2019
    """
    #--------------------------------------------------------------------------
    #função é usada para acessar a última linha do dataframe
    x = np.array(usina_sel.tail(1))
    #--------------------------------------------------------------------------
    #Cálculo correlação
    correlacao = np.corrcoef(x=x, y=usina_sel)[1: -1, 0]
    #--------------------------------------------------------------------------
   
    
    return correlacao


resultado_correlacao = calculo_correlacao()
#%% Preenchimento

# Preenchimento
ano_preenchimento = series_anos[resultado_correlacao.argmax()+1]
#--------------------------------------------------------------------------

ano_escolhido = series_anos[resultado_correlacao.argmax()]
#--------------------------------------------------------------------------

print(f'período da correlação: {ano_escolhido}')


teste = tabela_aux.groupby("ANO_INI").get_group(ano_preenchimento)




#%% Escrever no arquivo txt

# with open(file = end, encoding='utf-8') as arquivo:
#     vazoes_novo = arquivo.readline()


