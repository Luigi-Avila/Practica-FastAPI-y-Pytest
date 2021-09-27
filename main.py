# fastapi CRUD de post y test con pytest 
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Text, Optional
from datetime import datetime
from uuid import uuid4 as uuid


app = FastAPI()
posts = []

# Modelado de datos con basemodel
class Post(BaseModel):
    id:Optional[str]
    title: str
    author: str
    content: Text
    created_at: datetime = datetime.now()
    published_at: Optional[datetime]
    published: bool = False

# Funciones HTTP

@app.get('/')
async def read_main():
    return {"welcome": "Hola mundo"}

# Mostrar los post

@app.get('/posts')
def get_post():
    return posts

# Metodo de guardar

@app.post('/posts')
def save_post(post: Post):
    post.id = str (uuid())
    posts.append(post.dict())
    return posts[-1]

# Metodo de obtener un solo post

@app.get('/posts/{post_id}')
def get_post(post_id: str):
    for post in posts:
        if post["id"] == post_id:
            return post
    raise HTTPException(status_code=404, detail="Post no encontrado")

# Metodo eliminar post

@app.delete('/posts/{post_id}')
def delete_post(post_id: str):
    for index, post in enumerate(posts):
        if post["id"] == post_id:
            posts.pop(index)
            return {"message": "Post eliminado correctamente"}
    raise HTTPException(status_code=404, detail="Post no encontrado")

# Metodo actualizar post

@app.put('/posts/{post_id}')
def update_post(post_id: str, updatedPost: Post):
    for index, post in enumerate[posts]:
        if post["id"] == post_id:
            posts[index]["title"] = updatedPost.title
            posts[index]["content"] = updatedPost.content
            posts[index]["author"] = updatedPost.author
            return {"mesage": "Post Actualizado Correctamente"}
    raise HTTPException(status_code=404, detail="Post no encontrado")

