# Desafio da NeoWay

O desafio é descrito no arquivo challenge.md, em geral consiste em desenvolver um serviço que faz ingestão de dados em uma base SQL.
De cara, me pareceu algo interessante. Então segui pensando em uma solução.

Primeiramente preparei o ambiente, conforme o desafio sugere.
- Postgres
- Python3

A solução que eu desenvolvi consiste em:
- Um serviço web que recebe o diretório
- Acessar os arquivos desse diretório
- Para cada arquivo, executar a leitura em chunks. Utilizei pandas, que facilita bastante esse tipo de cenário. Me baseei no template exemplo descrito no challange.
- Criei um pool de threads para inserção dos dados no postgres. 

Obs1: A escrita no banco foi utilizando o execute do psycogp2, onde eu concatenei os valores ao invés de usar o executemany. Isso deu um bom ganho de performance de escrita.

Obs2: Não consegui testar o copy nativo do postgres, por falta de tempo. Basicamente eu iria parsear os arquivos de entrada e gerar um arquivo sql relacionado e executar a escrita direto com o comando copy, suspeito que os ganhos seriam maiores, mas poderiamos perder o track de erros de inserção.

Para rodar a solução, basta:

## Execução Sem Docker
### Criar o esquema do banco:
 - Criar um banco de dados;
 - Connectar no banco e executar o arquivo `init.sql`

### Instalar os requisitos
- Na pasta do projeto:
```
pip install -r requirements.txt
```

### Atualizar o arquivo de configurações
```
Arquivo src/utils/project.config
```

### Iniciar o projeto
```
python src/server.py
```

### Utilizando alguma ferramenta de Rest Client (eu utilizo o Postman) enviar o request para o serviço.
Exemplo:
```
http://localhost:8080/upload?dir=G:\Fabio\workspace\neoway\\data
```
Importante: Inserir os dados de autorização, com Basic Auth. O jeito correto seria utilizando a base de dados e uma tabela de Usuário, por falta de tempo, deixei diretamente no código. Sim, com certeza, é um ponto de melhoria. 
```
username: admin
password: thesecret
```

## Execução com Docker

Na pasta do projeto, executar os comandos:
```
- docker-compose build
- docker-compose up
```

O docker está simples.
Criei um Dockerfile com python e adicionei as variáveis do postgres.
No docker-compose, inseri a imagem do postgres como serviço.
Em alguns casos não consegui executar os testes por problema de paths para ambientes Windows e Linux.


### Camada de testes
Na pasta raiz do projeto executar:
```
python -m unittest discover
```