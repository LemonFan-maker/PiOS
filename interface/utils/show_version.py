from colorama import Fore, Style

def show_version():
    version_info = """
    PyOS v1.0.0-古早版本
    一个简单的基于Python的操作系统(胡扯)
    由OrionisLi(LemonFan-maker)个人开发
    """
    print(Fore.GREEN + version_info + Style.RESET_ALL)