from collections import Counter
import string
import random


class Generator:

    def __init__(self, num=100000, __input_file='strings',__accuracy=0.95):
        self.__accuracy=__accuracy
        self.__n = num
        self.__input_file =__input_file
        self.__A = []
        try:
            self. __f = open(self.__input_file)
        except IOError as e:
            self.__f = open(self.__input_file, 'w')
            self.generate_file()

    def __del__(self):
        self.__f.close()

    def get_num(self):
        return self.__n

    def get_file_content(self):
        try:
            f = open(self.__input_file)
        except IOError as e:
            self.generate_file()
            f = open(self.__input_file)

        nf = f.read()
        self.__A = nf.split('\n')

        f.close()
        return self.__A

    def damage(self):
        return random.random()

    def generate_server(self):
        if self.damage() > self.__accuracy:
            server = ''.join(random.choice(string.ascii_letters + string.digits+ string.punctuation) for _ in range(random.randint(0,10)))
        else:
            server = ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(1,10)))
        return  server

    def generate_file_name(self):
        path_length = random.randint(0,12)
        s=''
        for i in range(path_length):
            if self.damage() > self.__accuracy:
                s=s+''.join(random.choice(string.punctuation))
            else:
                s=s+''.join('/')
            if self.damage() > self.__accuracy:
                s=s+''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(random.randint(0,8)))
            else:
                s=s+''.join(random.choice(string.ascii_letters) for _ in range(random.randint(0,8)))
        return s
   
    def generate_string(self):
        if self.damage() > self.__accuracy:
            heading=''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(random.randint(0,5)))
        else:
            heading='nfs://'
        return ''.join(heading + self.generate_server() + self.generate_file_name())

    def generate_file(self):
        for _ in range(self.__n):
            self.__f.write(self.generate_string() + '\n')


if __name__ == "__main__":

    Generator()