import os
from colorama import Fore, Style

def change_directory(parts):
    path = parts[1] if len(parts) > 1 else '~'
    try:
        expanded_path = os.path.expanduser(path)
        os.chdir(expanded_path)
        print(f"{Fore.GREEN}切换目录到: {os.getcwd()}{Style.RESET_ALL}")
    except FileNotFoundError:
        print(f"{Fore.RED}目录未找到: {path}")
    except PermissionError:
        print(f"{Fore.RED}无权限: 不能够进入目录 '{path}'. 你没有该权限.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}出现错误： {e}{Style.RESET_ALL}")
