from typing import Dict, List

__COLOR_END         = '\033[0m'
__BLACK             = '\033[0;30m'
__DARK_GRAY         = '\033[1;30m'
__RED               = '\033[0;31m'
__BRIGHT_RED        = '\033[1;31m'
__GREEN             = '\033[0;32m'
__BRIGHT_GREEN      = '\033[1;32m'
__YELLOW            = '\033[0;33m'
__BRIGHT_YELLOW     = '\033[1;33m'
__BLUE              = '\033[0;34m'
__BRIGHT_BLUE       = '\033[1;34m'
__MAGENTA           = '\033[0;35m'
__BRIGHT_MARENTA    = '\033[1;35m'
__CYAN              = '\033[0;36m'
__BRIGHT_CYAN       = '\033[1;36m'
__BRIGHT_GRAY       = '\033[0;37m'
__WHITE             = '\033[1;37m'

# COLOR = 

COLOR: Dict[str, List[str]] = {
    'RED'       : [__RED, __COLOR_END],
    'GREEN'     : [__GREEN, __COLOR_END],
    'BLUE'      : [__BLUE, __COLOR_END],
    'CYAN'      : [__CYAN, __COLOR_END],
    'MAGENTA'   : [__MAGENTA, __COLOR_END],
    'YELLOW'    : [__YELLOW, __COLOR_END],
}

def __usage(msg: str):
    print(msg.join(COLOR['RED']))
    print(msg.join(COLOR['GREEN']))
    print(msg.join(COLOR['BLUE']))

if __name__ == "__main__":
    __usage("Hello World")
    for (name, color) in COLOR.items():
        print(name, "test text".join(color))