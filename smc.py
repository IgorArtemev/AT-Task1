import generator
import time
import AppClass


class RecognizerSMC:

    __A = []
    __Servers_A = dict()
    __result_file = 'Smc\\result'
    __time_file = 'Smc\\time'
    __servers_file = 'Smc\\servers'
    __file = False

    def __init__(self, from_file=False, strings=None):
        self.__file = from_file
        self.__smc = AppClass.AppClass()
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

            res = self.__smc.CheckString(user_string)

            if res is not None:
                print("- OK\n")
                if self.__Servers_A.get(res) is None:
                    self.__Servers_A.setdefault(res, 1)
                else:
                    self.__Servers_A[res] += 1
            else:
                print("- ERROR\n")

        print('Statistic: \n')
        for key in self.__Servers_A:
            print(str(key) + ' ' + str(self.__Servers_A.get(key)) + '\n')

    def check_strings_from_file(self):
        self.__Servers_A.clear()
        f_time = open(self.__time_file, 'w')
        f_time.write('iter time' + '\n')
        f_time = open(self.__time_file, 'a')
        start_time = time.perf_counter()
        count = 0
        for i in range(len(self.__strings) - 1):
            res = self.__smc.CheckString(self.__strings[i])
            if res is None:
                self.__f.write(self.__strings[i] + ' - OK' + '\n')
            else:
                count += 1
                self.__f.write(self.__strings[i] + ' - ERROR' + '\n')
                if self.__Servers_A.get(res) is None:
                    self.__Servers_A.setdefault(res, 1)
                else:
                    self.__Servers_A[res] += 1
        f_time.write(str(time.perf_counter() - start_time)+'\n')
        f_time.close()
        print(count)

    def get_Servers(self):
        return self.__Servers_A

    def get_Time(self):
        return self.__time_file

    def get_file_content(self):
        try:
            self.__f = open(self.__result_file)
        except IOError as e:
            self.check_strings_from_file()
            self.__f = open(self.__result_file)

        nf = self.__f.read()
        self.__A = nf.split('\n')

        self.__f.close()
        return self.__A

    def analyze_servers(self):
        f_servers = open(self.__servers_file, 'w')
        for key in self.__Servers_A:
            f_servers.write(str(key) + ' ' + str(self.__Servers_A.get(key)) + '\n')
        f_servers.close()


if __name__ == "__main__":

    dialog = True

    while dialog:
        dialog = False
        print('Hello, how do your want to input lines (file or console)')
        input_type = input()
        if input_type == "file":
            print("Input filename:")
            filename = input()
            all_strings = generator.Generator(1000000, filename).get_file_content()
            recognizer = RecognizerSMC(True, all_strings)
            recognizer.check_strings_from_file()
            recognizer.analyze_servers()
            print("Data saved to files")
            print("Show statistic (yes to show):")
            input_show = input()
            if input_show == "yes":
                Server_A = recognizer.get_Servers()
                for key in Server_A:
                    print(str(key) + ' ' + str(Server_A.get(key)) + '\n')
                try:
                    f = open(recognizer.get_Time())
                    nf = f.read()
                    print("Time:", nf.split('\n')[1])

                    f.close()
                except IOError as e:
                    print("---- Error ----")
        elif input_type == "console":
            recognizer = RecognizerSMC()
            recognizer.check_strings_from_console()
        else:
            print("You are wrong! Try again")
            dialog = True