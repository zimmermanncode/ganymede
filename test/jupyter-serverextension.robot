*** Settings ***

Resource   ./jupyter.robot


*** Test Cases ***

Enable
   ${result}   ${output} =   Run Jupyter Process
   ...   serverextension   enable   ganymede
   Should Match Regexp   ${output}
   ...   - Validating...\\s+ganymede\\s*(\x1b[\\W0-9]+m)?\\s*(OK|ok)
