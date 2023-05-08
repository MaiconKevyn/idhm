# IDHM Municípios
## Parte 1 - Manipulação
Este projeto tem como objetivo calcular e analisar o IDHM (Índice de Desenvolvimento Humano Municipal) dos municípios brasileiros, utilizando dados de 2010. O IDHM é um indicador que avalia a qualidade de vida dos municípios com base em três aspectos: renda, saúde e educação. O índice é calculado a partir da média aritmética simples dos índices IDHM-E (educação), IDHM-L (longevidade ou saúde) e IDHM-R (renda). Ele permite ao usuário filtrar os municípios por um valor mínimo de habitantes e exibe as 20 principais cidades em diferentes categorias de IDHM.

Os dados utilizados neste projeto estão disponíveis no kaggle.com, que contém informações referentes ao ano de 2010 de cada município brasileiro.


### Fórmulas utilizadas

<img src="https://user-images.githubusercontent.com/101146083/236711198-50d878dc-1a46-435a-b9db-7589c41fb570.png" alt="Imagem IDHM" width="350"/>

Onde espvida é a expectativa de vida e rdpc é a renda per capita. Equações retiradas do site http://www.dhnet.org.br/

Ao executar o programa, o usuário será solicitado a fornecer um valor mínimo de habitantes que o município deve ter para ser considerado na análise. Isso permite filtrar os municípios com base no tamanho da população, focando apenas nos que atendem ao critério estabelecido pelo usuário.

Após inserir o valor mínimo de habitantes, o programa processará os dados e exibirá as seguintes informações, considerando apenas os municípios com uma população igual ou superior ao limite estabelecido:

+ Top 20 municípios com maior IDHM
+ Top 20 municípios com menor IDHM
+ Top 20 municípios com maior IDHM-L
+ Top 20 municípios com menor IDHM-R

Exemplo do formato do output para um input de 30000:

<img src="https://user-images.githubusercontent.com/101146083/236715009-52211d7c-657f-4f38-b798-af8b457d7c5c.png" alt="Imagem IDHM" width="450"/> 


## Parte 2 - Visualização
Na segunda parte do projeto, nosso objetivo é criar gráficos de barras para visualizar os dados do IDHM dos municípios brasileiros, a fim de facilitar a análise e compreensão das informações.

Ao criar gráficos de barras, vamos explorar os três aspectos do IDHM: renda, saúde e educação, representados pelos índices IDHM-R, IDHM-L e IDHM-E, respectivamente. Isso nos permitirá visualizar a distribuição desses índices em diferentes municípios e identificar padrões, desigualdades e áreas que necessitam de melhorias

Além disso, também criaremos um gráfico de barras para o índice geral do IDHM, que combina os três aspectos mencionados acima. Isso nos dará uma visão geral da qualidade de vida nos municípios brasileiros.

Ao executar o programa, o usuário será apresentado a duas opções para visualizar os dados do IDHM:

**1 - Ranking por estados:** Esta opção exibe um gráfico de barras que mostra o ranking dos municípios dentro de um estado específico, com base no IDHM. Os municípios são ordenados do maior para o menor IDHM, destacando as áreas com melhor qualidade de vida e aquelas que requerem atenção e melhorias.

Por exemplo, ao selecionar esta opção e escolher o estado do Rio Grande do Sul (RS), o programa irá gerar um gráfico de barras que apresenta o ranking dos municípios gaúchos de acordo com o IDHM. Isso permite aos usuários identificar facilmente os municípios com os melhores e piores índices de desenvolvimento humano no estado.


No gráfico de ranking por estados, por exemplo, para o estado do Rio Grande do Sul (RS), obtemos o seguinte gráfico:

<img src="https://user-images.githubusercontent.com/101146083/236712846-924a3a01-8ef9-4712-a38e-85c89706cd38.png" alt="Imagem IDHM" width="600"/>


**2 - Informações de um estado ao longo dos anos:** Esta opção exibe um gráfico de barras que mostra a evolução de um estado específico ao longo de diferentes anos (1991, 2000, 2010). O gráfico permite analisar as tendências e mudanças no IDHM do estado, oferecendo insights sobre o progresso ou declínio na qualidade de vida ao longo do tempo.

Ao selecionar esta opção e escolher um estado, o programa irá gerar um gráfico de barras que apresenta a evolução do IDHM do estado ao longo dos anos disponíveis nos dados. Isso facilita a compreensão das mudanças na qualidade de vida no estado e pode ser útil para identificar períodos de melhoria ou estagnação no desenvolvimento humano.

<img src="https://user-images.githubusercontent.com/101146083/236713729-c7fd2289-b3de-4681-89c7-a90870f015f5.png" alt="Imagem IDHM" width="600"/>


