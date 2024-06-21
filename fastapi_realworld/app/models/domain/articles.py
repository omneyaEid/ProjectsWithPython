from typing import List

from fastapi_realworld.app.models.common import DateTimeModelMixin, IDModelMixin
from fastapi_realworld.app.models.domain.profiles import Profile
from fastapi_realworld.app.models.domain.rwmodel import RWModel


class Article(IDModelMixin, DateTimeModelMixin, RWModel):
    slug: str
    title: str
    description: str
    body: str
    tags: List[str]
    author: Profile
    favorited: bool
    favorites_count: int
