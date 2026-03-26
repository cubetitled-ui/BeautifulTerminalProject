# BeautifulTerminalProject

Проект для создания красивого и функционального терминала на Python с множеством прикольных фич!

## Установка

### Через pip
1. Установите пакет:
   ```bash
   pip install git+https://github.com/cubetitled-ui/BeautifulTerminalProject.git
   ```
2. Запустите:
   ```bash
   beautiful-terminal
   ```

### Локально
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/cubetitled-ui/BeautifulTerminalProject.git
   ```
2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
3. Запустите:
   ```bash
   python -m beautiful_terminal.main
   ```

## Возможности
- Красивые баннеры с использованием `pyfiglet`.
- Прогресс-бары и таймеры с `rich`.
- ASCII-арт и мемы.
- Игра "Угадай число".
- Случайные цитаты.
- Мониторинг системы (CPU, RAM).
- Эффект печатающегося текста.
- Цветные логи.

## Пример
```python
from beautiful_terminal.main import print_banner

print_banner("Hello, World!")
```