from pydantic import BaseModel

from fastapi_realworld.app.models.domain.profiles import Profile


class ProfileInResponse(BaseModel):
    profile: Profile
