import random
from rich.console import Console
from rich.panel import Panel

console = Console()

quotes = [
    "Лучший способ предсказать будущее — изобрести его. — Алан Кей",
    "Код должен быть простым и красивым. — Линус Торвальдс",
    "Жизнь — это то, что происходит, пока ты строишь другие планы. — Джон Леннон",
    "Простота — это высшая степень изысканности. — Леонардо да Винчи"
]

def random_quote():
    """Выводит случайную цитату."""
    quote = random.choice(quotes)
    console.print(Panel(quote, title="Цитата дня", style="italic cyan"))