from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field, ConfigDict

date = datetime.now()


class ExampleModel(BaseModel):
    id: str = Field(
        title="title",
    )
    value_1: str = Field(
        title="value_1",
        min_length=1,
        alias='ValueValue',
    )
    value_2: Optional[int] = Field(
        title="value_2",
        alias='Value2',
        default=None,
    )

    model_config = ConfigDict(
        json_schema_extra={
            "type": "object"
        },
    )


class ModelList(BaseModel):
    items: List[ExampleModel]
    model_config = ConfigDict(
        json_schema_extra={
            "type": "array"
        },
    )


object_schema = ExampleModel.schema()
list_schema = ModelList.schema()
