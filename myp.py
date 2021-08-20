from bin.command import Command
from bin.file import File
from bin.help import Help
from bin.type import Type

command = Command()

if command.help():
    Help(command.me)
else:
    file = File(command.source())
    type = command.type()
    path = command.output()

    file.save(type, path)