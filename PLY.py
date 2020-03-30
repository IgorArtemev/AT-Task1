import generator
import re
import time
from parserClass import MyParser


class RecognizerPLY(object):
    __Servers_file = 'PLY\\servers'
    __result_file = 'PLY\\result'
    __time_file = 'PLY\\time'
    __file = False
    __Servers_A = dict()

    def __init__(self, from_file=False):
        self.__parser = MyParser(from_file)
        self.__file = from_file

    def check_strings_from_file(self, data):
        self.__Servers_A.clear()
        f_time = open(self.__time_file, 'w')
        start_time = time.perf_counter()

        f = open(data)
        nf = f.read()
        f.close()

        self.__parser.check_string(nf)
        self.__Servers_A = self.__parser.get_A()

        f_time.write(str(time.perf_counter() - start_time) + '\n')
        f_time.close()

    def check_strings_from_console(self):
        self.__Servers_A.clear()
        working = True
        print('Input your line or "exit" to exit:')

        while working:
            user_string = input()
            if user_string == "exit":
                working = False
                break
            if user_string != "":
                user_string += ("\n")
            if (len(user_string)>69):
                print("- ERROR\n")
            else:
                self.__parser.check_string(user_string)
                if self.__parser.get_A().keys():
                    print("- OK\n")
                    res = list(self.__parser.get_A().keys())[0]

                    if self.__Servers_A.get(res) is None:
                        self.__Servers_A.setdefault(res, 1)
                    else:
                        self.__Servers_A[res] += 1
                else:
                    print("- ERROR\n")

        print('Statistic: \n')
        for key in self.__Servers_A:
            print(str(key) + ' ' + str(self.__Servers_A.get(key)) + '\n')

    def analyze_Servers(self):
        f_Servers = open(self.__Servers_file, 'w')
        for key in self.__Servers_A:
            f_Servers.write(str(key) + ' ' + str(self.__Servers_A.get(key)) + '\n')
        f_Servers.close()

    def get_Servers(self):
        return self.__Servers_A

    def get_Time(self):
        return self.__time_file


if __name__ == "__main__":

    dialog = True

    while dialog:
        dialog = False
        print('Hello, how do your want to input lines (file or console)')
        input_type = input()
        if input_type == "file":
            print("Input filename:")
            filename = input()
            generator.Generator(10000, filename)
            recognizer = RecognizerPLY(True)
            recognizer.check_strings_from_file(filename)
            recognizer.analyze_Servers()
            print("Data saved to files")
            print("Show statistic (yes to show):")
            input_show = input()
            if input_show == "yes":
                Servers_A = recognizer.get_Servers()
                for key in Servers_A:
                    print(str(key) + ' ' + str(Servers_A.get(key)) + '\n')
                try:
                    f = open(recognizer.get_Time())
                    nf = f.read()
                    print("Time:", nf.split('\n')[1])

                    f.close()
                except IOError as e:
                    print("---- Error ----")

        elif input_type == "console":
            recognizer = RecognizerPLY(True)
            recognizer.check_strings_from_console()
        else:
            print("You are wrong! Try again")
            dialog = True

