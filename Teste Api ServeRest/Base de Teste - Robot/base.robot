*** Settings ***
Documentation       Arquivo simples para requisições HTTP em APIs
Library             RequestsLibrary

#Sessão para criação dos cenários de teste
*** Test Cases ***
Cenario: GET Todos os usuarios 200
    Criar Sessao
    GET Endpoint /usuarios
    Validar Status Code "200"

Cenario: POST Cadastrar usuario 201
    Criar Sessao
    POST Endpoint /usuarios
    Validar Status Code "201"

Cenario: PUT Editar usuario 200
    Criar Sessao
    PUT Endpoint /usuarios
    Validar Status Code "200"


#Sessão para criação de Keywords Personalizadas
*** Keywords ***
Criar Sessao
    Create Session          serverest           http://localhost:3000

GET Endpoint /usuarios
    ${response}             GET On Session      serverest       /usuarios
    Set Global Variable     ${response}

Validar Status Code "${statuscode}"
    Should Be True          ${response.status_code} == ${statuscode}

POST Endpoint /usuarios
    &{payload}              Create Dictionary       nome=william freitas    email=william@gmail.com     password=12345      administrador=true
    ${response}             POST On Session      serverest       /usuarios      data=&{payload}
    Log to Console          Response: ${response.content}
    Set Global Variable     ${response}
