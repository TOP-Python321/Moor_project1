from pathlib import Path
from re import compile

PLAYERS_PATH = Path(r'..\data\players.ini')
SAVES_PATH = Path(r'..\data\saves.txt')
HELP_PATH = Path(r'..\data\help.txt')

TITLE = 'КРЕСТИКИ-НОЛИКИ'
HELP_TITLE = 'ПОМОЩЬ'

DEBUG = True
debug_data = {}

PROMPT = ' > '

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
players_db: dict[str, dict[str, int]] = {}
saves_db: dict[tuple[str, str], dict] = {}

TOKENS = ('X', 'O')
WEIGHT_OWN = 1.5
WEIGHT_FOE = 1.0
START_MATRICES = ()

players: list[str] = []

authorized: str

dim: int = 3
dim_range = range(dim)
all_cells: int = dim**2

board: dict[int, str] = dict.fromkeys(range(1, all_cells+1), ' ')
turns: dict[int, str] = {}

field: str = ''

PATTERN = compile(r'[A-Za-zА-ЯЁа-яё][A-Za-zА-ЯЁа-яё\d_]+')
DIM_PATTERN = compile(r'[3-9]|1[0-9]|20')
STATISTIC = {}
