*** Settings ***
Documentation             Keywords e Variaveis para Ações do endpoint produtos

*** Variables ***
${token_auth}             Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImZ1bGFub0BxYS5jb20iLCJwYXNzd29yZCI6InRlc3RlIiwiaWF0IjoxNTg5NzU4NzQ2LCJleHAiOjE1ODk3Njg3NDZ9.B6TASHV8k9xBerz4NSeFBlAZGSDhZlqESt767M0567I

*** Keywords ***
POST Endpoint /produtos
    &{header}                   Create Dictionary       Authorization
    &{payload}                  Create Dictionary       nome=MouseTech      preco=400     descricao=Mouse    quantidade=100
    ${response}                 POST On Session         serverest       /produtos      data=&{payload}      headers=&{header}                 Create
    Log to Console              Response: ${response.content}
    Set Global Variable         ${response}
