import uvicorn

from fastapi import FastAPI

import schemas
# models ORM

api = FastAPI()

cats = []

@api.get("/")
async def list_cats():
    return cats

@api.put("/add")
async def add_cat(cat: schemas.Cat):
    cats.append(cat)


if __name__ == "__main__":
    uvicorn.run('main:api', reload=True)
    #API