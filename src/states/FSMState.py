from aiogram.dispatcher.filters.state import StatesGroup, State


class UrlGiv(StatesGroup):
    get_link = State()
    get_name = State()