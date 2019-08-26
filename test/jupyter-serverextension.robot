*** Settings ***

Resource   ./jupyter.robot

Suite Setup   Run Keyword If   "" in sys.path
...   Evaluate   sys.path.remove("")   modules=sys


*** Test Cases ***

Enable
   ${result}   ${output} =   Run Jupyter Process
   ...   serverextension   enable   ganymede

   Should Match Regexp   ${output}
   ...   - Validating...[\\s\\n]+ganymede\\s+([\\w\\.]+\\s*)?(\x1b[\\W0-9]+m)?\\s*(OK|ok)
