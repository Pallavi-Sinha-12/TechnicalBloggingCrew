from fastapi import FastAPI
from typing import List
from models import Blog
from database import db

app = FastAPI()

@app.post("/publish/blog/")
async def publish_blog(blog: Blog):
    status = db.add_blog(blog)
    if not status:
        return {"success" : False}
    return {"success" : True}

@app.get("/blogs/", response_model=List[Blog])
async def get_blogs():
    return db.get_blogs()