from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppData, WebAppInfo
from typing import Optional
from aiogram.filters.callback_data import CallbackData

class start_panel_factory(CallbackData, prefix="start_panel"):
    action: str
    value: Optional[str] = None
    
    
def start_panel_cb(is_admin: Optional[bool] = False):
    button_list = []
    if is_admin: button_list.append(InlineKeyboardButton(text="Ответить на реквест", web_app=WebAppInfo(url="https://google.com")))
    button_list.append(InlineKeyboardButton(text="Создать реквест", web_app=WebAppInfo(url="https://google.com/shitpost")))
    user_panel_mk = InlineKeyboardMarkup(inline_keyboard=[button_list])
    return user_panel_mk