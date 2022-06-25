*** Settings ***
Documentation

*** Variables ***
${email_para_login}            william@gmail.com
${password_para_login}         12345

*** Keywords ***
POST Endpoint /login
    &{payload}                  Create Dictionary       email=${email_para_login}      password=${password_para_login}    
    ${response}                 Create On Session       serverest       /usuarios      data=&{payload}
    Log to Console              Response: ${response.content}
    Set Global Variable         ${response}

Validar Ter Logado
    Should be Equal             ${response.json()["message"]}           Login realizado com sucesso
    Should Not Be Empty         ${response.json()["authorization"]}

Fazer Login e Armazenar Token
    POST Endpoint /login
    Validar Ter Logado
    ${token_auth}           Set Variable             ${response.json()["authorization"]}
    Log To Console          Token Salvo: ${token_auth}
    Set Global Variable       ${token_auth}
     

