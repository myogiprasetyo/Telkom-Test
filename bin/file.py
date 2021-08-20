from .type import Type

from datetime import datetime

import json
import os

class File:
    def __init__(self, path: str) -> None:
        self.__path = path

    def __uniquePath__(self, type: Type, path: str) -> str:
        filename, extension = os.path.splitext(path)
        index = 1

        if self.__path == path:
            if type == Type.JSON:
                extension = '.json'
            elif type == Type.TEXT:
                extension = '.txt'

            path = filename + extension
        
        while os.path.exists(path):
            path = filename + '_' + str(index) + extension
            index += 1

        return path

    def readJson(self) -> list[object]:
        list = []
        source = open(self.__path, 'r')
        lines = source.read().splitlines()

        for line in lines:
            text = line.split(' ')

            if line.lower() == 'stack trace:':
                None
            elif '#' in text[0]:
                dict = list[len(list) - 2]
                trace = {
                    'number': text[0].replace('#', '').strip(),
                    'info': line.replace(' '.join({text[0]}), '').strip()
                }
                
                if 'trace' in dict:
                    dict['trace'].append(trace)
                else:
                    dict['trace'] = [trace]
            else:
                dict = {
                    'datetime': ' '.join({text[0].strip(), text[1].strip()}),
                    'status': text[2].replace('[', '').replace(']', '').strip(),
                    'code': text[3].replace(':', '').strip()
                }

                if '*' in text[4]:
                    dict['total'] = text[4].replace('*', '').strip()

                dict['info'] = line.replace(' '.join([text[0], text[1], text[2], text[3], text[4]]), '').strip()
                
                list.append(dict)

        source.close()

        return json.dumps(list, indent = 4)

    def readText(self) -> list[str]:
        source = open(self.__path, 'r')
        text = source.read().splitlines()

        source.close()

        return text

    def save(self, type: Type, path: str) -> None:
        destination = open(self.__uniquePath__(type, path), 'w+')

        if type == Type.JSON:
            for text in self.readJson():
                destination.write(text)
        elif type == Type.TEXT:
            for text in self.readText():
                destination.write(text)

        destination.close()