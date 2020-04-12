# coding=utf8
import ply.lex as lex
from ply.lex import TOKEN
import re


class MyLexer(object):

    tokens = (
        'HEADING', 'SERVER', 'FILENAME',
    )


    def t_HEADING(self, t):
        r'(nfs://)'
        return t

    def t_SERVER(self, t):
        r'([a-zA-Z]+)'
        return t

    def t_FILENAME(self, t):
        r'(/([a-zA-Z]+/)+[a-zA-Z]+)'
        return t

    def t_ANY(self, t):
        r'.'
        return t
        
    t_ignore = ''

    def t_error(self, t):
        t.lexer.skip(1)
        t.lexer.begin('INITIAL')

    def input(self, data):
        return self.lexer.input(data)

    def token(self):
        return self.lexer.token()

    def __init__(self):
        self.lexer = lex.lex(module=self, optimize=True)


if __name__ == "__main__":
    f = open("sample")
    nf = f.read()
    f.close()
    lexer = MyLexer()
    lexer.input(nf)
    while True:
        tok = lexer.token()  
        if not tok:
            break
        if tok.type == "HEADING":
            print('\n')

        print(tok.type, tok.value)