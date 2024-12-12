import os
from colorama import Fore, Style

def cat_file(parts):
    if len(parts) <= 1:
        print(f"{Fore.RED}请指定要查看的文件{Style.RESET_ALL}")
        return
    
    filename = parts[1]
    try:
        if not os.path.exists(filename):
            print(f"{Fore.RED}文件不存在: {filename}{Style.RESET_ALL}")
            return
        
        with open(filename, 'r') as f:
            content = f.read()
        
        print(Fore.BLUE + f"文件名称: {filename}" + Style.RESET_ALL)
        print(content)
    
    except Exception as e:
        print(f"{Fore.RED}读取文件失败: {filename}. 错误: {e}{Style.RESET_ALL}")



