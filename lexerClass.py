# coding=utf8
import ply.lex as lex
from ply.lex import TOKEN
import re


class MyLexer(object):
    states = (
        ('heading', 'exclusive'),
        ('tail', 'exclusive'),
    )

    tokens = (
        'HEADING', 'ANY', 'NL', 'SERVER', 'FILENAME',
    )

    t_ANY = r'(.)'

    def t_HEADING(self, t):
        r'(nfs://)'
        if t.lexer.current_state() == 'heading':
            t.lexer.begin('tail')
        else:
            t.lexer.begin('heading')
        return t

    def t_NL(self, t):
        r'(\n)'
        t.lexer.lineno += len(t.value)
        return t

    def t_heading_SERVER(self, t):
        r'([a-zA-Z]+)'
        if t.lexer.current_state() == 'tail':
            t.lexer.begin('INITIAL')
        else:
            t.lexer.begin('tail')
        return t

    def t_heading_ANY(self, t):
        r'(.)'
        t.lexer.begin('INITIAL')
        return t

    def t_heading_NL(self, t):
        r'(\n)'
        t.lexer.lineno += len(t.value)
        t.lexer.begin('INITIAL')
        return t

    def t_tail_FILENAME(self, t):
        r'/([a-zA-Z]+/)+[a-zA-Z]+'
        t.lexer.begin('INITIAL')
        return t
    
    def t_tail_ANY(self, t):
        r'.'
        t.lexer.begin('INITIAL')
        return t

    def t_tail_NL(self, t):
        r'(\n)'
        t.lexer.lineno += len(t.value)
        t.lexer.begin('INITIAL')
        return t

    t_name_ignore = ''
    t_tail_ignore = ''
    t_ignore = ''

    def t_heading_error(self, t):
        print("Illegal character in HEADING '%s'" % t.value[0])
        t.lexer.begin('INITIAL')

    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.begin('INITIAL')

    def t_tail_error(self, t):
        print("Illegal character in TAIL'%s'" % t.value[0])
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