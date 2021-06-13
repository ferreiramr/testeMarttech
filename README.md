# TESTE MARTTECH - MARCOS FERREIRA

Projeto desenvolvido como teste do processo seletivo para a vaga de desenvolvedor Python.

O escopo do projeto consiste em crir um bloco de anotações utilizando biblioteca FastAPI na AWS Lambada gerenciada pelo AWS API Gateway.

## SITUAÇÃO DO PROJETO

    - CRUD finalizada com funcionalidades essenciais coberta por testes e projeto com deploy na Heroku e na AWS Lambda.
    - Na Heroku há uma falha no acesso a variável que armazenas as notas, nos teste locais não foi possível reproduzir o erro, possívelmente persistindo os dados das notas em um banco de dados esta falha seja eliminada.
    - Não houve tempo hábil para implementar a persistencia das notas no AWS DynamoDB.

## REFERÊNCIAS

- [Live de Python #113 - FastAPI - Com João Lugão](https://www.youtube.com/watch?v=MxlS5_MI_WY)
- [FastAPI Documentation](https://fastapi.tiangolo.com/#example)
- [Simple Serverless FastAPI with AWS Lambda](https://www.youtube.com/watch?v=6fE31084Uks)
- [Failed to load API definition after hosting the app on AWS](https://github.com/tiangolo/fastapi/issues/2787)

## TODO

 - [x] Entender as funcionalidades essências da FastAPI

 - [X] Dominar as funcionalidades essências da FastAPI

 - [x] Criar um modelo de **Nota**

 - [x] Criar um modelo de **Notas**

 - [x] Implementar a view para **adicionar nota**

 - [x] Implementar a view para **obter uma nota a partir de seu id**
 
 - [x] Implementar a view para **obter todas as notas**
 
 - [x] Implementar a view para **atualziar uma nota**
 
 - [x] Implementar a view para **excluir uma nota**
 
 - [x] Implementar a view para **excluir todas as notas**

 - [x] Implementar teste unitários nas principais funcionalidades das views

 - [x] Entender as fucionalidades essências da **AWS Lambada**

 - [x] Entender as fucionalidades essências do **AWS API Gateway**

 - [x] Entender as fucionalidades essências do **AWS DinamoDB**

 - [x] Dominar as fucionalidades básicas da **AWS Lambada**

 - [x] Entender as fucionalidades básicas do **AWS API Gateway**

 - [x] Entender as fucionalidades básicas do **AWS DinamoDB**

 - [x] Realizar o deploy a API na **AWS Lambada** (no ententano occore uma falha ao acessar o Swagger, as outras funcionalidades funcional normalmente)

 - [x] Gerenciar o acesso à API no **AWS API Gateway**

 - [ ] Implementar a persistencia das notas no ***AWS  DinamoDB**

 *As tarefas que utilizam os serviços da AWS não poderam ser implementas devido à alguma erro em minha conta, a Amazon estipulou um prazo de 24h para o acesso ser permitido.*


## ESTUDOS FUTUROS

Para utilizar de maneira mais efetiva a FastAPI é necessários estudar mais os seguintes tópicos:

- [pydantic - Frameowork para gerenciar validação de dados utilizando annotations](https://pydantic-docs.helpmanual.io/)

- [typing - Biblioteca para realizar checagem de tipos](https://docs.python.org/3/library/typing.html)

- [Starlette - Frameowork base da FastAPI](https://pydantic-docs.helpmanual.io/)

- [pytest - Framework para testes](https://docs.pytest.org/)

- [Swagger - Framework para documentação de APIs utilizada pela FastAPI](https://swagger.io/)

- [OpemAPI - Iniciativa que padroniza boas práticas no desenvolvimento de APIs](https://www.openapis.org/)