"""
"""
import re

# Regexp for matching whitespaces
whs_re = re.compile( "\s+" )

def normalize_text( data ):
    """
    Reduce number of white characters
    """
    return whs_re.sub( " ", data )

def parse_rule( data  ):
    eq_pos = data.find("=")
    end_pos = data.find(";")
    
    if eq_pos == -1 or end_pos == -1:
        raise Exception("Error parsing rule")
    
    name = data[ 0 : eq_pos - 1 ]
    body = data[ eq_pos + 1 : end_pos ]
    
    print( name )
    print( body )

def parse_ebnf( data ):
    normalized_data = normalize_text( data )
    parse_rule( normalized_data )

