# lextab.py. This file automatically created by PLY (version 3.11). Don't edit!
_tabversion   = '3.10'
_lextokens    = set(('ANY', 'FILENAME', 'HEADING', 'NL', 'SERVER'))
_lexreflags   = 64
_lexliterals  = ''
_lexstateinfo = {'INITIAL': 'inclusive', 'heading': 'exclusive', 'tail': 'exclusive'}
_lexstatere   = {'INITIAL': [('(?P<t_HEADING>(nfs://))|(?P<t_NL>(\\n))|(?P<t_ANY>(.))|(?P<t_name_ignore>)', [None, ('t_HEADING', 'HEADING'), None, ('t_NL', 'NL'), None, (None, 'ANY'), None, (None, 'name_ignore')])], 'heading': [('(?P<t_heading_SERVER>([a-zA-Z]+))|(?P<t_heading_ANY>(.))|(?P<t_heading_NL>(\\n))', [None, ('t_heading_SERVER', 'SERVER'), None, ('t_heading_ANY', 'ANY'), None, ('t_heading_NL', 'NL')])], 'tail': [('(?P<t_tail_FILENAME>/([a-zA-Z]+/)+[a-zA-Z]+)|(?P<t_tail_ANY>.)|(?P<t_tail_NL>(\\n))', [None, ('t_tail_FILENAME', 'FILENAME'), None, ('t_tail_ANY', 'ANY'), ('t_tail_NL', 'NL')])]}
_lexstateignore = {'INITIAL': '', 'tail': ''}
_lexstateerrorf = {'INITIAL': 't_error', 'heading': 't_heading_error', 'tail': 't_tail_error'}
_lexstateeoff = {}
