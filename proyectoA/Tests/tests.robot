*** Settings ***
Resource   ../Main/barrel.resource
Test Setup    Handle Test Start
Test Teardown    Handle Test Completion

*** Test Cases ***
Test CTC Connection
    [Documentation]    Test QA
    [Tags]    Pruebas QA    tests    

    I start recording    video_name=Prueba 1
    Sleep    1
    I stop recording
