# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 14:56:21 2022

@author: E805511
"""

import pandas as pd
import numpy as np
from pathlib import Path
import seaborn as sns

#%%
"""
ESTA´TISTICA DESCRITIVA

CORRELAÇÃO DE PEARSON:
    
    Quando uma hipótesede aumento ou queda de uma variável está associado à
    evolução de outra variável, aplica-se o coeficiente de correlação de Pearson
    com o intervalo de -1 a 1. O valor 0 indica que não há correlação entre as 
    duas variáveis
"""
def leitura_vazao(end) -> pd.DataFrame:
    """Leitura do arquivo vazões.dat."""
    tab = pd.read_csv(end, sep='\s+', header = None )
    cab = ['POSTO', 'ANOS', 'JAN','FEV', 'MAR', 'ABR', 
           'MAI','JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ']
    tab.columns = cab
    tab.set_index(['POSTO', 'ANOS'])
    tab.set_index('ANOS')
    return tab
    
end = Path(r'C:\Users\E805511\Downloads\vazoes 2022')
df_end = leitura_vazao(end)

teste_usinas = df_end.groupby("POSTO").get_group(113)


#%% Manipulação dos dados

pivot2 = obs.pivot_table(index = 'ANOS', columns='POSTO')

correlacao = df_end.corr(method='pearson')

#%% MANEIRAS DE ORGANIZAR AS INFORMAÇÃO
#Para separar por período do ano como abr/2022 a mar/2023
#E poder calcular o coeficiente de Pearson com as colunas geradas

# def reshape(inf, sup, data):
#     """Criando a própria função."""
#     return [float(i) for i in data.iloc[inf:sup,:].values]

# pd.DataFrame({'A': reshape(0,10, obs) ,'B': reshape(10,20, obs), 
#               'C': reshape(20,30, obs), 'D': reshape(30,40, obs)}, index = range(10))


# #Refatoração da função acima
# pd.DataFrame(obs.values.reshape(-1, 10).T, columns=['A','B', 'C', 'D'])




#%% PLOT

sns.heatmap(correlacao,
            cmap='ocean',
            annot=True,
            linewidths=0.5)

#Definir x e y
sns.scatterplot(data = obs, x='name1', y='name2')


#%% TESTES CONSERTANDO A LEITURA DO ARQUIVO



#------------------------------------------------------------------------------