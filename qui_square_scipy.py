
# -*- coding: utf-8 -*-

"""
Created on Thu Sep 29 13:33:15 2022.
@author: E805511
"""

#from scipy import c
import scipy
from scipy.stats import chi2_contingency
import numpy as np
import pandas as pd
from pathlib import Path

#==============================================================================
#%% Chi-square test of independence of variables in a contingency table
#==============================================================================

#obs = #numpy array


#%%

#Baseado no leitor Newave - Fabiano
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
df_vazoes = leitura_vazao(end)

teste_usinas = df_vazoes.groupby("POSTO").get_group(113)


chi2, p, dof, ex = chi2_contingency(df_vazoes, correction=True, lambda_= None)

vetor = df_vazoes.to_numpy()
vetor2 = df_vazoes['ANOS'].values

#%%

    
end = Path(r'C:\Users\E805511\Downloads\vazoes 2022')
with open(end) as arquivo:
    arq = arquivo.readlines()

# arq.insert(0,object:_T)
df_vazoes = pd.DataFrame(arq)
#%%
correlacao2 = df_vazoes.corrwith(other=df_vazoes)
#---------------------------------------------------------------
# DADOS:
#   chi2: float (The test statistic)
#   p : float (The p-value of the test)
#   dof : int (Degrees of freedom)
#   expected : ndarray, same shape as observed (The expected frequencies, based
                                            # on the marginal sums of the table.)
#--------------------------------------------------------------
dof = df_vazoes.size - sum(df_vazoes.shape) + df_vazoes.ndim - 1

chi2, p, dof, ex = chi2_contingency(df_vazoes, correction=False, lambda_= None)

#The number of degrees of freedom

