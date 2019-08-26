*** Settings ***

Resource   ./jupyter.robot


*** Test Cases ***

Enable
   ${result}   ${output} =   Run Jupyter Process
   ...   serverextension   enable   ganymede
   Should Match Regexp   ${output}
   ...   - Validating...[\\s\\n]+ganymede\\s+([\\w\\.]+\\s+)?(OK|ok)
