from typing import Generic, TypeVar

from django.db.models import Model

T = TypeVar('T', bound=Model)


class BaseRepository(Generic[T]):
    model: T = None
