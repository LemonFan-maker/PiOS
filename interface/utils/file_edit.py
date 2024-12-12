import os
from colorama import Fore, Style

def edit_file(parts):
    if len(parts) <= 1:
        print(f"{Fore.RED}请指定一个文件进行编辑.{Style.RESET_ALL}")
        return
    
    filename = parts[1]
    try:
        if not os.path.exists(filename):
            with open(filename, 'w') as f:
                pass
            print(f"{Fore.GREEN}新建文件: {filename}{Style.RESET_ALL}")
        
        with open(filename, 'r+') as f:
            content = f.readlines()
        
        print(Fore.BLUE + f"编辑文件: {filename}" + Style.RESET_ALL)
        print(Fore.CYAN + "输入编辑的内容 输入 ':wq' 保存并退出, 或者 ':q!' 放弃更改" + Style.RESET_ALL)
        
        editing = True
        while editing:
            # Display current content
            for i, line in enumerate(content):
                print(f"{i+1}> {line}", end='')
            
            # Prompt for user input
            line_number = len(content) + 1
            user_input = input(f"{line_number}> ")
            
            if user_input == ":wq":
                with open(filename, 'w') as f:
                    f.writelines(content)
                print(f"{Fore.GREEN}保存文件: {filename}{Style.RESET_ALL}")
                editing = False
            elif user_input == ":q!":
                print(f"{Fore.YELLOW}放弃更改{Style.RESET_ALL}")
                editing = False
            else:
                content.append(user_input + '\n')
    
    except Exception as e:
        print(f"{Fore.RED}编辑文件失败: {filename}. 错误: {e}{Style.RESET_ALL}")