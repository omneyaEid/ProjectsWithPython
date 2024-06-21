from fastapi_realworld.app.models.common import DateTimeModelMixin, IDModelMixin
from fastapi_realworld.app.models.domain.profiles import Profile
from fastapi_realworld.app.models.domain.rwmodel import RWModel


class Comment(IDModelMixin, DateTimeModelMixin, RWModel):
    body: str
    author: Profile
