from typing import TypedDict

from mipac.types.user import ILiteUser


class IClip(TypedDict):
    id: str
    created_at: str
    last_clipped_at: str
    user_id: str
    user: ILiteUser
    name: str
    description: str | None
    is_public: bool
    is_favorited: bool
    favorited_count: int
