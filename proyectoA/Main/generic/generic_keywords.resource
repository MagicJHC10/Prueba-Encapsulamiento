*** Settings ***
Library    SeleniumLibrary
Library    generic_functions.py
Library    ScreenCapLibrary
Library    OperatingSystem

Resource    generic_variables.resource

*** Comments ***

This file contains generic keywords that can be used across multiple test cases.

*** Keywords ***
Handle Test Start
    [Documentation]    
    ...                = DESCRIPTION =
    ...                Keyword to handle the initial setup required at the start of the test.
    ...       
    ...                = EXAMPLES =    
    ...                ``Handle Test Start``
    Change Directory
    
Handle Test Completion
    [Documentation]    
    ...                = DESCRIPTION =
    ...                Keyword to handle the cleanup required at the end of the test.
    ...       
    ...                = EXAMPLES =    
    ...                ``Handle Test Completion``
    Run Keyword If Test Passed    Set Test Message    PASSED
    Run Keyword If Test Failed    Set Test Message    FAILED
    Run    powershell -command "[System.Reflection.Assembly]::LoadWithPartialName('System.Windows.Forms'); $notification = New-Object System.Windows.Forms.NotifyIcon; $notification.Icon = [System.Drawing.SystemIcons]::Information; $notification.BalloonTipText = 'Execution of ${TEST NAME} has ${TEST MESSAGE}'; $notification.Visible = $true; $notification.ShowBalloonTip(3000); Start-Sleep 3; $notification.Dispose()"
    Close All Browsers
    Sleep    2
    Run Keyword If    '${RUNNING_FIRST_TIME_START_VIDEO}' == 'False'    Run Keyword If Test Failed    I stop recording


I open browser
    [Documentation]    
    ...                = DESCRIPTION =
    ...                Keyword to open a browser with the specified URL and browser type.
    ...    
    ...                = ARGUMENTS =
    ...                | url     | (Optional) The URL to open. Defaults to `${default_url}`. |
    ...                | browser | (Optional) The browser type to use. Defaults to `firefox`. |
    ...       
    ...                = EXAMPLES =    
    ...                ``I open browser    ${url}    chrome``
    ...                ``I open browser    ${default_url}``
    [Arguments]    ${url}=${default_url}    ${browser}=firefox
    ${service}=    Evaluate    sys.modules['selenium.webdriver.firefox.service'].Service(log_output=None)    sys, selenium.webdriver
    Open Browser    ${url}    ${browser}    service=${service}
    Maximize Browser Window

I start recording
    [Documentation]
    ...                = DESCRIPTION =
    ...                Will delete the recordings and start recording the screen
    ...    
    ...                = ARGUMENTS =
    ...                | video_name | The name of the video |
    ...                | monitor | The monitor to record |
    ...    
    ...                == EXAMPLES ==    
    ...                ``I start recording    ${video_name}    ${monitor}``
    [Tags]    Recording
    [Arguments]    ${video_name}=Default_test_video    ${monitor}=1
    Set Global Variable    ${RUNNING_FIRST_TIME_START_VIDEO}    False
    Start Video Recording    name=${video_name}    monitor=${monitor}

I stop recording
    [Documentation]
    ...                = DESCRIPTION =
    ...                Will stop the recording and move is to the results folder
    ...    
    ...                = ARGUMENTS =
    ...                | alias | The alias of the recording |
    ...    
    ...                == EXAMPLES ==    
    ...                ``I stop recording    ${alias}``
    [Tags]    Recording
    [Arguments]    ${alias}=None
    Sleep    2
    Stop Video Recording    alias=${alias}