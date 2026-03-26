from rich.console import Console

console = Console()

def log(message, level="info"):
    """Выводит цветные логи."""
    colors = {"info": "green", "warning": "yellow", "error": "red"}
    console.print(f"[{level.upper()}] {message}", style=colors[level])