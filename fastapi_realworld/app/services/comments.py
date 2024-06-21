from fastapi_realworld.app.models.domain.comments import Comment
from fastapi_realworld.app.models.domain.users import User


def check_user_can_modify_comment(comment: Comment, user: User) -> bool:
    return comment.author.username == user.username
