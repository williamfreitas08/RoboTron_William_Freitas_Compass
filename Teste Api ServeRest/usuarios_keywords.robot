*** Settings ***
Documentation       Keywords e Variáveis para Ações do enpoint de usuarios
Library             RequestsLibrary
Resource            ./common.robot

*** Variables ***
${nome_do_usuario}          herbert richards
${senha_do_usuario}         teste123
${email_do_usuario}         testeteste@gmail.com

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


#Sessão para criação de Keywords Personalizadas
*** Keywords ***
Criar Sessao
    Create Session          serverest           http://localhost:3000

GET Endpoint /usuarios
    ${response}             GET On Session      serverest       /usuarios
    Set Global Variable     ${response}

POST Endpoint /usuarios
    &{payload}              Create Dictionary       nome=${nome_do_usuario}    email=${email_do_usuario}     password=${senha_do_usuario}      administrador=true
    ${response}             POST On Session      serverest       /usuarios      data=&{payload}
    Log to Console          Response: ${response.content}
    Set Global Variable     ${response}

PUT Endpoint /usuarios
    &{payload}              Create Dictionary       nome=adelma oliveira    email=adelma@gmail.com     password=132345      administrador=true
    ${response}             PUT On Session          serverest           /usuarios       data=&{payload}
    Log to Console          Response: ${response.content}
    Set Global Variable     ${response}

DELETE Endpoint /usuarios
    ${response}             DELETE On Session          serverest           /usuarios 
    Log to Console          Response: ${response.content}
    Set Global Variable     ${response}

Validar Quantidade "${quantidade}"
    Should Be Equal         ${response.json()["quantidade"]}    ${quantidade}

Validar Se Mensagem Contem "${palavra}"
    Should Contain          ${response.json()["message"]}       ${palavra}

Printar Conteudo Response
    Log To Console      Response: ${response.json()["usuarios"][0]["nome"]}

Criar Usuario Estatico Valido
    ${json}            Importar JSON Estatico           json_usuario_ex.json
    ${payload}         Set Variable         $