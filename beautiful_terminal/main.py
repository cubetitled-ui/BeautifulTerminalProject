from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.prompt import Prompt
from rich.table import Table
from rich.align import Align
from rich.text import Text
from pyfiglet import Figlet
import time

console = Console()
f = Figlet(font='slant')

def print_banner(text):
    """Выводит красивый баннер."""
    banner = f.renderText(text)
    console.print(Panel.fit(banner, style="bold green"), justify="center")

def show_progress_bar():
    """Демонстрация прогресс-бара."""
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
    ) as progress:
        task = progress.add_task("[cyan]Загрузка...", total=100)
        for i in range(100):
            time.sleep(0.05)
            progress.update(task, advance=1)

def countdown_timer(seconds):
    """Таймер обратного отсчёта."""
    with console.status("[bold yellow]Таймер запущен...") as status:
        for i in range(seconds, 0, -1):
            time.sleep(1)
            console.print(Align.center(f"[bold red]{i}[/] секунд..."))
        console.print(Panel.fit("[bold green]✅ Время вышло!", style="bold green"))

def interactive_menu():
    """Интерактивное меню."""
    table = Table(title="Меню", style="bold blue", show_header=True, header_style="bold magenta")
    table.add_column("Опция", style="cyan")
    table.add_column("Описание", style="white")
    table.add_row("1", "Запустить прогресс-бар")
    table.add_row("2", "Запустить таймер (10 секунд)")
    table.add_row("3", "Вывести баннер")
    table.add_row("4", "Выход")

    console.print(table)
    choice = Prompt.ask("\nВыберите опцию", choices=["1", "2", "3", "4"], default="1")

    if choice == "1":
        show_progress_bar()
    elif choice == "2":
        countdown_timer(10)
    elif choice == "3":
        print_banner("Beautiful Terminal")
    else:
        console.print("[bold red]Выход...")

def main():
    console.clear()
    print_banner("Beautiful Terminal")
    console.print(Panel.fit("Добро пожаловать в проект! 🎉", style="bold blue"))

    while True:
        interactive_menu()
        if not Prompt.ask("Продолжить?", choices=["y", "n"], default="y") == "y":
            break

    console.print("[bold green]До свидания! 👋")

if __name__ == "__main__":
    main()