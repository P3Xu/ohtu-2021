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
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ei
    Set Password  narinari666
    Set Confirmation Password  narinari666
    Submit Credentials
    Register Should Fail With Message  Username is not valid

Register With Valid Username And Too Short Password
    Set Username  einar
    Set Password  narinari
    Set Confirmation Password  narinari
    Submit Credentials
    Register Should Fail With Message  Password is not valid

Register With Nonmatching Password And Password Confirmation
    Set Username  einars
    Set Password  narinari666
    Set Confirmation Password  narinari
    Submit Credentials
    Register Should Fail With Message  Passwords differs, should be the same

*** Keywords ***
Submit Credentials
    Click Button  Register

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
