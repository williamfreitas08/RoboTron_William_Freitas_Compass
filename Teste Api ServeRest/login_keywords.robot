*** Settings ***
Documentation

*** Variables ***
${email_para_login}            william@gmail.com
${password_para_login}         12345

*** Keywords ***
POST Endpoint /Login
    &{payload}                  Create Dictionary       email=${email_para_login}      password=${password_para_login}    
    ${response}                 Create On Session       serverest       /usuarios      data=&{payload}
    Log to Console              Response: ${response.content}
    Set Global Variable         ${response}
