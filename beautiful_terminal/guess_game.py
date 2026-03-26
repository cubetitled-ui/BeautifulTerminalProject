import random
from rich.console import Console
from rich.prompt import Prompt

console = Console()

def guess_number():
    """Игра 'Угадай число'."""
    number = random.randint(1, 100)
    console.print("[bold cyan]Угадай число от 1 до 100![/bold cyan]")
    while True:
        guess = Prompt.ask("Введи число")
        if int(guess) == number:
            console.print("Поздравляю! Ты угадал!", style="bold green")
            break
        elif int(guess) < number:
            console.print("Слишком маленькое число!", style="yellow")
        else:
            console.print("Слишком большое число!", style="red")