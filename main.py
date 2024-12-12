import curses
import colorama
from loading.LoadingScreen import loading_screen
from interface.Command import command_line_interface

def main():
    colorama.init(autoreset=True)
    # Start with the loading screen using curses
    curses.wrapper(loading_screen)
    
    # After loading screen, switch to command line interface
    command_line_interface()

if __name__ == "__main__":
    main()



