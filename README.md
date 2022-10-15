# Simulações NEWAVE-DECOMP ENCADEADO

**Período de Comercialização:**
A Copel GeT possuí um período de comercialização que vai até 18 anos a 
frente, com foco nos primeiros 2 anos. O princípio é investigar melhor estes 
primeiros 2 anos através de simulações NEWAVE-DECOMP encadeados.

 Inicialmente será feita simulação iniciando neste final de 2022 e 
terminando em dezembro de 2023.

Por exemplo se iniciado em Setembro/2022, a previsão da Refinitiv vai até 
março de 2023. Para que a simulação encadeada alcance dezembro de 
2023, faz-se necessário estender, de alguma forma, projeção de afluência.

Uma forma simples de fazer essa extensão seria através de Correlação com 
o histórico

## PREVISÕES DAS VAZÕES FUTURAS
Leitura do arquivo com o histórico das vazões das principais usinas hidrelétricas brasileiras,
por submercado, administradas pela ONS,com o objetivo de realizar dados estatísticos e prevê as vazões futuras.

|CÓD.| POSTO | USINA | SUB|
|---| --- |---|---|
|6|6| FURNAS| 1 |
|74|74| GBM | 2|
|169|169| SOBRADINHO | 3|
|275|275 | TUCURUÍ| 4|

## CORRELAÇÃO DE PEARSON

O Coeficiente de Correlação de Pearson também é chamado de "coeficiente de
correlação produto-momento" ou simplesmente de "ρ de Pearson". Segundo Miot (2018), é
um teste estatístico que explora a intensidade e o sentido do comportamento mútuo entre
variáveis. Este coeficiente pode assumir apenas valores entre -1 e 1.

A correlação indica a interdependência entre duas variáveis. O cálculo do
Coeficiente de Correlação de Pearson serve para detectar o grau de correlação entre as
variáveis quando não se é facilmente compreendida sua interdependência.


## PYTHON
Bibliotecas:
```python
import pandas as pd
import numpy as np
from pathlib import Path
from copy import deepcopy
from collections import deque
```


## REFERÊNCIAS

- [Artigo IME sobre a Correlação de Pearson](https://www.marinha.mil.br/spolm/sites/www.marinha.mil.br.spolm/files/DESENVOLVIMENTO%20DE%20UM%20C%C3%93DIGO%20EM%20PYTHON%20PARA%20GERA%C3%87%C3%83O%20DE%20MATRIZES%20DE%20CORRELA%C3%87%C3%83O%20DE%20PEARSON%20COM%20LA%C3%87OS%20A%20PARTIR%20DE%20N%20VARI%C3%81VEIS%20TOMADAS%20DUAS%20A%20DUAS.pdf)


