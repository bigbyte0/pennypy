import sys
import os
import subprocess

from penny import Penny
import pathlib
import sys
import pfile

def find_arg(arg_name: str) -> any:
    pass

def find_bool_arg(arg_names: tuple[str, str]) -> bool:
    for arg in sys.argv:
        if arg[2:] in arg_names:
            return True
    return False

def cls() -> None:
    if os.name == 'nt':  # For Windows
        subprocess.run(['cmd', '/c', 'cls'])
    else:  # For Linux and macOS
        subprocess.run(['clear'])

FLAG_USE_DEFAULT_CONFIG = ('d', 'default')
FLAG_REVERSE = ('r', 'reverse')
INPUT_QUIT = ('q', 'quit', 'exit')

class RunConfiguration:
    def __init__(self):
        self.reversed = False

def run():
    p = Penny()
    conf = RunConfiguration()

    if not find_bool_arg(FLAG_USE_DEFAULT_CONFIG):
        # Try reading the config file
        p.config(list(pfile.read_file(".pennyrc")))

    # Read the input file
    with pathlib.Path(sys.argv[1]).open('r') as file:
        p.read(file.readlines())
    cls()

    conf.reversed = sys.argv[2] in FLAG_REVERSE

    for card in p.shuffled():
        print(card.front if not conf.reversed else card.back, end="")
        inp = input()
        if inp in INPUT_QUIT: break
        print(card.back if not conf.reversed else card.front, end="")
        inp = input()
        if inp in INPUT_QUIT: break
        cls()

    print("*** Session Complete ***")

if __name__ == '__main__':
    run()