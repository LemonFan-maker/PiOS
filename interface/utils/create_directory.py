import os
from colorama import Fore, Style

def make_directory(parts):
    if len(parts) <= 1:
        print(f"{Fore.RED}请指定一个目录进行创建{Style.RESET_ALL}")
        return
    
    path = parts[1]
    recursive = False
    
    if len(parts) > 2 and parts[2] == '-p':
        recursive = True
    
    try:
        if recursive:
            os.makedirs(path, exist_ok=True)
            print(f"{Fore.GREEN}创建目录 (递归): {path}{Style.RESET_ALL}")
        else:
            os.mkdir(path)
            print(f"{Fore.GREEN}创建目录: {path}{Style.RESET_ALL}")
    
    except FileExistsError:
        print(f"{Fore.YELLOW}目录已经存在: {path}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}创建目录失败: {path}. 错误: {e}{Style.RESET_ALL}")
