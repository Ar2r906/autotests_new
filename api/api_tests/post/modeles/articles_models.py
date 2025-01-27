from pydantic import BaseModel, Field
from datetime import datetime

class ArticlesModels(BaseModel):
    id: int = Field(gt=1, title='id')
    title: str = Field(title='title', min_length=3)
    content: str = Field(title='content', min_length=3)
    image: str = Field(title='image', default=None)
    createdAt: datetime = Field(title='createdAt')
    updatedAt: datetime = Field(title='updatedAt')