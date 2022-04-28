from tkinter.messagebox import NO
from xmlrpc.client import Boolean
from fastapi import Body, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings


print(settings.database_username)

#models.Base.metadata.create_all(bind=engine)


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)



@app.get("/")
def root():
    return {"message": "welcome to KRYPTON CONSOLIDATE"}




#my_posts= [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title": "my favorite foods", "content": "i love ERICA banga", "id": 2}]


# def find_post(id):
#     for p in my_posts:
#         if p["id"] == id:
#             return p


# def find_post_index(id):
#     for i, p in enumerate (my_posts):
#         if p['id'] == id:
#             return i
