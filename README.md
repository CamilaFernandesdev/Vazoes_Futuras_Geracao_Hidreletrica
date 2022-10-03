# PREVISÕES DAS VAZÕES FUTURAS DAS USINAS HIDRELÉTRICAS BRASILEIRAS
USANDO O TESTE DE QUI-QUADRADO

Leitura do arquivo com o histórico das vazões das principais usinas hidrelétricas brasileiras, 
administradas pela ONS, com o objetivo de realizar dados estatísticos e prevê as vazões futuras.

## CORRELAÇÃO DE PEARSON

O Coeficiente de Correlação de Pearson também é chamado de "coeficiente de
correlação produto-momento" ou simplesmente de "ρ de Pearson". Segundo Miot (2018), é
um teste estatístico que explora a intensidade e o sentido do comportamento mútuo entre
variáveis. Este coeficiente pode assumir apenas valores entre -1 e 1.

A correlação indica a interdependência entre duas variáveis. O cálculo do
Coeficiente de Correlação de Pearson serve para detectar o grau de correlação entre as
variáveis quando não se é facilmente compreendida sua interdependência.

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
- [Artigo IME sobre a Correlação de Pearson](https://www.marinha.mil.br/spolm/sites/www.marinha.mil.br.spolm/files/DESENVOLVIMENTO%20DE%20UM%20C%C3%93DIGO%20EM%20PYTHON%20PARA%20GERA%C3%87%C3%83O%20DE%20MATRIZES%20DE%20CORRELA%C3%87%C3%83O%20DE%20PEARSON%20COM%20LA%C3%87OS%20A%20PARTIR%20DE%20N%20VARI%C3%81VEIS%20TOMADAS%20DUAS%20A%20DUAS.pdf)

Critical values of the Chi-square distribution with d degrees of freedom
