from dataclasses import dataclass


@dataclass
class DatabaseConfig:
    db_host: str       # URL-адрес базы данных
    db_user: str       # Username пользователя базы данных
    db_password: str   # Пароль к базе данных
    database: str      # Название базы данных


@dataclass
class TgBot:
    token: str             # Токен для доступа к телеграм-боту
    admin_ids: list[int]   # Список id администраторов бота


@dataclass
class Config:
    tg_bot: TgBot
    db: DatabaseConfig


config = Config(tg_bot=TgBot(token='6960720511:...',
                             admin_ids=[1]),
                db=DatabaseConfig(db_host='DB_HOST',
                                  db_user='DB_USER',
                                  db_password='DB_PASSWORD',
                                  database='DATABASE'))

print(config.tg_bot.token)
print(TgBot.__annotations__)


def example(arg1: int, kwarg1: int = 1) -> int:
    pass


print(example.__annotations__)
print(example.__name__)
