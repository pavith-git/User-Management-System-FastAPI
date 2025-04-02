from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID, uuid4
from enum import Enum

class Gender(str, Enum):
    male = "male"
    female = "female"

class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"

class User(BaseModel):
    id: UUID = None
    first_name: str
    last_name: str
    gender: Gender
    roles: List[Role]

def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not kwargs.get("id"): 
            object.__setattr__(self, "id", uuid4()) 

class UserUpdateRequest(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    roles: Optional[List[Role]] = None
