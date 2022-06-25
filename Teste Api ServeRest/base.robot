*** Settings ***
Documentation       Arquivo simples para requisições HTTP em APIs
Library             RequestsLibrary
Resource            ./usuarios.keywords.robot
Resource            ./login_keywords.robot
Resource            ./produtos_keywords.robot

#Sessão para criação dos cenários de teste
*** Test Cases ***
Cenario: GET Todos os usuarios 200
    [Tags]      GET
    Criar Sessao
    GET Endpoint /usuarios
    Validar Status Code "200"
    Validar Quantidade "${2}"
    Printar Conteudo Response

Cenario: POST Cadastrar usuario 201
    [Tags]      POST
    Criar Sessao
    POST Endpoint /usuarios
    Validar Status Code "201"

Cenario: PUT Editar usuario 200
    [Tags]      PUT
    Criar Sessao
    PUT Endpoint /usuarios
    Validar Status Code "200"

Cenario: DELETE Deletar usuario 200
    [Tags]      DELETE
    Criar Sessao
    DELETE Endpoint /usuarios
    Validar Status Code "200"

Cenario: POST Realizar Login 200
    [Tags]      POSTLOGIN
    Criar Sessao
    POST Endpoint /login
    Validar Status Code "200"

Cenario: POST Criar Produto 201
    [Tags]       POSTPRODUTO
    Criar Sessao
    Fazer Login e Armazenar Token
    POST Endpoint /produtos
    Validar Status Code "201"

Cenario: DELETE Excluir Produto 200
    [Tags]      DELETEPRODUTO
    Criar Sessao
    Fazer Login e Armazenar Token
    Criar Um Produto e Armazenar ID
    DELETE Endpoint /produtos
    Validar Status Code "200"

Cenario: POST Criar Usuario de Massa Estatico 201
    [Tags]      POSTCRIARUSUARIOESTATICO
    Criar Sessao
    Criar Usuario Estatico Valido
    Validar Status Code "201"

#Sessão para criação de Keywords Personalizadas
*** Keywords ***
Criar Sessao
    Create Session          serverest           http://localhost:3000
