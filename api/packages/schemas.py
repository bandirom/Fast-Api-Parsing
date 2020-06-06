from pydantic import BaseModel


class UrlBase(BaseModel):
    title: str
    url: str
    context: str


class MainUrlList(UrlBase):
    id: int


class MainUrlCreate(UrlBase):
    is_main: bool = True

    class Config:
        orm_mode = True
