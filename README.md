# PREVISÕES DAS VAZÕES FUTURAS DAS USINAS HIDRELÉTRICAS BRASILEIRAS
USANDO O TESTE DE QUI-QUADRADO

Leitura do arquivo com o histórico das vazões das principais usinas hidrelétricas brasileiras, 
administradas pela ONS, com o objetivo de realizar dados estatísticos e prevê as vazões futuras.

## TESTE QUI-QUADRADO DE PEARSON

A hipótese estatística do Qui-quadrado de Pearson é um teste de independência entre variáveis 
categóricas

**A tabela de contingência:**

uma tabela de contingência (também chamada de crosstab) é usada em estatísticas para resumir
a relação entre várias variáveis categórica

## PYTHON
Bibliotecas:
```python
import pandas as pd
import scipy
from scipy.stats import chi2_contingency
```

A função chi2_contingency() do módulo scipy.stats toma como entrada a 
tabela de contingência no formato de array 2d. Ele retorna uma tupla contendo 
estatísticas de teste , o valor p , graus de liberdade e a tabela esperada 
(aquela que criamos a partir dos valores calculados) nessa ordem. 


## REFERÊNCIAS
- [Acervo Lima](https://acervolima.com/python-teste-qui-quadrado-de-pearson/)

Critical values of the Chi-square distribution with d degrees of freedom
