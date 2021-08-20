class Help:
    def __init__(self, me: str) -> None:
        print('Telkom Test : Muhammad Yogi Prasetyo')
        print()
        print('Usage: python3 ' + me + ' [-h] [-t json] [-t text] [-o path]')
        print()
        print('Options:')
        print('     -h       : this help')
        print('     -t json  : set file type to json')
        print('     -t text  : set file type to text')
        print('     -o path  : set path to save file')