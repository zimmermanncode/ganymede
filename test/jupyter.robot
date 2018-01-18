*** Settings ***

Library   Process


*** Keywords ***

Run Jupyter Process
   [Arguments]   ${subcommand}   @{args}
   ${result} =   Run Process   jupyter   ${subcommand}   @{args}
   ...   stdout=stdout.txt   stderr=stderr.txt
   Should Be Equal As Integers   ${result.rc}   0
   [Return]   ${result}   ${result.stderr}
