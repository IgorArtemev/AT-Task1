import AppClass_sm


class AppClass:
    def __init__(self):
        self.__counter=0
        self.__substring = ''
        self.__name = ''
        self._fsm = AppClass_sm.AppClass_sm(self)
        self._is_acceptable = False
        self._fsm.enterStartState()

    def ClearSMC(self):
        self.__substring = ''
        self.CounterZero()
        self.clearSubstring()
        self._is_acceptable = True

    def CheckString(self, string):
        self._fsm.Heading()
        for c in string:
            if not self._is_acceptable:
                break
            if c.isalpha():
                self.__substring+=c
                self._fsm.Alpha()
            elif c == ':':
                self._fsm.Colon()
            elif c == '/':
                self._fsm.Slash()
            else:
            	self._fsm.Unknown()
        self._fsm.EOS()
        if self._is_acceptable:
            return self.__name
        else:
            return None

    def Acceptable(self):
        self._is_acceptable = True

    def Unacceptable(self):
        self._is_acceptable = False

    def CounterInc(self):
        self.__counter += 1

    def CounterZero(self):
        self.__counter=0

    def isValidHeading(self):
        return self.__counter <= 3

    def isValid(self):
        return self.__counter <= 63
    def isValidName(self):
        return self.__substring
    def checkHeading(self):
        return self.__substring == "nfs"

    def clearSubstring(self):
        self.__substring = ''

    def set_name(self):
        self.__name = self.__substring
