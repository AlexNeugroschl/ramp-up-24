from pydantic import BaseModel

class BookTemplate(BaseModel):
    title:str
    author:str
    year:int