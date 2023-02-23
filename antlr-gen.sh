#!/bin/sh

export CLASSPATH=".:$(pwd)/lib/antlr-4.10.1-complete.jar:$CLASSPATH"
alias antlr4='java -jar $(pwd)/lib/antlr-4.10.1-complete.jar'

antlr4 -Dlanguage=Python3 src/antlr/BlaiseLexer.g4 -o gen
