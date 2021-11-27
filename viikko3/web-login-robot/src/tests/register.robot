*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page And Check Its Open

*** Test Cases ***
Register With Valid Username And Password
    Set Username  einari
    Set Password  narinari666
    Set Confirmation Password  narinari666
    Submit Register Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ei
    Set Password  narinari666
    Set Confirmation Password  narinari666
    Submit Register Credentials
    Register Should Fail With Message  Username is not valid

Register With Valid Username And Too Short Password
    Set Username  einar
    Set Password  narinari
    Set Confirmation Password  narinari
    Submit Register Credentials
    Register Should Fail With Message  Password is not valid

Register With Nonmatching Password And Password Confirmation
    Set Username  einars
    Set Password  narinari666
    Set Confirmation Password  narinari
    Submit Register Credentials
    Register Should Fail With Message  Passwords differs, should be the same

Login After Successful Registration
    Go To Login Page
    Login Page Should Be Open
    Set Username  einari
    Set Password  narinari666
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Go To Login Page
    Login Page Should Be Open
    Set Username  einar
    Set Password  narinari
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Submit Register Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login

Register Should Succeed
    Welcome Page Should Be Open

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Confirmation Password
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Go To Register Page And Check Its Open
    Go To Register Page
    Register Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}
