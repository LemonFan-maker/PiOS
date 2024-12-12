import os
import shutil
from colorama import Fore, Style

def remove_file_or_directory(parts):
    if len(parts) <= 1:
        print(f"{Fore.RED}指定一个文件或者目录进行删除.{Style.RESET_ALL}")
        return
    
    path = parts[1]
    force = False
    
    if len(parts) > 2 and parts[2] == '-rf':
        force = True
    
    try:
        if not os.path.exists(path):
            print(f"{Fore.RED}路径不存在: {path}{Style.RESET_ALL}")
            return
        
        if os.path.isfile(path):
            os.remove(path)
            print(f"{Fore.GREEN}删除文件: {path}{Style.RESET_ALL}")
        elif os.path.isdir(path):
            if force:
                shutil.rmtree(path)
                print(f"{Fore.GREEN}强制删除目录: {path}{Style.RESET_ALL}")
            else:
                shutil.rmtree(path)
                print(f"{Fore.GREEN}删除目录: {path}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}错误的路径: {path}{Style.RESET_ALL}")
    
    except Exception as e:
        print(f"{Fore.RED}删除失败: {path}. 错误: {e}{Style.RESET_ALL}")
