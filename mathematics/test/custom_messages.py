from colorama import Fore

def show_success_message(message: str):
    print(f"{Fore.GREEN} ✓ {Fore.WHITE} {message}")

def show_failed_message(message: str):
    print(f"{Fore.RED} X Error: {Fore.WHITE} {message}")