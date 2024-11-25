# README
## Trabalho

O repositório contém tanto o PDF quanto o .odt original.

Os scripts analisados no trabalho encontram-se em "PCA_Santos.ipynb"

## Dependências

Encontram-se no arquivo "requirements.txt"
Instalados numa .venv ou globalmente por meio de:
`pip install requirements.txt`

## Datasets

Devem ser colocados na pasta *datasets*:
  
    1. Carga – os arquivos de 2018 a 2023;
    2. Carga Conteinerizada – os arquivos de 2018 a 2023;
    3. E também foram utilizados os arquivos de tabelas auxiliares:
        a) Instalação Origem;
        b) Instalação Destino;
        c) Mercadoria;
        d) Mercadoria Conteinerizada1;

Ambos links abaixos contém o mesmo *dataset*. Recomenda-se o da ANTAQ, para poder se baixar apenas os arquivos dos anos relevantes com mais facilidade.
### Links
**ANTAQ**: https://web3.antaq.gov.br/ea/sense/download.html#pt

**Gov.br**: https://dados.gov.br/dados/organizacoes/visualizar/agencia-nacional-de-transportes-aquaviarios

*Datasets* de **Carga de 2018**, **Carga Conteinerizada 2018** e *dataset* intermediário com importações de Santos podem ser encontrados zipados em "datasets/datasets_zip.zip".

## Execução dos scripts

Caso o arquivo "datasets/df_rus_psantos.csv" não esteja na pasta datasets, então pode é necessário rodar o script gerador "etl_inicial.py" - para tal é necessário as tabelas de Carga e Carga Conteinerizada dos anos **2018, 2019, 2020, 2021, 2022 e 2023**.