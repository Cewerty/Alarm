from sqladmin import Admin, ModelView
from db import Session, sync_engine, PostInDB
# from main import PostInDB

class PostAdmin(ModelView, model=PostInDB):
    column_list = [PostInDB.id, PostInDB.title, PostInDB.content]
    name = 'Посты'
    name_plural = 'Посты'
    category = 'Работа с постами'
    can_create = True
    can_delete = True
    can_edit = True
    can_export = False
