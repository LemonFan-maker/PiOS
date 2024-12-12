import platform
from colorama import Fore, Style

def show_system_info():
    info = {
        "系统": platform.system(),
        "节点名称": platform.node(),
        "发行版本": platform.release(),
        "版本": platform.version(),
        "架构": platform.machine(),
        "处理器": platform.processor()
    }
    print(Fore.BLUE + "系统信息:" + Style.RESET_ALL)
    for key, value in info.items():
        print(f"{Fore.WHITE}{key}: {value}{Style.RESET_ALL}")