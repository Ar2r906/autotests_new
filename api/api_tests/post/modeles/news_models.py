from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

date = datetime.now()

class NewsModel(BaseModel):
    id: int = Field(title='id', gt=1)
    title: str = Field(title='title', min_length=1)
    content: str = Field( title='content')
    image: str = Field(default=None, title='image')
    createdAt: datetime = Field(title='createdAt')
    updatedAt: datetime = Field(title='updatedAt')
