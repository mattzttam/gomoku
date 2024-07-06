import curses
import signal
import sys

def signal_handler(signal, frame):
    sys.exit(0)

def main(stdscr):
    stdscr.clear()
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.refresh()

    signal.signal(signal.SIGINT, signal_handler)

    while True:
        try:
            stdscr.refresh()
        except Exception as e:
            stdscr.refresh()
        curses.endwin()

if __name__ == "__main__":
    curses.wrapper(main)
