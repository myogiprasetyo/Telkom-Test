from .type import Type

import sys

class Command:
    __command__: list[str] = sys.argv
    me: str = __command__[0]

    def source(self) -> str:
        if len(self.__command__) > 1:
            return self.__command__[1]
        else:
            print('Invalid command')
            exit()

    def type(self) -> Type:
        if '-t' in self.__command__:
            indexParam = self.__command__.index('-t') + 1

            if indexParam < len(self.__command__):
                param = self.__command__[indexParam]

                if param == 'json':
                    return Type.JSON
                elif param == 'text':
                    return Type.TEXT
                else:
                    print(self.me + ': option "-t" parameter is invalid')
                    exit()
            else:
                print(self.me + ': option "-t" requires parameter')
                exit()
        else:
            return Type.TEXT
    
    def output(self) -> str:
        if '-o' in self.__command__:
            indexParam = self.__command__.index('-o') + 1

            if indexParam < len(self.__command__):
                return self.__command__[indexParam]
            else:
                print(self.me + ': option "-o" requires parameter')
                exit()
        else:
            return self.source()

    def help(self) -> bool:
         return '-h' in self.__command__