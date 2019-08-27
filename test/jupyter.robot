*** Settings ***

Library   Process


*** Keywords ***

Run Jupyter Process
   [Arguments]   ${subcommand}   @{args}
   ${python} =   Evaluate   sys.executable   modules=sys

   ${result} =   Run Process   ${python}   -m   jupyter
   ...   ${subcommand}   @{args}
   ...   stdout=stdout.txt   stderr=stderr.txt

   Should Be Equal As Integers   ${result.rc}   0
   [Return]   ${result}   ${result.stderr}