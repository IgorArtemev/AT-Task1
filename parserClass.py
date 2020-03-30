from lexerClass import MyLexer
import ply.yacc as yacc

class MyParser(object):
    tokens = MyLexer.tokens
    __Servers_A = dict()
    __A = []
    __servers_file = 'PLY\\servers'
    __result_file = 'PLY\\result'
    count = 0

    def get_A(self):
        return self.__Servers_A

    def __init__(self, from_file=False):
        self.__file = from_file
        self.lexer = MyLexer()
        self.parser = yacc.yacc(module=self, optimize=1, debug=False, write_tables=False)

    def check_string(self, code):
        self.__Servers_A.clear()
        if self.__file:
            self.__f = open(self.__result_file, 'w')
        result = self.parser.parse(code)
        print(self.count)
        if self.__file:
            self.__f.close()
        return result

    def p_server_list(self, p):
        '''server_list : server
        | server_list server '''


    def p_server(self, p):
        '''server : HEADING SERVER FILENAME NL'''
        if self.__file:
            string=str(p[1]) + str(p[2]) + str(p[3])
            if len(string)<=69:
                self.__f.write(string + ' - OK\n')
                self.count += 1
            else:
                self.__f.write(string + ' - ERROR\n')
        if self.__Servers_A.get(p[2]) is None:
            self.__Servers_A.setdefault(p[2], 1)
        else:
            self.__Servers_A[p[2]] += 1

    def p_server_zero_err_type(self, p):
        'server : err_list NL'
        if self.__file:
            self.__f.write(p[1] + ' - ERROR\n')

    def p_server_first_err_type(self, p):
        'server : HEADING err_list NL'
        if self.__file:
            self.__f.write(str(p[1]) + str(p[2]) + ' - ERROR\n')

    def p_server_second_err_type(self, p):
        'server : HEADING SERVER err_list NL'
        if self.__file:
            self.__f.write(str(p[1]) + str(p[2]) + str(p[3]) + ' - ERROR\n')

    def p_func_forth_err_type(self, p):
        'server : HEADING SERVER FILENAME err_list NL'
        if self.__file:
            self.__f.write(str(p[1]) + str(p[2]) + str(p[3]) + str(p[4]) + ' - ERROR\n')

    def p_err_list_type3(self, p):
        '''err_list : err_list err'''
        p[0] = p[1]
        p[0] += p[2]

    def p_err_list_type1(self, p):
        '''err_list : '''

    def p_err_list_type2(self, p):
        '''err_list : err'''
        p[0] = p[1]

    def p_err(self, p):
        '''err : ANY'''
        p[0] = p[1]

    def p_error(self, p):
        print('Unexpected token:', p)


if __name__ == "__main__":
    f = open("sample")
    nf = f.read()
    f.close()
    parser = MyParser()
    print(parser.check_string(nf))