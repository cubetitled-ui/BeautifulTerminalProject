from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from rich.console import Console

console = Console()

def demo_ascii_art():
    """Запускает анимацию ASCII-арта."""
    def demo(screen):
        effects = [
            Cycle(screen, FigletText("WOW!", font='big'), int(screen.height / 2 - 8)),
            Stars(screen, 200)
        ]
        screen.play([Scene(effects, 500)])
    
    Screen.wrapper(demo)

def show_meme():
    """Показывает случайный мем."""
    meme = """
     ╱|、
    (˛•̮˛ )
    /   ⋊   \\
    |  ⊙_⊙  |
    \  ͜ʖ  /
     `⊙´⊙´
    """
    console.print("[bold magenta]Мем:[/bold magenta]")
    console.print(meme, style="bold yellow")