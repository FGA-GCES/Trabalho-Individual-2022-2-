# Trabalho individual de GCES 2022-2


Os conhecimentos de Gestão de Configuração de Software são fundamentais no ciclo de vida de um produto de software. As técnicas para a gestão vão desde o controle de versão, automação de build e de configuração de ambiente, testes automatizados, isolamento do ambiente até o deploy do sistema. Todo este ciclo nos dias de hoje são integrados em um pipeline de DevOps com as etapas de Integração Contínua (CI) e Deploy Contínuo (CD) implementadas e automatizada.

Para exercitar estes conhecimentos, neste trabalho, você deverá aplicar os conceitos estudados ao longo da disciplina no produto de software contido neste repositório.

O sistema se trata de uma biblioteca python para executar pipelines de dados de forma customizável em bancos de dados.

Para executar a aplicação em sua máquina, basta seguir o passo-a-passo descritos abaixo.

# Resumo da aplicação 

 A biblioteca desenvolvida auxilia desenvolvedores a explorar os dados com funções essenciais para a identificação de outliers e anomalias e uma interface que auxilia a visualizar as informações de acordo com o arquivo de configuração.

 A biblioteca recebe um arquivo yaml com as configurações de cada etapa do pipeline de dados, e do endereço do banco de dados.
 Após a execução do banco de dados, o banco de dados de dados é atualizado com os resultados da análise e os resultados podem ser visualizados por meio de dashboards no metabase.

 # Etapas do Trabalho

 O trabalho deve ser elaborado através de etapas. Cada uma das etapas deve ser realizada em um commit separado com o resultado funcional desta etapa.

As etapas de 1 a 3 são relacionadas ao isolamento do ambiente utilizando a ferramenta Docker e Docker Compose. Neste sentido o tutorial abaixo cobre os conceitos fundamentais para o uso destas tecnologias.

[Tutorial de Docker](https://github.com/FGA-GCES/Workshop-Docker-Entrega-01/tree/main/tutorial_docker)

As etapas de 4 e 5 são relacionadas à configuração do pipeline de CI e CD.

[Tutorial CI - Gitlab](https://github.com/FGA-GCES/Workshop-CI-Entrega-02/tree/main/gitlab-ci_tutorial)


## Containerização do Banco


A versão inicial do sistema contém o metabase no backend cujo funcionamento requer uma instalação de um banco de dados Mongo. A primeira etapa do trabalho é de configurar um container somente para o banco de dados com as credenciais especificadas na descrição da aplicação e testar o funcionamento do mesmo.

## Containerização da aplicação + metabase

Nesta etapa, tanto o a aplicação python quanto o metabase/banco deverão estar funcionando em containers individuais.

Deverá ser utilizado um orquestrador (Docker Compose) para gerenciar comunicação entre os containers além do uso de credenciais, networks, volumes, entre outras configurações necessárias para a correta execução da aplicação.

## Gestão de dependencias e pacotes python

Configurar o gerenciador de dependencias e pacotes python, o poetry, para gerar um pacote pip da solução. Publicar a biblioteca

https://python-poetry.org

## Documentação automatizada

Gerar a documentação da biblioteca de forma automatizada utilizando o doxygen para gerar informacoes da biblioteca e o sphinx para criar documentação https://www.sphinx-doc.org



##  Integração Contínua (CI)

Para a realização desta etapa, a aplicação já deverá ter seu ambiente completamente containerizado.

Deverá ser utilizada uma ferramenta de Integração Contínua para garantir o build, os testes e o deploy para o https://pypi.org .

Esta etapa do trabalho poderá ser realizada utilizado os ambientes de CI do GitLab-CI ou Github Actions.

Requisitos da configuração da Integração Contínua (Gitlab ou Github) incluem:

Build (Poetry)
Test - unitários
Lint - 
Documentação (sphinx)


## Avaliação

A avaliação do trabalho será feita à partir da correta implementação de cada etapa. A avaliação será feita de maneira **quantitativa** (se foi realizado a implementação + documentação), e **qualitativa** (como foi implementado, entendimento dos conceitos na prática, complexidade da solução). Para isso, faça os **commits atômicos, bem documentados, completos** a fim de facilitar o entendimento e avaliação do seu trabalho. Lembrando o trabalho é individual.

**Observações**: 
1. A data final de entrega do trabalho é o dia 28/01/2023;
2. O trabalho deve ser desenvolvido em um **repositório PESSOAL e PRIVADO** que deverá ser tornado público somente após a data de entrega do trabalho (no dia 28/01/2023);
3. Cada etapa do trabalho deverá ser entregue em commits progressivos (pendendo ser mais de um commit por etapa);
4. Os **commits devem estar espaçados em dias ao longo do desenvolvimento do trabalho**. Commits feitos todos juntos na data de entrega não serão descontados da nota final.

| Item | Peso |
|---|---|
| 1. Containerização do Banco                      | 1.0 |
| 2. Containerização da biblioteca + Banco          | 1.5 |
| 3. Publicação da biblioteca  | 1.5 |
| 4. Documentação automatiza | 1.5 |
| 5. Integração Contínua (Build, Test, Lint, documentacao)       | 3.0 |
| 6. Deploy Contínuo                               | 1.5 |


##  Exemplo de Trabalhos Anteriores

Alguns trabalhos de trabalhos anteriores:

- [2020/2](https://github.com/FGA-GCES/Trabalho-Individual-2020-2)
- [2021/1](https://github.com/FGA-GCES/Workshop-Docker-Entrega-01)
- [2021/2](https://github.com/FGA-GCES/Trabalho-Individual-2021-2)



### Requisitos de instação

```
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### Rodando a aplicação

```
python src/main.py
```

### Testando

```
pytest --cov
```

### Metabase

O metabase ajuda a visualizar e a modelar o processamento dos dados, a engenharia de features e monitoramento do modelo.



| Keywords  | Descrição |
|-----------|-------------|
|   CSV     | Um arquivo CSV é um arquivo de texto simples que armazena informações de tabelas e planilhas. Os arquivos CSV podem ser facilmente importados e exportados usando programas que armazenam dados em tabelas.|
| Collection (coleção)| Uma coleção é um agrupamento de documentos do MongoDB. Os documentos dentro de uma coleção podem ter campos diferentes. Uma coleção é o equivalente a uma tabela em um sistema de banco de dados relacional.|
|  Database | Um banco de dados armazena uma ou mais coleções de documentos.|
| Mongo| É um banco de dados NoSQL desenvolvido pela MongoDB Inc. O banco de dados MongoDB foi criado para armazenar uma grande quantidade de dados e também executar rapidamente.|



**Connect the database to the metabase**

- step 1: Open localhost:3000
- step 2: Click Admin setting
- step 3: Click Database
- step 4: Adicione os dados de autenticação de  banco de dados 


**Exemplo da conexão mongo  metabase**
|  metabase  | credential  |
|------------|-------------|
|    host    |  mongo  |
|dabase_name | use the name you define in make migrate|
|    user    |   lappis    |
|  password  |   lappis    |

