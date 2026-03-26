from rich.console import Console
from pyfiglet import Figlet

def print_banner(text):
    console = Console()
    f = Figlet(font='slant')
    banner = f.renderText(text)
    console.print(banner, style="bold green")

if __name__ == "__main__":
    print_banner("Beautiful Terminal")
    console = Console()
    console.print("Добро пожаловать в проект!", style="bold blue")