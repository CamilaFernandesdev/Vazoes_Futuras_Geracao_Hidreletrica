# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 14:56:21 2022

@author: E805511
"""

import pandas as pd
import numpy as np
from pathlib import Path
import seaborn as sns

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
    tab = pd.read_fwf(end)#(end, header = False )
    cab = ['POSTO', 'ANOS', 'JAN','FEV', 'MAR', 'ABR', 'MAI','JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ']
    tab.columns = cab#['POSTO', 'ANOS', 'JAN','FEV', 'MAR', 'ABR', 'MAI','JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ']
    tab.set_index('POSTO', drop=True, inplace=True)
    return tab
    
end = Path(r'C:\Users\E805511\Downloads\vazoes 2022')
obs = leitura_vazao(end)
correlacao = obs.corr()

#%% PLOT

sns.heatmap(correlacao, annot=True)

#Definir x e y
sns.scatterplot(data = obs, x='name1', y='name2')
