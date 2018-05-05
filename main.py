#!/usr/bin/env python3

# Load the ebnf grammar 
# Convert it to the NDFA
# Convert the NDFA to DFA
# Optimize DFA by minimizing it's states

from pygramm import parse_ebnf

if __name__ == "__main__":
    parse_ebnf( "a =    \"0\"   |       \"1\"   ;" )
    

