"""
Beautiful Terminal — набор инструментов для красивого и функционального терминала.

Функции:
- ASCII-арт и мемы
- Цветные логи
- Игра "Угадай число"
- Случайные цитаты
- Мониторинг системы
- Эффект печатающегося текста
"""
from .main import main, print_banner, show_progress_bar, countdown_timer, interactive_menu
from .ascii_art import demo_ascii_art, show_meme
from .logger import log
from .guess_game import guess_number
from .quotes import random_quote
from .system_monitor import system_info
from .typewriter import typewriter