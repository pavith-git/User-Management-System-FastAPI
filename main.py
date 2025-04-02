from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from models import User, Gender, Role, UserUpdateRequest
from uuid import UUID, uuid4

app = FastAPI()

# In-memory database
db: List[User] = [
    User(
        id=uuid4(),
        first_name="John",
        last_name="Doe",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    ),
    User(
        id=uuid4(),
        first_name="Jane",
        last_name="Smith",
        gender=Gender.female,
        roles=[Role.student]
    )
]

@app.get("/api/users")
def get_users():
    return db

@app.post("/api/users")
def add_user(user: User):
    user.id=uuid4()
    db.append(user)  # User's id will be automatically set in the User model
    return {"id": user.id}

@app.put("/api/users/{user_id}") 
def update_user(user_update: UserUpdateRequest, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return {"message": f"User {user_id} updated successfully"}
    raise HTTPException(status_code=404, detail=f"User {user_id} not found")

@app.delete("/api/users/{user_id}")
def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return {"message": f"User {user_id} deleted successfully"}
    raise HTTPException(status_code=404, detail=f"User {user_id} not found")
