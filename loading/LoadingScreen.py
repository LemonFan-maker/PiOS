import curses
import time, sys

def loading_screen(stdscr):
    # Clear screen
    stdscr.clear()
    
    # Get the dimensions of the screen
    height, width = stdscr.getmaxyx()
    
    message = "PyOS正在启动..."
    message_x = (width // 2) - (len(message) // 2)
    message_y = height // 2 - 1
    
    # Total steps for the progress bar
    total_steps = 50
    
    # Loop to create the progress bar
    for i in range(total_steps + 1):
        # Calculate the percentage of completion
        percent_complete = (i / total_steps) * 100
        
        # Create a string that represents the progress bar
        progress_bar = "[" + "=" * i + " " * (total_steps - i) + "]"
        
        # Add the message to the screen
        stdscr.addstr(message_y, message_x, message)
        
        # Calculate the position for the progress bar
        progress_x = (width // 2) - (len(progress_bar) // 2)
        progress_y = height // 2
        
        # Add the progress bar and percentage to the screen
        stdscr.addstr(progress_y, progress_x, f"{progress_bar} {percent_complete:.2f}%")
        
        # Refresh the screen to show changes
        stdscr.refresh()
        
        # Simulate some work being done with varying speed
        if i < 10:
            time.sleep(0.15)
        elif i < 30:
            time.sleep(0.07)
        else:
            time.sleep(0.04)
        stdscr.clear()