#!/bin/bash

pip install -q -r requirements.txt
antlr4 -Dlanguage=Python3 SCLang.g4

echo 'Build Complete...'
