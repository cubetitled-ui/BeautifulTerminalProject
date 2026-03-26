from rich.console import Console
import time

console = Console()

def typewriter(text, speed=0.05):
    """Эффект печатающегося текста."""
    for char in text:
        console.print(char, end="", style="bold green")
        time.sleep(speed)
    console.print()