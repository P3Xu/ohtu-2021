*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input New Command And Create User
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input New Command
    Input Credentials  ka  kalle123
    Output Should Contain  Username is not valid

Register With Valid Username And Too Short Password
    Input New Command
    Input Credentials  kallee  kalle12
    Output Should Contain  Password is not valid

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command
    Input Credentials  kallee  kallellaan
    Output Should Contain  Password is not valid

*** Keywords ***
Input New Command And Create User
    Input New Command
    Input Credentials  kalle  kalle123
