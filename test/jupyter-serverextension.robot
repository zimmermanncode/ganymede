*** Settings ***

Resource   ./jupyter.robot


*** Test Cases ***

Enable
   ${result}   ${output} =   Run Jupyter Process
   ...   serverextension   enable   ganymede
   Should Match Regexp   ${output}   - Validating...\\s+ganymede\\s+(OK|ok)
