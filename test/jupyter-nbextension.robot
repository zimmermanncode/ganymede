*** Settings ***

Library   String

Resource   ./jupyter.robot

Suite Setup   Run Keyword If   "" in sys.path
...   Evaluate   sys.path.remove("")   modules=sys


*** Test Cases ***

Install
   ${result}   ${output} =   Run Jupyter Process
   ...   nbextension   install   --py   ganymede   --sys-prefix

   @{expected nbextension dirs} =   Create List
   ...   ganymede
   ...   declarativewidgets
   ...   declarativewidgets/urth_components
   ...   declarativewidgets/urth_components/declarativewidgets-explorer

   @{matches} =   Get Regexp Matches   ${output}
   ...   Installing [^>]+ -> (?P<dest>[^\\s]+)   dest
   Should Be Equal   ${expected nbextension dirs}   ${matches}

   @{matches} =   Get Regexp Matches   ${output}
   ...   - Validating:\\s*(\x1b[\\W0-9]+m)?\\s*(OK|ok)
   Length Should Be   ${matches}   4

Enable
   ${result}   ${output} =   Run Jupyter Process
   ...   nbextension   enable   --py   ganymede   --sys-prefix

   @{expected nbextension js paths} =   Create List
   ...   ganymede/ganymede
   ...   declarativewidgets/js/main
   ...   declarativewidgets/js/main
   ...   declarativewidgets/js/main

   @{matches} =   Get Regexp Matches   ${output}
   ...   Enabling notebook extension (?P<path>[^\\.]+)   path
   Should Be Equal   ${expected nbextension js paths}   ${matches}

   @{matches} =   Get Regexp Matches   ${output}
   ...   - Validating:\\s*(\x1b[\\W0-9]+m)?\\s*(OK|ok)
   Length Should Be   ${matches}   4
