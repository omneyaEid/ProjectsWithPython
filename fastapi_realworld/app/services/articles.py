from slugify import slugify

from fastapi_realworld.app.db.errors import EntityDoesNotExist
from fastapi_realworld.app.db.repositories.articles import ArticlesRepository
from fastapi_realworld.app.models.domain.articles import Article
from fastapi_realworld.app.models.domain.users import User


async def check_article_exists(articles_repo: ArticlesRepository, slug: str) -> bool:
    try:
        await articles_repo.get_article_by_slug(slug=slug)
    except EntityDoesNotExist:
        return False

    return True


def get_slug_for_article(title: str) -> str:
    return slugify(title)


def check_user_can_modify_article(article: Article, user: User) -> bool:
    return article.author.username == user.username
