from .utils.run_program import run_program
from .utils.change_directory import change_directory
from .utils.list_directory import list_directory
from .utils.show_sysinfo import show_system_info
from .utils.show_version import show_version
from .utils.file_edit import edit_file
from .utils.open_file import cat_file
from .utils.delete_file import remove_file_or_directory
from .utils.create_directory import make_directory
from colorama import Fore, Style
import difflib

def command_line_interface():
    print(f"{Fore.CYAN}PyOS 命令行界面{Style.RESET_ALL}")
    print(f"{Fore.CYAN}键入 'help' 展示可用的命令{Style.RESET_ALL}")
    running = True
    history = []
    current_index = -1
    
    while running:
        try:
            prompt = f"\n{Fore.BLUE}PyOS> {Style.RESET_ALL}"
            user_input = input(prompt).strip()
            
            if user_input:
                history.append(user_input)
                current_index = len(history) - 1
                
                running = handle_command(user_input)
        except KeyboardInterrupt:
            print("\n退出...")
            running = False
        except EOFError:
            print("\n退出...")
            running = False

def handle_command(command):
    parts = command.split()
    cmd = parts[0].lower()

    available_commands = [
        "exit", "help", "ls", "cd", "run", "sysinfo", "version",
        "edit", "cat", "rm", "mkdir"
    ]

    if cmd == "exit":
        return False
    elif cmd == "help":
        show_help()
    elif cmd == "ls":
        list_directory(parts)
    elif cmd == "cd":
        change_directory(parts)
    elif cmd == "run":
        run_program(parts)
    elif cmd == "sysinfo":
        show_system_info()
    elif cmd == "version":
        show_version()
    elif cmd == "edit":
        edit_file(parts)
    elif cmd == "cat":
        cat_file(parts)
    elif cmd == "rm":
        remove_file_or_directory(parts)  
    elif cmd == "mkdir":
        make_directory(parts)
    else:
        similar_commands = difflib.get_close_matches(cmd, available_commands, n=3, cutoff=0.6)
        if similar_commands:
            suggestions = ', '.join(similar_commands)
            print(f"{Fore.YELLOW}未知命令: {cmd}. 是这个吗: {suggestions}?{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}未知命令: {cmd}{Style.RESET_ALL}")
    return True

def show_help():
    help_text = [
        "目前可用的命令:",
        "  help - 展示这条帮助命令",
        "  ls - 列出目录内容",
        "  cd - 改变目录",
        "  run - 运行程序",
        "  exit - 退出PyOS",
        "  sysinfo - 显示系统信息",
        "  version - 显示PyOS版本和介绍",
        "  edit - 编辑文件",
        "  cat - 查看文件",
        "  rm - 删除文件(夹)",
    ]
    print("\n".join(help_text))