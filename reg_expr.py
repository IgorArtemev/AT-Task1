import generator
import re
import time


class RecognizerRE:
    __A = []
    __Servers_A = dict()
    __result_file = 'Reg_Expr\\result'
    __time_file = 'Reg_Expr\\time'
    __servers_file = 'Reg_Expr\\servers'
    __file = False

    def __init__(self, from_file=False, strings=None):
        self.__file = from_file
        if from_file:
            self.__f = open(self.__result_file, 'w')
            self.__strings = strings

    def __del__(self):
        if self.__file:
            self.__f.close()

    def check_strings_from_console(self):
        self.__Servers_A.clear()
        working = True
        print('Input your line or "exit" to exit:')

        while working:
            user_string = input()
            if user_string == "exit":
                working = False
                break
            if (len(user_string)>69):
                print("- ERROR\n")
            else:
                rex = re.match(r'(nfs://)([a-zA-Z]+)/([a-zA-Z]+/)+[a-zA-Z]+$', user_string)

                if rex is not None:
                    print("- OK\n")
                    result = rex.group(2)
                    print(result)
                    if self.__Servers_A.get(result) is None:
                        self.__Servers_A.setdefault(result, 1)
                    else:
                        self.__Servers_A[result] += 1
                else:
                    print("- ERROR\n")

        print('Statistic: \n')
        for key in self.__Servers_A:
            if self.__Servers_A.get(key) >= 1:
                print(str(key) + ' ' + str(self.__Servers_A.get(key)) + '\n')

    def check_strings_from_file(self):
        self.__Servers_A.clear()
        f_time = open(self.__time_file, 'w')
        f_time.write('iter time' + '\n')
        f_time = open(self.__time_file, 'a')
        start_time = time.perf_counter()
        count = 0
        for i in range(len(self.__strings) - 1):

            if(len(self.__strings[i])>69):
                self.__f.write(self.__strings[i] + ' - ERROR' + '\n')
            else:
                rex = re.match(r'(nfs://)([a-zA-Z]+)/([a-zA-Z]+/)+[a-zA-Z]+$', self.__strings[i])
    
                if rex is not None:
                    count += 1
                    self.__f.write(self.__strings[i] + ' - OK' + '\n')
                    server_name = rex.group(2)
                    if self.__Servers_A.get(server_name) is None:
                        self.__Servers_A.setdefault(server_name, 1)
                    else:
                        self.__Servers_A[server_name] += 1
                else:
                    self.__f.write(self.__strings[i] + ' - ERROR' + '\n')
        f_time.write(str(time.perf_counter() - start_time) + '\n')
        f_time.close()
        print(count)

    def get_file_content(self):
        try:
            __f = open(self.__result_file)
        except IOError as e:
            self.check_strings_from_file()
            __f = open(self.__result_file)

        nf = __f.read()
        self.__A = nf.split('\n')

        __f.close()
        return self.__A

    def get_Servers(self):
        return self.__Servers_A

    def get_Time(self):
        return self.__time_file

    def analyze_Servers(self):
        f_Servers = open(self.__servers_file, 'w')
        for key in self.__Servers_A:
            if self.__Servers_A.get(key) >= 1:
                f_Servers.write(str(key) + ' ' + str(self.__Servers_A.get(key)) + '\n')
        f_Servers.close()


if __name__ == "__main__":

    dialog = True

    while dialog:
        dialog = False
        print('Hello, how do your want to input lines (file or console)')
        input_type = input()
        if input_type == "file":
            print("Input filename:")
            filename = input()
            all_strings = generator.Generator(100000, filename).get_file_content()
            recognizer = RecognizerRE(True, all_strings)
            recognizer.check_strings_from_file()
            recognizer.analyze_Servers()
            print("Data saved to files")
            print("Show statistic (yes to show):")
            input_show = input()
            if input_show == "yes":
                Servers_A = recognizer.get_Servers()
                for key in Servers_A:
                    if Servers_A.get(key) >= 1:
                        print(str(key) + ' ' + str(Servers_A.get(key)) + '\n')
                try:
                    f = open(recognizer.get_Time())
                    nf = f.read()
                    print("Time:", nf.split('\n')[1])

                    f.close()
                except IOError as e:
                    print("---- Error ----")

        elif input_type == "console":
            recognizer = RecognizerRE()
            recognizer.check_strings_from_console()
        else:
            print("You are wrong! Try again")
            dialog = True