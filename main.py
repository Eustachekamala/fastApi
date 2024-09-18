from typing import List
from uuid import uuid4, UUID
from fastapi import FastAPI # type: ignore
from models import Gender, Role, User # type: ignore

app = FastAPI()

db : List[User] = [
    User(
        id=UUID("cde241b9-5ad0-4727-a9f3-8c5eec38cf18"),
        first_name="Eustache", 
        last_name="Leroy", 
        email="eustache.leroy@gmail.com",
        password="12345678", 
        gender=Gender.male, 
        roles=[Role.admin, Role.user]
        ),
    User(
        id=UUID("cba6bda3-f6d5-4992-baeb-5dd771cf5f75"),
        first_name="John", 
        last_name="Doe", 
        email="john.doe@gmail.com",
        password="12345678", 
        gender=Gender.male, 
        roles=[Role.user]
        ),
    User(
        id=UUID("55c87985-b52a-4285-bfae-1fbb3d21e352"),
        first_name="Jane", 
        last_name="Doe", 
        email="jane.doe@gmail.com",
        password="12345678", 
        gender=Gender.female, 
        roles=[Role.student]        
        )
]

@app.get("/")
async def get_users():
    return db

@app.post("/")
async def create_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return {"id": user.id}
    return {"error": "User not found"}

@app.get("/{user_id}")
async def get_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            return user
    return {"error": "User not found"}

@app.put("/{user_id}")
async def update_user(user_id: UUID, user: User):
    for user in db:
        if user.id == user_id:
            user.first_name = user.first_name
            user.last_name = user.last_name
            user.email = user.email
            user.password = user.password
            user.gender = user.gender
            user.roles = user.roles
            return user
    return {"error": "User not found"}
