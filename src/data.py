from pathlib import Path
from re import compile

PLAYERS_PATH = Path(r'..\data\players.ini')
SAVES_PATH = Path(r'..\data\saves.txt')

MESSAGES = {
    'ввод имени': 'Введите имя игрока: ',
    'некорректное имя': 'Имя игрока должно начинаться с буквы, может состоять из букв, цифр и символа подчеркивания',
}

COMMANDS = {
    'начать новую партию': ('new', 'n', 'начать', 'н'),
    'загрузить существующую партию': ('load', 'l', 'загрузка', 'з'),
    'отобразить раздел помощи': ('help', 'h', 'помощь', 'п'),
    'создать или переключиться на игрока': ('player', 'p', 'игрок', 'и'),
    'отобразить таблицу результатов': ('table', 't', 'таблица', 'т'),
    'изменить размер поля': ('dim', 'd', 'размер', 'р'),
    'выйти': ('quit', 'q', 'выход', 'в'),
}
player_db = {}

TOKENS = ('X', 'O')
players: list[str] = []

dim: int = 3
dim_range = range(dim)
all_cells: int = dim**2

turns: dict[int, str] = {}

PATTERN = compile(r'[A-Za-zА-ЯЁа-яё][A-Za-zА-ЯЁа-яё\d_]+')
STATISTIC = {}
