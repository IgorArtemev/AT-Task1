from lexerClass import MyLexer
import ply.yacc as yacc

class MyParser(object):
    tokens = MyLexer.tokens

    def __init__(self):
        self.lexer = MyLexer()
        self.parser = yacc.yacc(module=self, optimize=1, debug=False, write_tables=False)

    def check_string(self, s):
        res = self.parser.parse(s)
        return res

    def p_server(self, p):
        '''server : HEADING SERVER FILENAME '''
        p[0]=p[2]

    def p_error(self, p):
        pass


if __name__ == "__main__":
    f = open("sample")
    nf = f.read()
    f.close()
    parser = MyParser()
    print(parser.check_string(nf))