import psutil
from rich.console import Console

console = Console()

def system_info():
    """Выводит информацию о системе."""
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    console.print(f"[bold blue]CPU:[/bold blue] {cpu}% | [bold blue]RAM:[/bold blue] {ram}%")