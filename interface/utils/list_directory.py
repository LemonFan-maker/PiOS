import os
from colorama import Fore, Style

def list_directory(parts):
    path = parts[1] if len(parts) > 1 else '.'
    try:
        items = os.listdir(path)
        for item in items:
            print(item)
    except FileNotFoundError:
        print(f"{Fore.RED}目录未找到: {path}{Style.RESET_ALL}")
    except PermissionError:
        print(f"{Fore.RED}无权限: 无法列出'{path}'之下的文件.{Style.RESET_ALL}")
