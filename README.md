# BeautifulTerminalProject

Проект для создания красивого и функционального терминала на Python.

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/cubetitled-ui/BeautifulTerminalProject.git
   ```

2. Установите зависимости:
   ```bash
   pip install rich pyfiglet colorama
   ```

3. Запустите:
   ```bash
   python main.py
   ```

## Возможности
- Красивые баннеры с использованием `pyfiglet`.
- Цветной вывод с помощью `rich`.
- Легко расширяемая структура.

## Пример
```python
from rich.console import Console
from pyfiglet import Figlet

console = Console()
f = Figlet(font='slant')

console.print(f.renderText("Hello, World!"), style="bold green")
```