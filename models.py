from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel # type: ignore
from enum import Enum

class Gender(str, Enum):
    male = "male"
    female = "female"
    
class Role(str, Enum):
    user = "user"
    admin = "admin"
    student = "student"

class User(BaseModel):
    id:Optional[UUID] = uuid4()
    first_name:str
    last_name:str
    email:str
    password:str
    gender:Gender
    roles:List[Role]
    
   