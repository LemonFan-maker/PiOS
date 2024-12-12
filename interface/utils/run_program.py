import subprocess
from colorama import Fore, Style

def run_program(parts):
    if len(parts) <= 1:
        print(f"{Fore.RED}请指定要运行的程序.{Style.RESET_ALL}")
        return
    
    program_name = parts[1]
    args = parts[2:]  # Collect all arguments after the program name
    try:
        result = subprocess.run([program_name] + args, check=True, text=True, capture_output=True)
        print(Fore.YELLOW + result.stdout + Style.RESET_ALL)
    except Exception as e:
        print(f"{Fore.RED}运行程序{program_name}失败. 错误: {e}{Style.RESET_ALL}")