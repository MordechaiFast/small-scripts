import sys
import tty
import termios


def getchar():
    fd = sys.stdin.fileno()
    attr = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSANOW, attr)


EOT = '\x04'  # CTRL+D
ESC = '\x1b'
CSI = '['

if __name__ == '__main__':
  line = ''

  while True:
    c = getchar()
    if c == EOT:
        print('exit')
        break
    elif c == ESC:
        if getchar() == CSI:
            x = getchar()
            if x == 'A':
                print('UP')
            elif x == 'B':
                print('DOWN')
    elif c == '\r':
        print([line])
        line = ''
    else:
        line += c