from pydantic import BaseModel


class BaseAccount(BaseModel):
    username: str
