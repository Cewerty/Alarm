from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Optional
from db import get_db, PostInDB, sync_engine, Session
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqladmin import Admin
from admin_panel import PostAdmin

app = FastAPI()
admin = Admin(app=app, engine=sync_engine, session_maker=Session, base_url='/admin')
admin.add_view(PostAdmin)

templates = Jinja2Templates(directory="templates/")

class Post(BaseModel):
    title: str
    content: str

@app.get("/post", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("post_form.html", {"request": request})

@app.post("/post/create", response_model=Post)
async def post_form(post: Post, request: Request, db: AsyncSession = Depends(get_db)):
    post = Post(title=post.title, content=post.content)
    db_post = PostInDB(**post.model_dump())
    db.add(db_post)
    await db.commit()
    await db.refresh(db_post)
    return post
    
    
# @app.get('/post/created')
# async def answer_post_creation():
#     print('Goida!')


@app.get('/')
async def get_test_answer(request: Request):
    return {"message": "Hello World"}

@app.get('/post/show')
async def show_post(db=Depends(get_db)):
    result = await db.execute(select(PostInDB))
    posts = result.scalars().all()
    return posts
    