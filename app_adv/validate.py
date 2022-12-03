import pydantic
from errors import ApiException


class CreateOwnerSchema(pydantic.BaseModel):
    email: str
    password: str


class CreateAdvertisementSchema(pydantic.BaseModel):
    title: str
    description: str
    owner_id: int


def validate(data: dict, schema_class):
    try:
        return schema_class(**data).dict()
    except pydantic.ValidationError as er:
        raise ApiException(400, er.errors())
